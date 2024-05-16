from enum import Enum
from pydantic import BaseModel
from typing import Optional, List, Union


class Mes(str, Enum):
    tipo_1 = 'Janeiro'
    tipo_2 = 'Fevereiro'
    tipo_3 = 'Marco'
    tipo_4 = 'Abril'
    tipo_5 = 'Maio'
    tipo_6 = 'Junho'
    tipo_7 = 'Julho'
    tipo_8 = 'Agosto'
    tipo_9 = 'Setembro'
    tipo_10 = 'Outubro'
    tipo_11 = 'Novembro'
    tipo_12 = 'Dezembro'
    


class ResponseSite(BaseModel):
    id: Optional[Union[int, str]]  = ''
    exercicio: Optional[Union[int, str]]  = ''
    mes: Optional[Union[int, str]]  = ''
    descricaoReceita: Optional[Union[int, str]]  = ''
    valorPrevisao: Optional[float]  = 0.0
    valorReceitaNoMes: Optional[float]  = 0.0
    valorReceitaAteMes: Optional[float]  = 0.0
    

class ResponseDefault(BaseModel):
    code: int
    message: str
    datetime: str
    results: List[ResponseSite]

class ResponseError(BaseModel):
    code: int
    message: str