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
    CLIENTE: {perfil['usuario']['nome']}, {perfil['usuario']['idade']} anos e tem o objetivo {perfil['usuario']['objetivo']}
    SETORES: Tem interesse em {perfil['preferencias']['setores_de_interesse']} e evita {perfil['preferencias']['setores_a_evitar']} 

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
4. Não recomende ativos específicos (PETR4, WEGE3, VALE3, etc), apenas setores que tendem a se beneficiar com os eventos fornecidos
5. Não responda perguntas fora do escopo
"""

# call ollama
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']


# interface
st.title("Welcome, I'm Optimus")

if pergunta := st.chat_input("Como o mundo impacta vai impactar suas finanças hoje?"):
    st.chat_message("user").write(pergunta)
    with st.spinner("....."):
        st.chat_message("assistente").write(perguntar(pergunta))
