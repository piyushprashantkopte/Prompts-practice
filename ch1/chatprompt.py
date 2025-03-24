from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate,PromptTemplate
from groq import Groq
from decouple import config
SECRET_KEY = config('GROQ_API_KEY')
chat = ChatGroq(temperature=0, groq_api_key=SECRET_KEY, model_name="llama-3.3-70b-versatile")



#chatPrompt = ChatPromptTemplate([
#    ("system,"
#    "You are a helpful assistant that translate {input_language} to {output_language}"),
#    ("human","{text}")
#])
#print("Chat promt: ", chatPrompt)
#formattedChatprompt = chatPrompt.format_messages(
#    input_language ="English",
#    output_language ="French",
#    text = "I am learning"
#)
#print("formated chat prompt: ", formattedChatprompt)
#chain = chatPrompt | chat
#response = chain.invoke(formattedChatprompt)
#print("Response content: ", response.content)

prompt = ChatPromptTemplate.from_messages([("human", "Write a Limerick about {topic}")])
chain = prompt | chat
response = chain.invoke({"topic": "The Moon"})

print("Response content : ", response.content)