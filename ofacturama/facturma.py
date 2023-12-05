import requests
import base64
import json

endpoints = {
    "clients": "https://apisandbox.facturama.mx/client",
    "products": "https://apisandbox.facturama.mx/product",
    "cfdi": "https://apisandbox.facturama.mx/3/cfdis",
}


class BasicAuthentication:
    def __init__(self, user: str, password: str) -> None:
        # Tu nombre de usuario y contraseña para la autenticación básica
        self.username = user
        self.password = password

        self._headers = self.encodeAuthorization()

    @property
    def headers(self) -> dict:
        return self._headers

    def encodeAuthorization(self) -> dict:
        # Codificar el nombre de usuario y la contraseña en base64
        auth_string = f"{self.username}:{self.password}"
        base64_auth_string = base64.b64encode(auth_string.encode()).decode()

        # Crear el encabezado de autenticación
        headers = {"Authorization": f"Basic {base64_auth_string}"}

        return headers


class Client:
    def __init__(self, basic_auth: BasicAuthentication) -> None:
        self.headers = basic_auth.headers

    def list(self) -> dict:
        # Realiza la solicitud GET
        response = requests.get(endpoints["clients"], headers=self.headers)

        if response.status_code == 200:
            # La solicitud fue exitosa
            data = response.json()  # Si la respuesta es JSON
            # Puedes procesar 'data' aquí según tus necesidades
            print(data)
            return data

        # La solicitud falló
        print(f"Error: {response.status_code} - {response.text}")


class Product:
    def __init__(self, basic_auth: BasicAuthentication) -> None:
        self.headers = basic_auth.headers

    def list(self) -> dict:
        # Realiza la solicitud GET
        response = requests.get(endpoints["products"], headers=self.headers)

        if response.status_code == 200:
            # La solicitud fue exitosa
            data = response.json()  # Si la respuesta es JSON
            # Puedes procesar 'data' aquí según tus necesidades
            return data

        # La solicitud falló
        print(f"Error: {response.status_code} - {response.text}")

    def create(self, data) -> dict:
        response = requests.post(endpoints["products"], json=data, headers=self.headers)
        if response.status_code == 201:
            # La solicitud fue exitosa
            data = response.json()  # Si la respuesta es JSON
            # Puedes procesar 'data' aquí según tus necesidades
            result = {"status_code": response.status_code, "data": data}
            return result

        print(f"Error: {response.status_code} - {response.text}")

        return {"status_code": response.status_code, "data": ""}

    def retrieve(self, id: str):
        response = requests.get(endpoints["products"] + f"/{id}", headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            return data

        print(f"Error: {response.status_code} - {response.text}")

    def delete(self, id: str):
        response = requests.delete(
            endpoints["products"] + f"/{id}", headers=self.headers
        )

        if response.status_code == 200:
            data = response.json()
            return data

        print(f"Error: {response.status_code} - {response.text}")

    def update(self, new_data: dict, id: str):
        response = requests.put(
            endpoints["products"] + f"/{id}", json=new_data, headers=self.headers
        )

        if response.status_code == 200:
            data = response.json()
            return data

        print(f"Error: {response.status_code} - {response.text}")


class Cfdi:
    def __init__(self, basic_auth: BasicAuthentication) -> None:
        self.headers = basic_auth.headers

    def create(self, data) -> dict:
        response = requests.post(endpoints["cfdi"], json=data, headers=self.headers)

        import pdb

        pdb.set_trace()

        if response.status_code == 200:
            # La solicitud fue exitosa
            data = response.json()  # Si la respuesta es JSON
            # Puedes procesar 'data' aquí según tus necesidades
            return data

        print(f"Error: {response.status_code} - {response.text}")
