import math
import stats 

def calcular_lambda(equipa_casa, equipa_fora, dados):
    """Calcula o Lambda (xG) para ambas as equipas usando o modelo de Forças."""
    
    media_liga_casa = dados['media_liga_casa']
    media_liga_fora = dados['media_liga_fora']
    
    stats_casa = dados['equipas'].get(equipa_casa)
    stats_fora = dados['equipas'].get(equipa_fora)
    
    if stats_casa is None or stats_fora is None:
        return None, None

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

def calcular_probabilidades_jogo(lambda_casa, lambda_fora, max_golos=5):
    """Calcula as % de Vitória, Empate e Derrota somando a matriz de resultados."""
    prob_vitoria_casa = 0.0
    prob_empate = 0.0
    prob_vitoria_fora = 0.0
    
    for golos_casa in range(max_golos + 1):
        for golos_fora in range(max_golos + 1):
            
            prob_c = poisson_prob(lambda_casa, golos_casa)
            prob_f = poisson_prob(lambda_fora, golos_fora)
            
            prob_resultado_exato = prob_c * prob_f
            
            if golos_casa > golos_fora:
                prob_vitoria_casa += prob_resultado_exato
            elif golos_casa == golos_fora:
                prob_empate += prob_resultado_exato
            else:
                prob_vitoria_fora += prob_resultado_exato
                
    return prob_vitoria_casa * 100, prob_empate * 100, prob_vitoria_fora * 100

def sugestao_aposta(vit_casa, empate, vit_fora, lambda_casa, lambda_fora):
    """Gera uma sugestão de aposta baseada nas probabilidades e xG."""
    xg_total = lambda_casa + lambda_fora
    
    if vit_casa > 60.0:
        return "🔥 Vitória da Equipa da Casa (Confiança Alta)"
    elif vit_fora > 60.0:
        return "🔥 Vitória da Equipa de Fora (Confiança Alta)"
    
    elif xg_total > 2.8:
        return "⚽ Over 2.5 (Mais de 2.5 golos no jogo)"
    elif xg_total < 1.5:
        return "🛡️ Under 2.5 (Menos de 2.5 golos no jogo)"
    
    elif vit_casa > 45.0:
        return "⚖️ Empate Anula: Equipa da Casa (DNB)"
    elif vit_fora > 45.0:
        return "⚖️ Empate Anula: Equipa de Fora (DNB)"
    
    else:
        return "⚠️ Jogo Imprevisível (Evitar Apostar no Vencedor)"
    
if __name__ == "__main__":
    dados_stats = stats.obter_estatisticas_completas()
    
    equipa_A = "Arsenal FC"
    equipa_B = "Manchester United FC"
    
    lambda_A, lambda_B = calcular_lambda(equipa_A, equipa_B, dados_stats)
    
    if lambda_A and lambda_B:
        vit_casa, empate, vit_fora = calcular_probabilidades_jogo(lambda_A, lambda_B)
        
        print(f"--- PREVISÃO DE JOGO: {equipa_A} vs {equipa_B} ---")
        print(f"Vitória {equipa_A}: {vit_casa:.1f}%")
        print(f"Empate: {empate:.1f}%")
        print(f"Vitória {equipa_B}: {vit_fora:.1f}%")
    else:
        print("Dados insuficientes para estas equipas.")