import streamlit as st
import stats
import predict

st.set_page_config(page_title="World Cup Predictor", page_icon="🏆", layout="centered")

st.markdown("<h1 style='text-align: center;'>🏆 Previsões do Mundial 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Powered by Poisson Distribution & Data Science</p>", unsafe_allow_html=True)
st.divider()

# Carregar Dados
dados_stats = stats.obter_estatisticas_completas()
lista_equipas = list(dados_stats['equipas'].keys())
lista_equipas.sort()

st.subheader("📋 Seleciona o Confronto")
col1, col2 = st.columns(2)

with col1:
    equipa_casa = st.selectbox("🏠 Equipa 1 (Casa)", lista_equipas)
with col2:
    equipa_fora = st.selectbox("✈️ Equipa 2 (Fora)", lista_equipas, index=1 if len(lista_equipas)>1 else 0)

st.write("") 
botao_calcular = st.button("🔮 Gerar Previsão Estatística", use_container_width=True, type="primary")

if botao_calcular:
    if equipa_casa == equipa_fora:
        st.error("⚠️ As equipas têm de ser diferentes!")
    else:
        lambda_A, lambda_B = predict.calcular_lambda(equipa_casa, equipa_fora, dados_stats)
        
        if lambda_A is not None and lambda_B is not None:
            vit_casa, empate, vit_fora = predict.calcular_probabilidades_jogo(lambda_A, lambda_B)
            aposta = predict.sugestao_aposta(vit_casa, empate, vit_fora, lambda_A, lambda_B)
            
            st.divider()
            
            st.success(f"**Aposta Sugerida pelo Algoritmo:** {aposta}")
            
            st.subheader("📊 Probabilidades do Jogo")
            res_col1, res_col2, res_col3 = st.columns(3)
            
            res_col1.metric(label=f"Vitória {equipa_casa}", value=f"{vit_casa:.1f}%")
            res_col2.metric(label="Empate", value=f"{empate:.1f}%")
            res_col3.metric(label=f"Vitória {equipa_fora}", value=f"{vit_fora:.1f}%")
            
            with st.expander("🔍 Ver Estatísticas Avançadas (xG)"):
                st.write(f"O **Expected Goals (xG)** mede a qualidade das oportunidades de golo criadas. Baseado na performance deste Mundial até agora:")
                st.info(f"**{equipa_casa}:** Vai marcar em média **{lambda_A:.2f}** golos.")
                st.info(f"**{equipa_fora}:** Vai marcar em média **{lambda_B:.2f}** golos.")
        else:
            st.warning("Ainda não existem dados suficientes para estas equipas neste Mundial. Elas precisam de jogar mais partidas!")