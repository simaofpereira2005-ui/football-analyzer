import sqlite3

def criar_base_dados():

    conexao = sqlite3.connect('football_data.db')

    cursor = conexao.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY,
        equipa_casa TEXT NOT NULL,
        equipa_fora TEXT NOT NULL,
        data_jogo TEXT NOT NULL,
        estado TEXT NOT NULL
    )
    """
    
    cursor.execute(query)
    conexao.commit()
    conexao.close()

def guardar_jogos(lista_jogos):
    conexao = sqlite3.connect('football_data.db')
    cursor = conexao.cursor()
    
    query = """
    INSERT OR REPLACE INTO jogos (id, equipa_casa, equipa_fora, data_jogo, estado)
    VALUES (?, ?, ?, ?, ?)
    """
    
    dados_formatados = []
    for jogo in lista_jogos:
        dados_formatados.append((
            jogo['id'],
            jogo['homeTeam']['name'],
            jogo['awayTeam']['name'],
            jogo['utcDate'],
            jogo['status']
        ))
    
    cursor.executemany(query, dados_formatados)
    conexao.commit()
    conexao.close()
    
    print(f"> {len(dados_formatados)} jogos guardados/atualizados na base de dados SQLite!")

if __name__ == "__main__":
    criar_base_dados()