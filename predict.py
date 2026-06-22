import math
import stats 

def calcular_lambda(equipa_casa, equipa_fora, dados):
    """Calcula o Lambda (xG) para ambas as equipas usando o modelo de Forças."""
    
    media_liga_casa = dados['media_liga_casa']
    media_liga_fora = dados['media_liga_fora']
    
    stats_casa = dados['equipas'].get(equipa_casa)
    stats_fora = dados['equipas'].get(equipa_fora)
    
    if not stats_casa or not stats_fora:
        return None, None # Se não tivermos dados de uma das equipas, abortamos

    forca_ataque_casa = stats_casa['casa_marcados'] / media_liga_casa
    forca_defesa_casa = stats_casa['casa_sofridos'] / media_liga_fora
    
    forca_ataque_fora = stats_fora['fora_marcados'] / media_liga_fora
    forca_defesa_fora = stats_fora['fora_sofridos'] / media_liga_casa
    
    lambda_casa = forca_ataque_casa * forca_defesa_fora * media_liga_casa
    lambda_fora = forca_ataque_fora * forca_defesa_casa * media_liga_fora
    
    return lambda_casa, lambda_fora

def poisson_prob(lambd, golos):
    """Aplica a fórmula matemática da Distribuição de Poisson."""
    return (math.exp(-lambd) * (lambd**golos)) / math.factorial(golos)

if __name__ == "__main__":
    dados_stats = stats.obter_estatisticas_completas()
    
    equipa_A = "Arsenal FC"
    equipa_B = "Manchester United FC"
    
    lambda_A, lambda_B = calcular_lambda(equipa_A, equipa_B, dados_stats)
    
    print(f"--- EXPECTATIVA DE GOLOS (xG) ---")
    print(f"{equipa_A} (Casa): {lambda_A:.2f} golos esperados")
    print(f"{equipa_B} (Fora): {lambda_B:.2f} golos esperados\n")
    
    prob_arsenal_2_golos = poisson_prob(lambda_A, 2) * 100
    print(f"Probabilidade de o {equipa_A} marcar exatamente 2 golos: {prob_arsenal_2_golos:.1f}%")