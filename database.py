import sqlite3

def criar_base_dados():
    conexao = sqlite3.connect('football_data.db')
    cursor = conexao.cursor()
    
    query = """
    CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY,
        equipa_casa TEXT NOT NULL,
        equipa_fora TEXT NOT NULL,
        golos_casa INTEGER,
        golos_fora INTEGER,
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
    INSERT OR REPLACE INTO jogos 
    (id, equipa_casa, equipa_fora, golos_casa, golos_fora, data_jogo, estado)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    
    dados_formatados = []
    for jogo in lista_jogos:
        resultado = jogo.get('score', {}).get('fullTime', {})
        golos_c = resultado.get('home')
        golos_f = resultado.get('away')
        
        dados_formatados.append((
            jogo['id'],
            jogo['homeTeam']['name'],
            jogo['awayTeam']['name'],
            golos_c,
            golos_f,
            jogo['utcDate'],
            jogo['status']
        ))
    
    cursor.executemany(query, dados_formatados)
    conexao.commit()
    conexao.close()
    
    print(f"> {len(dados_formatados)} jogos guardados com os respetivos golos!")

if __name__ == "__main__":
    criar_base_dados()