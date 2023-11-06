import requests


class BaseApi:
    def __init__(self):
        self._base_url = "https://practice.expandtesting.com/notes/api"
        self._headers = {
            'Content-Type': 'application/json',
            'x-auth-token': None
        }

    def _get(self, url, headers=None):
        if not headers:
            headers = self._headers
        response = requests.get(f'{self._base_url}{url}', headers=headers)
        return response

    def _post(self, url, data, headers=None):
        if not headers:
            headers = self._headers
        response = requests.post(f'{self._base_url}{url}', data=data, headers=headers)
        return response

    def _patch(self, url, data, headers=None):
        if not headers:
            headers = self._headers
        response = requests.patch(f'{self._base_url}{url}', data=data, headers=headers)
        return response

    def _put(self, url, data, headers=None):
        if not headers:
            headers = self._headers
        response = requests.put(f'{self._base_url}{url}', data=data, headers=headers)
        return response

    def _delete(self, url, data=None, headers=None):
        if not headers:
            headers = self._headers
        response = requests.delete(f'{self._base_url}{url}', data=data, headers=headers)
        return response
