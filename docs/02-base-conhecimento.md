# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `optimus_indicadores_macro.csv` | CSV | 12 indicadores macroeconômicos (VIX, DXY, CPI, Fed Rate, Brent, etc.) com direção e impacto em cada classe de ativo |
| `optimus_historico_eventos.csv` | CSV |  10 eventos geopolíticos reais (2014–2024) com variação percentual por setor e impacto no S&P 500 |
| `optimus_setores.json` | JSON |  setores mapeados (Defesa, Energia, Tecnologia, Saúde, Agronegócio, Ouro/Refúgio, Infraestrutura) com indicadores positivos/negativos, exemplos de ativos e correlação com conflitos |
| `optimus_conflitos.json` | JSON | 6 tipos de conflito (guerra convencional, regional, comercial, pandemia, bloqueio marítimo, instabilidade política) com matriz de impacto esperado por setor |
| `optimus_perfis_investidor.json` | JSON | perfil com alocações-base e alocações táticas específicas para períodos de conflito |
| `optimus_config_assistente.json` | JSON | Fluxo de raciocínio em 5 etapas com prompts sugeridos para cada fase, fontes recomendadas e palavras-chave para monitoramento de notícias |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Modifiquei todos os arquivos para melhor atender ao meu modelo

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Todos os dados vão no system prompt, é mais simples e fácil de implementar

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
    contexto = f"""
        CLIENTE: {perfil['usuario']['nome']}, {perfil['usuario']['idade']} anos e tem o objetivo {perfil['usuario']['objetivo']}
        SETORES: Tem interesse em {perfil['preferencias']['setores_de_interesse']} e evita {perfil['preferencias']['setores_a_evitar']} 

        INDICADORES:
        {indicador[colunas_uteis].to_string(index=False)}

        CONFIG_RESPOSTA:
        {json.dumps(config['fluxo_de_analise'], ensure_ascii=False, indent=2)}    
    """
  ...
```
