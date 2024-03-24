from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA


class MyChatBot:

    def __init__(self):
        # Initialize attributes to None
        self.DB_FAISS_PATH = "vectorstore/db_faiss"
        self.custom_prompt_template = """Use the following pieces of information to answer the user's question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer. Look for a suiting protocol and find your answer. If it looks like the patient is in danger write "EMERGENCY" and nothing else.

        Context: {context}
        Question: {question}

        Only return the helpful answer below and nothing else.
        Helpful answer:
        """
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
        )
        return qa_chain

    # Loading the model
    def load_llm(self):
        # Load the locally downloaded model here
        llm = CTransformers(
            model="model/llama-2-7b-chat.ggmlv3.q8_0.bin",
            model_type="llama",
            max_new_tokens=512,
            temperature=0.5,
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
        response = self.chain({"query": query})
        return response
