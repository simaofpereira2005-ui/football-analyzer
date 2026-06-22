import requests
import os
from dotenv import load_dotenv

load_dotenv()

minha_chave = os.getenv("API_KEY")

url = "https://api.football-data.org/v4/competitions/"

# 3. Usar a variável no cabeçalho em vez da string hardcoded
headers = {
    "X-Auth-Token": minha_chave
}

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    print("Sucesso! A API validou a chave lida a partir do cofre.")
else:
    print(f"Erro: {resposta.status_code}")