🤖 Optimus: Analista Financeiro Geopolítico
O Optimus é um agente de inteligência artificial proativo projetado para ajudar investidores a entenderem o impacto de eventos geopolíticos e notícias macroeconômicas em seus portfólios. Diferente de chatbots reativos, o Optimus cruza notícias em tempo real com uma base histórica de conflitos e indicadores macro para sugerir alocações táticas.

🎯 Caso de Uso
Problema: Investidores têm dificuldade em interpretar como notícias de conflitos ou crises impactam ativos específicos.

Solução: O usuário fornece uma notícia e o Optimus analisa os setores beneficiados ou prejudicados com base em padrões históricos.

Persona: Um analista técnico e sugestivo que prioriza a segurança e a precisão dos dados.

🏗️ Arquitetura do Sistema
O projeto utiliza uma arquitetura local para garantir privacidade e performance:

Interface: Chatbot interativo desenvolvido em Streamlit.

Cérebro (LLM): Ollama executando o modelo llama3.2:1b.

Base de Conhecimento: Arquivos JSON e CSV contendo perfis de investidores, indicadores macro e histórico de eventos.

🛠️ Tecnologias Utilizadas
Linguagem: Python

Bibliotecas: Pandas (manipulação de dados), Streamlit (UI), Requests (comunicação com Ollama)

Orquestração: Ollama

📊 Base de Dados (RAG)
O agente utiliza os seguintes dados para fundamentar suas análises:

optimus_indicadores_macro.csv: 12 indicadores como VIX, DXY e Fed Rate.

optimus_historico_eventos.csv: Histórico de 10 eventos (ex: Invasão à Ucrânia, COVID-19) e seus impactos no S&P 500.

optimus_setores.json: Mapeamento de correlação de setores como Defesa, Energia e Tecnologia com conflitos.

optimus_perfil_investidor.json: Dados específicos do usuário "Vitor" (perfil moderado).

🚀 Como Executar
Prepare o Ollama:

Bash
ollama pull llama3.2:1b
ollama serve
Instale as dependências:

Bash
pip install streamlit pandas requests
Inicie a aplicação:

Bash
streamlit run src/app.py
🛡️ Segurança e Regras de Negócio
Anti-Alucinação: O agente é instruído via System Prompt a basear-se estritamente nos dados fornecidos e admitir quando não possui uma informação.

Restrições: O Optimus recomenda setores e segmentos, mas nunca empresas específicas, para garantir a conformidade ética.

Contexto: Só realiza recomendações personalizadas se o perfil do investidor estiver disponível.

Este projeto foi desenvolvido como parte do desafio de Agentes Inteligentes com IA Generativa.
