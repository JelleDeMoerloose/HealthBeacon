from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
import os

class MyChatBot:

    def __init__(self, prompt_files=os.path.normpath(os.path.join(os.path.dirname(__file__), "data", "prompts", "default"))):
        # Initialize attributes to None

        # Vectorstore database path for storing the embeddings of the hospital protocol
        self.DB_FAISS_PATH = "vectorstore/db_faiss"

        # Custom prompt template for QA retrieval
        system_prompt = open(os.path.join(prompt_files, "system_prompt.txt"), "r").read()        
        user_message = open(os.path.join(prompt_files, "user_message.txt"), "r").read()
        self.custom_prompt_template = """<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>

{user_message} [/INST]""".format(
            system_prompt=system_prompt,
            user_message=user_message
        )

        # Load the QA model
        self.chain = self.qa_bot()

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
        llm = CTransformers(
            model="model/llama-2-7b-chat.Q8_0.gguf",
            model_type="llama",
            max_new_tokens=512,
            temperature=0.5,
            n_gpu_layers=-1,
            # verbose=True,
        )
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
    def final_result(self, query):
        response = self.chain.invoke({"query": query})
        return response
