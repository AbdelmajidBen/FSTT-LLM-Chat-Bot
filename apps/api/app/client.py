from langserve import RemoteRunnable
import requests

""" model = RemoteRunnable("http://API:8000/rag")

response = model.invoke("Qui est le doyen de la fst tanger?")

print(response) """

url = "http://API:8000/rag/stream"

payload = { "input": { "text": "Qui est le doyen de la fst tanger?" } }

response = requests.post(url, json=payload)