# Importando libs
# stdlib imports
from os import environ as env
from datetime import datetime

# 3rd party imports
import aiohttp
from fastapi.logger import logger
from fastapi.responses import JSONResponse
from fastapi import status

# Local imports
from src.models import *
from utils.util import get_headers

# Captura variáveis de ambiente e cria constantes
TIMEOUT = env.get('TIMEOUT', default=180)

#-----------------------------------------------------------------------------------------------------
async def fetch(ano: int, mes: str = ''):
    if not ano or not mes:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"code": 422, "message": "Unprocessable Entity",
                     "datetime": datetime.now().isoformat()}
        )
    
    
    mes_dict = {
        'Janeiro': '1',
        'Fevereiro': '2',
        'Marco': '3',
        'Abril': '4',
        'Maio': '5',
        'Junho': '6',
        'Julho': '7',
        'Agosto': '8',
        'Setembro': '9',
        'Outubro': '10',
        'Novembro': '11',
        'Dezembro': '12'
    }

    if mes in mes_dict:
        mes = mes_dict[mes]
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"code": 400, "message": "Argumentos inválidos",
                     "datetime": datetime.now().isoformat()}
        )

    logger.info(f"Consulta: {mes}/{ano}")

    # Configura os timeouts
    timeout = aiohttp.ClientTimeout(total=TIMEOUT)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        # Configurando headers
        session.headers.update(get_headers())
        session.headers.update({'Referer': 'https://portaltransparencia.fortaleza.ce.gov.br'})

        try:
            
            url = f'https://portaltransparencia-back.sepog.fortaleza.ce.gov.br/api/receitas/federais/{ano}/{mes}'

            async with session.get(url, ssl=False, allow_redirects=True) as resp:
                logger.debug(f"Consulta: {resp.status} - {url}")
                response_data = await resp.json()
                
                if not response_data:
                    result = ResponseDefault(
                        code=0,
                        message='Não foi encontrado transferencias para o período informado',
                        results=[],
                        datetime=str(datetime.now()),
                    )
                else:
                    results = [ResponseSite(**item) for item in response_data]  # Cria uma lista de ResponseSite
                    result = ResponseDefault(
                        code=0,
                        message='Consulta realizada com sucesso',
                        results=results,
                        datetime=str(datetime.now()),
                    )
        except aiohttp.ClientError as e:
            logger.exception('Erro durante a consulta API')
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    'code': 500,
                    'message': f'INTERNAL_SERVER_ERROR: {str(e)}'
                }
            )
        except Exception as e:
            logger.exception('Erro inesperado durante a consulta API')
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    'code': 500,
                    'message': f'INTERNAL_SERVER_ERROR: {str(e)}'
                }
            )

        logger.info(f"Consulta finalizada: {result}")
        return result
