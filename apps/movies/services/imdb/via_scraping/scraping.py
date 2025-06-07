import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup


import logging
logger = logging.getLogger(__name__)

class ImdbScraping():
    @staticmethod
    def get_movie(movie_id):
        logger.info("Searching movie: " + movie_id)
        headers = {
            # Pode mandar tudo em inglês. Se esse header for em português, a descrição continua em inglês do mesmo jeito kkkk 
            "accept-language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
        }
        response = requests.get("https://www.imdb.com/title/" + movie_id, headers=headers)
        if response.status_code != 200:
            return ""

        soup = BeautifulSoup(response.content, 'html.parser')

        description = soup.find(attrs={"role": "presentation", "data-testid": "plot-xs_to_m"}).get_text(strip=True)
        title = soup.find(attrs={"class": "hero__primary-text", "data-testid": "hero__primary-text"}).get_text(strip=True)
        cover = soup.find(attrs={"class": "ipc-image"})['src']
        
        # Eu só quero o rating. Ex: Por padrão, essa classe tem "7.7/10". Quero só o "7.7"
        rating = soup.find(attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"}).get_text(strip=True).split("/")[0]

        # Esqueci de botar o diretor no banco de dados
        # Mas tá bom, vai? Fica aí.
        directors = [_.get_text() for _ in soup.find('li', {'data-testid': 'title-pc-principal-credit'}).find('div').find_all("li")]

        release_date = datetime.strptime(
            soup.find('li', {'data-testid': 'title-details-releasedate'}).find('a', class_='ipc-metadata-list-item__list-content-item').get_text(strip=True).split(' (')[0], 
            '%B %d, %Y'
        ).strftime('%Y-%m-%d')


        date_tag = soup.find('a', class_='ipc-metadata-list-item__list-content-item')

        data = { "description": description, "name": title, "cover": cover, "rating": rating, "release_date": release_date }
        logger.info(json.dumps(data))
        return data
    