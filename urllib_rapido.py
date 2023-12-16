import asyncio
import aiohttp
import json
import time

BASE_URL = "https://httpbin.org"

async def make_request(session, method, endpoint, data=None):
    """Realiza uma requisição HTTP e retorna os dados em formato JSON."""
    url = f"{BASE_URL}/{endpoint}"

    async with session.request(method, url, json=data) as response:
        return await response.json()

async def execute_requests(requests_list):
    """Executa uma lista de requisições de forma assíncrona."""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for request_name, request_data in requests_list.items():
            task = make_request(session, request_data['method'], request_data['endpoint'], request_data.get('data'))
            tasks.append(asyncio.ensure_future(task))

        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)

async def main():
    """Função principal para realizar chamadas e medir o tempo de execução."""
    start = time.perf_counter()

    requests_list = {
        'GET': {'method': 'GET', 'endpoint': 'get'},
        'POST': {'method': 'POST', 'endpoint': 'post', 'data': {"key": "value"}},
        'PUT': {'method': 'PUT', 'endpoint': 'put', 'data': {"key": "updated_value"}},
        'DELETE': {'method': 'DELETE', 'endpoint': 'delete'}
    }

    await execute_requests(requests_list)

    end = time.perf_counter()
    print(f"Tempo decorrido: {end - start:.2f} segundos.")

if __name__ == "__main__":
    asyncio.run(main())
