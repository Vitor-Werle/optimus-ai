# Passo a Passo de Execução

## Setup do Ollama

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar modelo leve
ollama3.2:1b

# 3. Testar se funciona
ollama run llama3.2:1b "Olá!"
```

## Código completo

Todo o código fonte está no arquivo `app.py`

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit)
```

## Exemplo de requirements.txt

```
streamlit
pandas
requests
```

## Como Rodar

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Garantir que o Ollama está rodando:
ollama list 
ollama serve

# 3. Rodar a aplicação
streamlit run ./src/app.py
```
