

import requests
import pandas as pd
from bs4 import BeautifulSoup
def imoveis():
    URL = 'https://www.vivareal.com.br/aluguel/parana/londrina/bairros/centro/apartamento_residencial/'
    page = requests.get(URL)
    imoveis = []

    soup = BeautifulSoup(page.content, "html.parser")

    imovel = soup.find_all("div", class_='js-card-selector')
    print(imovel)

    print("Apartamentos para alugar no Centro de Londrina: ")

    for infos in imovel:
        titulo = infos.find('span', class_="property-card__title js-cardLink js-card-title")
        endereco = infos.find('span', class_="property-card__address")
        detalhes_apartamento = infos.find('ul', class_='property-card__details')
        detalhes_predio = infos.find('ul', class_='property-card__amenities')
        aluguel_mensal= infos.find('p')
        aluguel_condominio =infos.find('strong', class_='js-condo-price')

        print("-----------------------------------------")
        print("")
        print("titulo: ", titulo.text.strip())
        print("endereco: ", endereco.text.strip())
        print("detalhes_apartamento: ", detalhes_apartamento.text.strip())  
      
        if detalhes_predio != None:
            print("detalhes_predio: ", detalhes_predio.text.strip())
        else:
            print("Sem detalhes extras do predio ")
            print("aluguel_mensal: ", aluguel_mensal.text.strip())
        if aluguel_condominio != None:
            print("aluguel_condominio: ", aluguel_condominio.text.strip())
        else:
            print("Sem aluguel do condominio ")

        valores = [titulo.text.strip(), endereco.text.strip(), aluguel_mensal.text.strip()]
        imoveis.append(valores)




        df = pd.DataFrame(imoveis, columns=['Titulo', 'endereco', 'aluguel'])
        df.to_excel('scrapImoveis.xlsx', index=False)
        df.to_csv('scrapImoveis.csv', index=False)
        print(df)
        return df