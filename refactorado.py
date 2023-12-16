from typing import Any
import time
import requests

BASE_URL = "https://httpbin.org"


def make_request(session: requests.Session, method: str, endpoint: str, data: dict = None) -> Any:
    """Realiza uma requisição HTTP e retorna os dados em formato JSON."""
    try:
        response = session.request(method, f"{BASE_URL}/{endpoint}", json=data)
        response.raise_for_status()  # Verifica se houve algum erro na requisição
        return response.json()
    except requests.RequestException as e:
        print(f"Erro na requisição {method} {endpoint}: {e}")
        return None


def main() -> None:
    """Função principal para realizar chamadas e medir o tempo de execução."""
    start = time.perf_counter()

    with requests.Session() as session:
        print(make_request(session, 'GET', 'get'))
        print(make_request(session, 'POST', 'post', {"key": "value"}))
        print(make_request(session, 'PUT', 'put', {"key": "updated_value"}))
        print(make_request(session, 'DELETE', 'delete'))

    end = time.perf_counter()
    print(f"Tempo decorrido: {end - start:.2f} segundos.")


if __name__ == "__main__":
    main()
