import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

class GrapheneEngine:
    def __init__(self, data_path="./resources", db_path="./graphene_db"):
        self.data_path = data_path
        self.db_path = db_path
        self.embeddings = OllamaEmbeddings(model="mxbai-embed-large")
        self.llm = Ollama(model="llama3.2:3b", temperature=0.3)
        
        # Initialize Vector Store
        if not os.path.exists(db_path) or not os.listdir(db_path):
            self.build_knowledge_base()
        else:
            self.vectorstore = Chroma(persist_directory=db_path, embedding_function=self.embeddings)

    def build_knowledge_base(self):
        print("Indexing Research Materials...")
        loader = DirectoryLoader(self.data_path, glob="./*.pdf", loader_cls=PyPDFLoader)
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=80)
        chunks = splitter.split_documents(docs)
        self.vectorstore = Chroma.from_documents(chunks, self.embeddings, persist_directory=self.db_path)

    def generate_prompt(self, intent):
        # 1. Similarity Search
        docs = self.vectorstore.similarity_search(intent, k=3)
        context = "\n\n".join([d.page_content for d in docs])
        
        # 2. Structured Generation
        template = """
        ROLE: Senior AI Prompt Architect.
        CONTEXT FROM RESEARCH: {context}
        USER INTENT: {intent}
        
        TASK: Create a comprehensive Master Prompt. 
        CRITICAL: Use [bracketed_variables] for any parts the user might want to customize later.
        
        MASTER PROMPT:
        """
        prompt_template = ChatPromptTemplate.from_template(template)
        chain = prompt_template | self.llm
        return chain.invoke({"context": context, "intent": intent})