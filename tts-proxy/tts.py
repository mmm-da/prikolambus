import logging
import requests
from os import environ

logger = logging.getLogger("tts-api")

def generate_file(text):
    logger.info("Generating audio file")
    
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': 'Api-Key ' + environ.get('TTS_API_SECRET_KEY'),
    }
    data = {
        'text': text,
        'voice': 'filipp',
        'speed': '1.4',
        'format': 'oggopus',
        'lang': 'ru-RU'
    }

    result_obj = b''

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

        for chunk in resp.iter_content(chunk_size=None):
            result_obj += chunk

    return result_obj