from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import defaultdict
import re


url = 'https://sbt.fandom.com/pt/wiki/Lista_de_filmes_exibidos_na_Sess%C3%A3o_da_Tarde'

class Scraping:
  def __init__(self) -> None:
    self.soup_object_scraping = self.get_object_scraping()
    self.data = defaultdict(list)
    self.sessao_da_tarde_df = None
    

  def get_object_scraping(self):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    s = soup.find('div', class_="mw-parser-output")
    return s

  def filter_data_scraping(self, resp, ano_tag, mes_tag) -> None:
    self.data["titulo"].append(resp[1].strip())
    self.data["ano"].append(re.findall(r'\d+', ano_tag.text)[0] )
    self.data["mes"].append(mes_tag.text.replace('\u200b', ''))
    self.data["mes"][-1] = re.findall(r'[a-zA-Z]+', self.data["mes"][-1])[0]
    self.data["dia"].append(resp[0].strip().split('/')[0])

  def scraping_data(self) -> None:
    for ano_tag in self.soup_object_scraping.find_all('h2')[2:37]:
      meses_tag = ano_tag.find_next_siblings('h3', limit=12)
      for mes_tag in meses_tag:
        ul_tag = mes_tag.find_next('ul')
        for content in ul_tag.find_all('li'):
          resp = content.text.split('-', maxsplit=1)
          if len(resp) == 2:
            self.filter_data_scraping(resp, ano_tag, mes_tag)
    
    
  def processing(self) -> None:
    df = pd.DataFrame(self.data)
    df = df[~df["titulo"].str.lower().str.contains("não houve exibição|Festival de Férias")]
    df.loc[:, "titulo"] = df['titulo'].apply(lambda x: re.sub(r'\(.*', '', x).strip())
    df.loc[:, "titulo"] = df['titulo'].apply(lambda x: x.split('|')[0] if '|' in x else x)
    df.loc[:, "mes"] = df['mes'].apply(lambda x:  'Março' if x == 'Mar' else x)
    df.drop(df[df["titulo"] == ''].index, inplace=True)
   
    self.sessao_da_tarde_df = df 
  
  def save_data(self) -> None:
    self.sessao_da_tarde_df.to_csv("./data/sessao_da_tarde.csv", index=False)

