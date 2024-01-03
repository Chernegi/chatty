import os
from langchain.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter


class Chatty:
    def __init__(self):
        self.model = ChatOllama(base_url=os.getenv['OLLAMA_URL', "http://ollamahost:11434"]
                                , model="mistral"
                                , num_thread=os.getenv('NUM_THREADS')
                                )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1024, chunk_overlap=100
        )
        self.prompt = PromptTemplate.from_template(
            """
            <s> [INST] You are an assistant for question-answering tasks. 
            Answer the question with poems in the style of Shakespeare. 
            If you don't know the answer, just say: "To be, or not to be,
            that is the question". Use not more than two verses and keep 
            the answer concise. [/INST] </s> 
            [INST] Question: {question} 
            Answer: [/INST]
            """
        )
        self.chain = (
            {"question": RunnablePassthrough()}
            | self.prompt
            | self.model
            | StrOutputParser()
        )

    def ask(self, query: str):
        return self.chain.invoke(query)
