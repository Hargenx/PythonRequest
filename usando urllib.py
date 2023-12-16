import json
import time
from urllib import request, parse

BASE_URL = "https://httpbin.org"

def make_request(method, endpoint, data=None):
    """Realiza uma requisição HTTP e retorna os dados em formato JSON."""
    url = f"{BASE_URL}/{endpoint}"
    headers = {'Content-Type': 'application/json'}

    if data:
        data = json.dumps(data).encode('utf-8')

    req = request.Request(url, method=method, data=data, headers=headers)

    try:
        with request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except request.HTTPError as e:
        print(f"Erro na requisição {method} {endpoint}: {e}")
        return None

def execute_requests(requests_list):
    """Executa uma lista de requisições."""
    for request_name, request_data in requests_list.items():
        print(make_request(request_data['method'], request_data['endpoint'], request_data.get('data')))
        time.sleep(1)

def main():
    """Função principal para realizar chamadas e medir o tempo de execução."""
    start = time.perf_counter()

    requests_list = {
        'GET': {'method': 'GET', 'endpoint': 'get'},
        'POST': {'method': 'POST', 'endpoint': 'post', 'data': {"key": "value"}},
        'PUT': {'method': 'PUT', 'endpoint': 'put', 'data': {"key": "updated_value"}},
        'DELETE': {'method': 'DELETE', 'endpoint': 'delete'}
    }

    execute_requests(requests_list)

    end = time.perf_counter()
    print(f"Tempo decorrido: {end - start:.2f} segundos.")

if __name__ == "__main__":
    main()
