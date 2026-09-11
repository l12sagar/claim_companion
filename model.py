from langchain_openai import ChatOpenAI
import httpx

client = httpx.Client(verify=False)

llm = ChatOpenAI(
    base_url="https://genailab.tcs.in",
    model="genailab-maas-Opus-4.6",
    api_key="sk-VHold_zIX3VuaK-xkAc8rw",
    http_client=client
)

response = llm.invoke("Hi")

print(response.content)
