from fastapi import FastAPI
import anekdot
from random import choice
from enum import Enum
import logging

app = FastAPI()
logging.basicConfig(filename='generator.log',
                    encoding='utf-8', level=logging.DEBUG)


class ModelName(str, Enum):
    funny1 = 'mmm-da/anekdot_funny1_rugpt3Small'
    funny2 = 'mmm-da/anekdot_funny2_rugpt3Small'


@app.get("/anekdot")
async def get_anekdot(
        model_name: ModelName = ModelName.funny1.value,
        length: int = 100,
        t: float = 0.9,
        k: int = 0,
        p: float = 0.92,
        repetition_penalty: float = 1.0,
        sequence_count: int = 1):

    generation_result = anekdot.generate_anekdot(
        model_name,
        length,
        t,
        k,
        p,
        repetition_penalty,
        sequence_count
    )

    for i in generation_result:
        i = anekdot.postprocess_anekdot(i)
    return {"anekdot": generation_result}
