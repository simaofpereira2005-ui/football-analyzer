import requests
import os
from dotenv import load_dotenv

load_dotenv()
minha_chave = os.getenv("API_KEY")

# 1. Definimos a Liga (PL = Premier League, PPL = Primeira Liga Portuguesa)
competicao = "PL"
url = f"https://api.football-data.org/v4/competitions/{competicao}/matches"

headers = {
    "X-Auth-Token": minha_chave
}

# 2. Definimos os Parâmetros de Pesquisa (Filtros)
# A documentação da API diz-nos que 'SCHEDULED' são os jogos futuros
filtros = {
    "status": "SCHEDULED"
}

# 3. Fazemos o pedido passando o URL, o Cartão VIP e os Filtros
resposta = requests.get(url, headers=headers, params=filtros)

if resposta.status_code == 200:
    dados = resposta.json()
    # Extraímos a lista de jogos do dicionário
    jogos = dados.get('matches', [])
    
    print(f"Encontrados {len(jogos)} jogos agendados para a competição {competicao}.")
    
    # Se houver jogos futuros, vamos ver o primeiro!
    if len(jogos) > 0:
        proximo_jogo = jogos[0]
        equipa_casa = proximo_jogo['homeTeam']['name']
        equipa_fora = proximo_jogo['awayTeam']['name']
        data_jogo = proximo_jogo['utcDate']
        
        print(f"\nO próximo jogo em destaque é:")
        print(f"{equipa_casa} vs {equipa_fora} no dia {data_jogo}")
else:
    print(f"Erro: {resposta.status_code}")