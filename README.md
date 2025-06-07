

<h1 align="center">
  🐝
  Bee - Desafio Técnico
  <img src="https://cdn3.emoji.gg/emojis/1887_python.png" width="30px">
</h1>
<div style="display: flex; align-items: center;">
    <img src="https://i.imgur.com/B90tHjI.png" style="align-self: flex-start;" />
</div>

<center>
Esse projeto partiu de um desafio técnico disponível no repositório original. 
</center>
</div>

---

## ✨🌼 Desafio Técnico - Scraping de Dados do IMDB 

O objetivo era buscar dados dos serviços do **IMDB**, utilizando suas APIs ou técnicas de raspagem de dados para buscar as informações dos filmes disponíveis para o público. 

Nesse repositório, implementei uma API em Django que possui dois endpoints para informações: `api/search`, que utiliza a própria API do IMDB e `api/movie`, que faz a raspagem de dados da página do filme e persiste eles no Banco. 

### Implementação ☁️✩ ₊

As principais funções solicitadas foram implementadas utilizando as seguintes tecnologias:

- **Front-end**: HTML, CSS (Tailwind), Javascript (Vanilla) 🥞
- **Back-end**: Django, SQLite 🧇
- **Infra**: Docker, Celery e Redis (Agendamento) 🧸

|Método|Endpoint| Recurso |
|--|--|--|
|`GET`| `/` | Página inicial, hospedando o `front-end` |
|`GET`| `/api/search?q=` | Busca rápida pelo nome da obra [`API IMDB`]  |
|`POST`| `/api/movie` | Busca avançada a obra e pesiste [`IMDB Scraping`]  |
|`GET`| `/api/df` | Gera um csv contendo todos os filmes do Banco [`Pandas`]  |
|`GET`| `/api/all` | Retorna todos os filmes do Banco  |
> A porta padrão exposta pelo Docker é a 8000, então você deve conseguir acessar o serviço em `http://localhost:8000`. 

### Mínimo Entregável  ✅

 - [X] Buscar dados de forma automatizada (Interface Web)
- [X]   Padronizar os retornos de forma estruturada (`JSON` e `CSV`)
- [X]  Sistema de logs de para acompanhamento da execução (Django Logger)
- [X]  Prova de Consulta

### Extras ✅

- [X]   Armazenamento dos resultados em um banco relacional (SQLite)
- [X]   Fazer um dataframe que possibilite visualizar os resultados via pandas (Endpoint Implementado)
- [X]  Trazer resultados de forma dinamica sem fixar caminhos no  `xpath`
- [X]  Dockerizar a aplicação 
- [X]  Conseguir agendar uma execução para um dia e horário. (Celery e Redis)


## O que testar? 🍯𓆪☼

Utilizando a interface web, pesquise por obras e clique no botão de adicionar (cruz com `hover` verde) para acrescentar esse item a sua página inicial e no banco de dados. 

A cada trinta segundos, e todo dia às dez horas, o Celery vai rodar a seguinte task: 

```python
# bee/apps/movies/tasks.py
@shared_task
def make_api_request():
    response = requests.get('http://host.docker.internal:8000/api/df')
    logger.info(f"Requisicao de 30 segundos: {response.status_code}")
    return

@shared_task
def daily_api_request():
    response = requests.post('http://host.docker.internal:8000/api/df')
    logger.info(f"Requisicao Diaria: {response.status_code}")
    return
```

Você ainda pode editar o arquivo de configuração do Django, no módulo do Celery, para alterar a frequência que essas tasks são chamadas (e também acrescentar novas).

```python
# bee/server/settings.py
CELERY_BEAT_SCHEDULE = {
    'frequent-api-request': {
        'task': 'apps.movies.tasks.make_api_request',
        'schedule': 30.0,  # a cada 30 segundos
    },
    'daily-api-request': {
        'task': 'movies.tasks.daily_api_request',
        'schedule': crontab(hour=10, minute=0),  # todo dia as 10
    },
}

```

<div style="display: flex;, align-items: center;">
	<img src="https://i0.wp.com/media3.giphy.com/media/eHQ5BsgBIBIGI/giphy.gif" />
</div>

## 📦 Instalação

###  ✿𓍢𓄹༶ Setup

É necessário ter o Python, o Git e a Docker Engine instalados na sua máquina. 
- Clone meu repositório:
 ```bash
git clone https://github.com/vergonha/bee
```
<img align="right" src="https://i.imgur.com/P8PJKTD.png" />

 - Inicie o Docker: 
```bash
cd bee

docker compose build 
docker compose up 
```







