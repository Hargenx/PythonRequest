import asyncio
import aiohttp
import json
import logging
import time

logging.basicConfig(level=logging.INFO)

class HTTPClient:
    BASE_URL = "https://httpbin.org"

    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def close_session(self):
        await self.session.close()

    async def make_request(self, method, endpoint, data=None):
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        try:
            async with self.session.request(method, url, json=data, headers=headers) as response:
                response_data = await response.json()
                response.raise_for_status()
                return response_data
        except aiohttp.ClientError as e:
            logging.error(f"Erro ao fazer requisição {method} {endpoint}: {e}")
            return None

    async def execute_requests(self, requests_list):
        tasks = [self.make_request(req_data['method'], req_data['endpoint'], req_data.get('data'))
                 for req_name, req_data in requests_list.items()]
        return await asyncio.gather(*tasks)

async def main():
    start = time.perf_counter()

    client = HTTPClient()

    requests_list = {
        'GET': {'method': 'GET', 'endpoint': 'get'},
        'POST': {'method': 'POST', 'endpoint': 'post', 'data': {"key": "value"}},
        'PUT': {'method': 'PUT', 'endpoint': 'put', 'data': {"key": "updated_value"}},
        'DELETE': {'method': 'DELETE', 'endpoint': 'delete'}
    }

    responses = await client.execute_requests(requests_list)

    for response in responses:
        if response:
            logging.info(f"Response: {response}")

    await client.close_session()

    end = time.perf_counter()
    logging.info(f"Tempo decorrido: {end - start:.2f} segundos.")

if __name__ == "__main__":
    asyncio.run(main())