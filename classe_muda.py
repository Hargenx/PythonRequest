from typing import Any, Callable, Dict
import time
import requests
from dataclasses import dataclass

BASE_URL = "https://httpbin.org"

@dataclass
class RequestData:
    method: str
    endpoint: str
    data: Dict[str, Any] = None

def make_request(session: requests.Session, request_data: RequestData) -> Any:
    """Realiza uma requisição HTTP e retorna os dados em formato JSON."""
    try:
        response = session.request(request_data.method, f"{BASE_URL}/{request_data.endpoint}", json=request_data.data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro na requisição {request_data.method} {request_data.endpoint}: {e}")
        return None

def execute_requests(session: requests.Session, requests_list: Dict[str, Callable]) -> None:
    """Executa uma lista de requisições."""
    for request_name, request_func in requests_list.items():
        print(make_request(session, request_func()))
        time.sleep(1)  # Adiciona um pequeno intervalo entre as requisições

def main() -> None:
    """Função principal para realizar chamadas e medir o tempo de execução."""
    start = time.perf_counter()

    with requests.Session() as session:
        requests_list = {
            'GET': lambda: RequestData('GET', 'get'),
            'POST': lambda: RequestData('POST', 'post', {"key": "value"}),
            'PUT': lambda: RequestData('PUT', 'put', {"key": "updated_value"}),
            'DELETE': lambda: RequestData('DELETE', 'delete')
        }

        execute_requests(session, requests_list)

    end = time.perf_counter()
    print(f"Tempo decorrido: {end - start:.2f} segundos.")

if __name__ == "__main__":
    main()
