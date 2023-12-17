from typing import Any
import time
import requests

BASE_URL = "https://httpbin.org"


def fetch_get(session: requests.Session) -> Any:
    """Realiza uma requisição GET e retorna os dados em formato JSON."""
    response = session.get(f"{BASE_URL}/get")
    return response.json()


def fetch_post(session: requests.Session) -> Any:
    """Realiza uma requisição POST e retorna os dados em formato JSON."""
    data_to_post = {"key": "value"}
    response = session.post(f"{BASE_URL}/post", json=data_to_post)
    return response.json()


def fetch_put(session: requests.Session) -> Any:
    """Realiza uma requisição PUT e retorna os dados em formato JSON."""
    data_to_put = {"key": "updated_value"}
    response = session.put(f"{BASE_URL}/put", json=data_to_put)
    return response.json()


def fetch_delete(session: requests.Session) -> Any:
    """Realiza uma requisição DELETE e retorna os dados em formato JSON."""
    response = session.delete(f"{BASE_URL}/delete")
    return response.json()


def main() -> None:
    """Função principal para realizar chamadas e medir o tempo de execução."""
    start = time.perf_counter()

    with requests.Session() as session:
        print(fetch_get(session))
        print(fetch_post(session))
        print(fetch_put(session))
        print(fetch_delete(session))

    end = time.perf_counter()
    print(f"Tempo decorrido: {end - start:.2f} segundos.")


if __name__ == "__main__":
    main()
