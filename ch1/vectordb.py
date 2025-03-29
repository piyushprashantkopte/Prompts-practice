from groq import Groq
from langchain_groq import GroqEmbeddings
from decouple import config
SECRET_KEY = config('GROQ_API_KEY')



embeddings_model = GroqEmbeddings(api_key=SECRET_KEY)

embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
print(len(embeddings), len(embeddings[0]))