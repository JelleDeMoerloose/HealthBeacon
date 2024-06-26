from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from logic.patient import Patient
from abc import ABC, abstractmethod
import os


class IChatBot(ABC):
    @abstractmethod
    def final_result(self, query: str, patient_as_context: Patient) -> dict[str, str]:
        pass


class ChatBotV1(IChatBot):

    def __init__(
        self,
        prompt_files=os.path.normpath(
            os.path.join(os.path.dirname(__file__), "data", "prompts", "default")
        ),
    ):
        # Vectorstore database path for storing the embeddings of the hospital protocol
        self.DB_FAISS_PATH = "vectorstore/db_faiss"

        # Custom prompt template for QA retrieval
        self.custom_prompt_template = None
        self.custom_prompt_template_unformatted = """<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>
Example questions:
{examples}
User message:
Patient information: {patient_context}
{user_message}
[/INST]"""

        # Prompt file path
        self.prompt_files = prompt_files

        # Patient id
        self.patient_id = None

        # Load the QA model
        self.chain = None

    def set_custom_prompt(self):
        """
        Prompt template for QA retrieval for each vectorstore
        """
        prompt = PromptTemplate(
            template=self.custom_prompt_template,
            input_variables=["context", "question"],
        )
        return prompt

    # Retrieval QA Chain
    def retrieval_qa_chain(self, llm, prompt, db):
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(search_kwargs={"k": 2}),
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt},
            # verbose=True,
        )
        return qa_chain

    # Loading the model
    def load_llm(self):
        # Load the locally downloaded model here

        config = {
            "max_new_tokens": 256,
            "temperature": 0,
            # "n_gpu_layers": -1,   # 'n_gpu_layers' is an invalid keyword argument for from_pretrained()
            "context_length": 4096,
            # verbose:True,
        }

        llm = CTransformers(
            # model="model/llama-2-7b-chat.Q8_0.gguf",
            # faster, download from https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q5_K_M.gguf
            # model="model/llama-2-7b-chat.Q5_K_M.gguf",
            model="model/llama-2-7b-chat.ggmlv3.q8_0.bin",
            model_type="llama",
            config=config,
        )

        # print(dir(llm))
        # print(llm._identifying_params)

        return llm

    # QA Model Function
    def qa_bot(self):
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
        )
        db = FAISS.load_local(
            self.DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True
        )
        llm = self.load_llm()
        qa_prompt = self.set_custom_prompt()
        qa = self.retrieval_qa_chain(llm, qa_prompt, db)

        return qa

    # output function

    def final_result(self, query: str, patient: Patient) -> dict[str, str]:
        # print("Patient: ", patient)

        if self.patient_id != patient.id or self.chain is None:
            # Update patient id
            self.patient_id = patient.id

            # Custom prompt template for QA retrieval
            system_prompt = open(
                os.path.join(self.prompt_files, "system_prompt.txt"), "r"
            ).read()
            examples = open(os.path.join(self.prompt_files, "examples.txt"), "r").read()
            user_message = open(
                os.path.join(self.prompt_files, "user_message.txt"), "r"
            ).read()
            self.custom_prompt_template = (
                self.custom_prompt_template_unformatted.format(
                    system_prompt=system_prompt,
                    patient_context=str(patient),
                    examples=examples,
                    user_message=user_message,
                )
            )

            # Build new chain with correct patient context
            self.chain = self.qa_bot()

        # print("Custom prompt template: ", self.custom_prompt_template)
        print("Query: ", query)

        response = self.chain.invoke({"query": query})

        print("Response: ", response)

        return response
