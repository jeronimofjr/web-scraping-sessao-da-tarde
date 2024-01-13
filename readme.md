## Web Scraping - Sessão da Tarde

<img src="./sessao-da-tarde.jpg" height="390" width="700">

### Descrição do Projeto

Este projeto tem como objetivo realizar web scraping para obter dados de transmissão dos filmes exibidos na "Sessão da Tarde". A "Sessão da Tarde" é uma programação de filmes exibida tradicionalmente nas tardes da televisão brasileira, trazendo clássicos e filmes populares para o público.

  
O web scraping será utilizado para extrair informações como título do filme, data de exibição e qualquer outra informação relevante disponível.

  
### Principais Ferramentas Utilizadas

**Python:** A linguagem de programação principal para a implementação do web scraping.

**Beautiful Soup:** Biblioteca Python para extrair dados de arquivos HTML e XML.

**Pandas:** Biblioteca Python para manipulação e transformação de dados.


### Caso queira replicar, segue as instruções de uso

**Donwload do projeto**
<!--MAIN_BEGIN-->
```bash

git clone https://github.com/jeronimofjr/web-scraping-sessao-da-tarde 
```
<!--MAIN_END-->

**Mudar para a pasta do projeto**
<!--MAIN_BEGIN-->
```bash
cd web-scraping-sessao-da-tarde/
```
<!--MAIN_END-->

**Configuração do Ambiente:**

Instale as dependências necessárias executando os seguintes comandos no terminal (linux): 

<!--MAIN_BEGIN-->
```bash
# criação do ambiente virtual [recomendado]
python3 -m venv venv

# ativação do ambiente virtual
source venv/bin/activate

# instalação das dependências
pip install -r requirements.txt
```
<!--MAIN_END-->


**Execução do script:**

Execute o script main.py para iniciar o processo de web scraping.

<!--MAIN_BEGIN-->
```bash
python3 main.py
```
<!--MAIN_END-->

Os dados extraídos serão armazenados em um arquivo CSV chamado ```sessao_da_tarde.csv``` na pasta **data/** para fácil visualização e manipulação.


### Estrutura do Projeto

* **app/**: Pasta com o script principal responsável pelo web scraping.
* **data/**: Pasta onde o arquivo csv gerado a partir do web scraping será salvo.
* **utils/**: Pasta com o script de processamento de texto usado na EDA.
* **eda.ipynb**: Notebook com a EDA dos dados obtidos.
* **requirements.txt**: Lista de dependências do projeto.
