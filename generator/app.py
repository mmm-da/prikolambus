from fastapi import FastAPI
from numpy.lib import index_tricks
import anekdot
from random import choice,randint
from enum import Enum
import logging

app = FastAPI()
logging.basicConfig(filename='generator.log',
                    encoding='utf-8', level=logging.DEBUG)


@app.get("/anekdot")
async def get_anekdot(
        model_name: str = 'mmm-da/anekdot_funny1_rugpt3Small',
        length: int = 100,
        t: float = 0.9,
        k: int = 0,
        p: float = 0.92,
        repetition_penalty: float = 1.0,
        sequence_count: int = 1,
        seed: int = None):

    seed = seed or randint(1,10000000)

    generation_result = anekdot.generate_anekdot(
        model_name,
        length,
        t,
        k,
        p,
        repetition_penalty,
        sequence_count,
        seed
    )

    for i in generation_result:
        i = anekdot.postprocess_anekdot(i)
    return {"anekdot": generation_result}
