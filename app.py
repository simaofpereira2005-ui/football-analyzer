import streamlit as st
import stats
import predict

st.set_page_config(page_title="Football Match Analyzer", page_icon="⚽", layout="centered")

st.title("⚽ Football Match Analyzer")
st.write("Previsão de resultados da Premier League baseada na Distribuição de Poisson.")

dados_stats = stats.obter_estatisticas_completas()

lista_equipas = list(dados_stats['equipas'].keys())
lista_equipas.sort()

col1, col2 = st.columns(2)

with col1:
    equipa_casa = st.selectbox("Equipa da Casa", lista_equipas)

with col2:
    equipa_fora = st.selectbox("Equipa de Fora", lista_equipas, index=1)


if st.button("Calcular Probabilidades 📊"):
    
    if equipa_casa == equipa_fora:
        st.warning("⚠️ A equipa da casa não pode ser a mesma que a equipa de fora!")
    else:
        lambda_A, lambda_B = predict.calcular_lambda(equipa_casa, equipa_fora, dados_stats)
        
        if lambda_A and lambda_B:
            vit_casa, empate, vit_fora = predict.calcular_probabilidades_jogo(lambda_A, lambda_B)
            
            st.markdown("---")
            st.subheader("Resultados da Previsão")
            
            res_col1, res_col2, res_col3 = st.columns(3)
            
            with res_col1:
                st.metric(label=f"Vitória {equipa_casa}", value=f"{vit_casa:.1f}%")
            with res_col2:
                st.metric(label="Empate", value=f"{empate:.1f}%")
            with res_col3:
                st.metric(label=f"Vitória {equipa_fora}", value=f"{vit_fora:.1f}%")
                
            # Informação extra para os geeks de estatística
            st.caption(f"Expectativa de Golos (xG): {equipa_casa} **{lambda_A:.2f}** - **{lambda_B:.2f}** {equipa_fora}")
        else:
            st.error("Não foi possível calcular as probabilidades. Faltam dados.")