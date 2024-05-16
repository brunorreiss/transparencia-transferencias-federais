# Consulta Portal Transparência - evidenciando os valores efetivamente arrecadados das principais transferências realizadas pelo governo federal ao município. :robot:

## Introdução
Consulta Pública ao Portal da Transparência de Fortaleza - principais transferencias federais


## Respostas da API

| HTTP CODE | `code` | Descrição |
| --------- | ---------- | --------- |
| `200` | 0 | Sucesso |
| `422` | 7 | Não foi possível processar |
| `502` | 5 | Bad Gateway |
| `512` | 4 | Erro ao executar parse da pagina |

## URL

* https://portaltransparencia.fortaleza.ce.gov.br/#/receitas/federais


### Para executar o bot manualmente, siga os passos abaixo:

1. Baixe o repositorio:
```
git clone https://github.com/brunorreiss/transparencia-transferencias-federais.git
```
2. Mude de diretorio:
```
cd transparencia-tranferencias-federais
```
3. Instale as bibliotecas requeridas:
```
pip install -r requirements.txt
```
4. Execute o bot:
```
uvicorn server:app --host 0.0.0.0 
```
5. Abra o navegador a acesse a URL: http://localhost:8000/


| ENV VAR | Descrição |
| ------- | ---------- |
| `BOT_NAME` | Nome do bot. Util caso houver mais de um container do mesmo bot rodando. (*default: transparencia-receita-fortaleza*) |
| `LOG_LEVEL` | Nivel de log. Valores aceitos: (DEBUG, INFO, WARNING, ERROR - *default: INFO*) |
| `TIMEOUT` | Total de **segundos** que o bot espera antes de encerrar a conexao com o site. (*default: 180*) |