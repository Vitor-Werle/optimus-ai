import json
import pandas as pd
import requests
import streamlit as st

# config
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = 'llama3.2:1b'
# load data
perfil = json.load(open('./data/optimus_perfil_investidor.json'))
config = json.load(open('./data/optimus_config_assistente.json'))
conflitos = json.load(open('./data/optimus_conflitos.json'))
setores = json.load(open('./data/optimus_setores.json', encoding='utf-8'))
eventos = pd.read_csv('./data/optimus_historico_eventos.csv')
indicador = pd.read_csv('./data/optimus_indicadores_macro.csv')
colunas_uteis = ['indicador', 'direcao', 'impacto_acoes_growth', 'impacto_ouro', 'impacto_commodities']

# mount data
contexto = f"""
    CLIENTE: {perfil['usuario']['nome']}, {perfil['usuario']['idade']} anos
    OBJETIVO: {perfil['usuario']['objetivo']}
    HORIZONTE: {perfil['usuario']['horizonte']}
    EXPERIENCIA: {perfil['usuario']['experiencia']}

    PREFERENCIAS:
    - Mercados aceitos: {perfil['preferencias']['mercados']}
    - Setores de interesse: {perfil['preferencias']['setores_de_interesse']}
    - Setores a evitar: {perfil['preferencias']['setores_a_evitar']}
    - Aceita exposição cambial: {perfil['preferencias']['exposicao_cambial_aceita']}

    ALOCAÇÃO ATUAL:
    {json.dumps(perfil['alocacao_atual'], ensure_ascii=False, indent=2)}

    COMPORTAMENTO EM CRISE:
    - Tolerância máxima de queda: {perfil['comportamento_em_crise']['tolerancia_queda_maxima']}
    - Reação típica: {perfil['comportamento_em_crise']['reacao_tipica']}
    - Revisão: {perfil['comportamento_em_crise']['frequencia_revisao']}

    INDICADORES:
    {indicador[colunas_uteis].to_string(index=False)}

    CONFIG_RESPOSTA:
    {json.dumps(config['fluxo_de_analise'], ensure_ascii=False, indent=2)}
"""

# system prompt
SYSTEM_PROMPT = """ Você é o Optimus, um analísta financeiro com base nas notícias e conflitos fornecidos pelo usuário. Seu objetivo é recomandar as melhores áreas para investir com base na notícia fornecida pelo usuário e consulta aos dados fornecidos.

    REGRAS:
    1. Sempre baseie suas respostas nos dados fornecidos
    2. Nunca invente informações financeiras
    3. Se não souber algo, admita e ofereça alternativas
    4. Não reponde perguntas que não estejam relacionadas a investimentos ou finanças
        Ex.: Qual é a capital da França? -> Desculpe, não posso responder a essa pergunta. Posso ajudar com algo relacionado a investimentos ou finanças?
            Qual é a previsão do tempo para amanhã? -> Desculpe, não posso responder a essa pergunta. Posso ajudar com algo relacionado a investimentos ou finanças?
    5. Deixe a advertência de risco como o último parágrafo da resposta
"""

# call ollama
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json().get('response')


# interface
st.title("Welcome, I'm Optimus")

if pergunta := st.chat_input("Como essa notícia impacta o mundo"):
    st.chat_message("user").write(pergunta)
    with st.spinner("....."):
        st.chat_message("assistente").write(perguntar(pergunta))


