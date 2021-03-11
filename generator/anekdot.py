import numpy as np
import torch
import random
import re
import logging
from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,)

logger = logging.getLogger("rugpt3")

# Предзагрузка моделей
logger.info("Start downloading models to cache")
temp = GPT2Tokenizer.from_pretrained('mmm-da/anekdot_funny1_rugpt3Small', cache_dir='/tmp')
temp = GPT2LMHeadModel.from_pretrained('mmm-da/anekdot_funny1_rugpt3Small', cache_dir='/tmp')
temp = GPT2Tokenizer.from_pretrained('mmm-da/anekdot_funny2_rugpt3Small', cache_dir='/tmp')
temp = GPT2LMHeadModel.from_pretrained('mmm-da/anekdot_funny2_rugpt3Small', cache_dir='/tmp')
del temp

def postprocess_anekdot(text:str):
    ''' Что тут происходит:
        (Сделано)
        1. Текст обрезается по стоп токену
        2. Добавляются отсутствующие переносы строк после -
        3. Убираются повторяющиеся переносы строк
        (TODO) 4. Текст обрезается по последнему знаку препинания.
    '''
    print(text)
    result = text.replace('Анекдот. ','')
    result = result.replace('Анекдот.','')
    result = result.replace('—','\n—')
    result = result.split('</s>')[0]
    print(result)
    return result


def generate_anekdot(
    model_name_or_path:str,
    length:int = 100,
    t:float = 0.9,
    k:int = 0,
    p:float = 0.92,
    repetition_penalty:float=1.0,
    count:int = 1,
    seed:int = None
    ):

    logger.info("Generating anekdot")

    device = torch.device("cpu")
    
    seed = seed or random.randint(1,10000000)

    np.random.seed(seed)
    torch.manual_seed(seed)

    tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path, cache_dir='/tmp')
    model = GPT2LMHeadModel.from_pretrained(model_name_or_path, cache_dir='/tmp')
    model.to(device)

    text = "Анекдот."

    inpt = tokenizer.encode(text, return_tensors="pt")

    result = []
    out = model.generate(
        inpt.cpu(),
        max_length=length,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        top_k=k,
        top_p=p,
        temperature=t,
        num_return_sequences=count
    )
    for sequence in out:
        result.append(
            postprocess_anekdot(
                str(
                    tokenizer.decode(sequence)
                )
             )
        )

    logger.info("Done")
    del tokenizer
    del model
    return result
