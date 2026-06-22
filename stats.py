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
    # Usamos um truque matemático (0.001) para evitar que a divisão por zero parta a nossa matemática (Poisson)
    estatisticas["media_liga_casa"] = liga["avg_casa"] if liga["avg_casa"] else 0.001
    estatisticas["media_liga_fora"] = liga["avg_fora"] if liga["avg_fora"] else 0.001
    
    cursor.execute("""
        SELECT equipa_casa, AVG(golos_casa) as golos_marcados, AVG(golos_fora) as golos_sofridos
        FROM jogos WHERE estado = 'FINISHED' GROUP BY equipa_casa
    """)
    for linha in cursor.fetchall():
        equipa = linha["equipa_casa"]
        if equipa not in estatisticas["equipas"]:
            estatisticas["equipas"][equipa] = {"casa_marcados": 0, "casa_sofridos": 0, "fora_marcados": 0, "fora_sofridos": 0}
            
        estatisticas["equipas"][equipa]["casa_marcados"] = linha["golos_marcados"] or 0
        estatisticas["equipas"][equipa]["casa_sofridos"] = linha["golos_sofridos"] or 0

    cursor.execute("""
        SELECT equipa_fora, AVG(golos_fora) as golos_marcados, AVG(golos_casa) as golos_sofridos
        FROM jogos WHERE estado = 'FINISHED' GROUP BY equipa_fora
    """)
    for linha in cursor.fetchall():
        equipa = linha["equipa_fora"]
        if equipa not in estatisticas["equipas"]:
            estatisticas["equipas"][equipa] = {"casa_marcados": 0, "casa_sofridos": 0, "fora_marcados": 0, "fora_sofridos": 0}
            
        estatisticas["equipas"][equipa]["fora_marcados"] = linha["golos_marcados"] or 0
        estatisticas["equipas"][equipa]["fora_sofridos"] = linha["golos_sofridos"] or 0
        
    conexao.close()
    return estatisticas

if __name__ == "__main__":
    dados = obter_estatisticas_completas()
    print("Média Casa Torneio:", dados['media_liga_casa'])
    print(f"Total de equipas carregadas com sucesso: {len(dados['equipas'])}")