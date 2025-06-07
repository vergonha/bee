from celery import shared_task
import requests
import logging

logger = logging.getLogger(__name__)

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
