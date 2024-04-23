import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

# etapa 1 - criando sistema
#TITULO
st.write("# Análise de Satisfação do Cliente")
#INPUT
user_i = st.text_input("Digite sua satisfação : ")

# etapa 2 - maquina preditiva e pln
sentimento = SentimentIntensityAnalyzer()
score = sentimento.polarity_scores(user_i)

# visualização otimizadaa
if score == 0 :
    st.write(score)
    st.write("## Análise neutra.")
elif score["neg"] != 0:
    st.write(score)
    st.write("## Análise negativa.")
elif score["pos"] != 0:
    st.write(score)
    st.write("## Análise positiva.")    
    
# etapa 3 - uso do sistema
# streamlit run analise.py
