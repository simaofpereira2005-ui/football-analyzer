import requests
import os
import time
from dotenv import load_dotenv
import database

load_dotenv()
minha_chave = os.getenv("API_KEY")
headers = {"X-Auth-Token": minha_chave}
competicao = "WC"

database.criar_base_dados()

anos_para_analisar = ["2022", "2026"]
total_jogos_guardados = 0

print("A iniciar extração histórica...")

for ano in anos_para_analisar:
    url = f"https://api.football-data.org/v4/competitions/{competicao}/matches"
    filtros = {
        "status": "FINISHED",
        "season": ano
    }
    
    print(f"> A consultar o menu do Mundial {ano}...")
    resposta = requests.get(url, headers=headers, params=filtros)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        jogos = dados.get('matches', [])
        
        if len(jogos) > 0:
            database.guardar_jogos(jogos)
            total_jogos_guardados += len(jogos)
    else:
        print(f"Erro no ano {ano}: {resposta.status_code}")
        
    time.sleep(2) 

print(f"\n✅ Tubagem concluída! {total_jogos_guardados} jogos guardados no teu laboratório.")