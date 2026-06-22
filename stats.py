import sqlite3

def obter_estatisticas_completas():
    conexao = sqlite3.connect('football_data.db')
    conexao.row_factory = sqlite3.Row 
    cursor = conexao.cursor()
    
    estatisticas = {
        "media_liga_casa": 0.0,
        "media_liga_fora": 0.0,
        "equipas": {}
    }
    
    cursor.execute("SELECT AVG(golos_casa) as avg_casa, AVG(golos_fora) as avg_fora FROM jogos WHERE estado = 'FINISHED'")
    liga = cursor.fetchone()
    estatisticas["media_liga_casa"] = liga["avg_casa"]
    estatisticas["media_liga_fora"] = liga["avg_fora"]
    
    cursor.execute("""
        SELECT equipa_casa, AVG(golos_casa) as golos_marcados, AVG(golos_fora) as golos_sofridos
        FROM jogos WHERE estado = 'FINISHED' GROUP BY equipa_casa
    """)
    for linha in cursor.fetchall():
        equipa = linha["equipa_casa"]
        if equipa not in estatisticas["equipas"]:
            estatisticas["equipas"][equipa] = {}
        estatisticas["equipas"][equipa]["casa_marcados"] = linha["golos_marcados"]
        estatisticas["equipas"][equipa]["casa_sofridos"] = linha["golos_sofridos"]

    cursor.execute("""
        SELECT equipa_fora, AVG(golos_fora) as golos_marcados, AVG(golos_casa) as golos_sofridos
        FROM jogos WHERE estado = 'FINISHED' GROUP BY equipa_fora
    """)
    for linha in cursor.fetchall():
        equipa = linha["equipa_fora"]
        estatisticas["equipas"][equipa]["fora_marcados"] = linha["golos_marcados"]
        estatisticas["equipas"][equipa]["fora_sofridos"] = linha["golos_sofridos"]
        
    conexao.close()
    return estatisticas

if __name__ == "__main__":
    dados = obter_estatisticas_completas()
    
    print("--- ESTATÍSTICAS GERAIS DA LIGA ---")
    print(f"Média Golos Casa (Liga): {dados['media_liga_casa']:.2f}")
    print(f"Média Golos Fora (Liga): {dados['media_liga_fora']:.2f}")
    
    print("\n--- ESTATÍSTICAS DO ARSENAL ---")
    print(dados["equipas"]["Arsenal FC"])