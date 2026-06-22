import requests
import os
from dotenv import load_dotenv
import database 

load_dotenv()
minha_chave = os.getenv("API_KEY")

competicao = "PL"
url = f"https://api.football-data.org/v4/competitions/{competicao}/matches"

headers = {
    "X-Auth-Token": minha_chave
}

filtros = {
    "status": "FINISHED",
    "season": "2025"
}

resposta = requests.get(url, headers=headers, params=filtros)

if resposta.status_code == 200:
    dados = resposta.json()
    jogos = dados.get('matches', [])
    
    print(f"Encontrados {len(jogos)} jogos na API.")
    
    if len(jogos) > 0:
        database.criar_base_dados() 
        database.guardar_jogos(jogos)
else:
    print(f"Erro: {resposta.status_code}")