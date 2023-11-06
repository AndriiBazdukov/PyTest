import json
from tests.lesson_20_homework_api_testing.api_collections.apis._base_api import BaseApi
from tests.lesson_20_homework_api_testing.api_collections.data.user_request_url import UserRequestUrl


class UsersApi(BaseApi):
    def __init__(self):
        super().__init__()

    def post_new_user(self, user_data: dict):
        return self._post(url=UserRequestUrl.user_register, data=json.dumps(user_data), headers=self._headers)

    def post_login_user(self, user_data: dict):
        response = self._post(url=UserRequestUrl.user_login, data=json.dumps(user_data), headers=self._headers)
        return response

    def get_user_profile(self, token):
        headers = self._headers.update({"x-auth-token": token})
        return self._get(url=UserRequestUrl.user_profile, headers=headers)

    def patch_update_user_profile(self, token, body):
        headers = self._headers.update({"x-auth-token": token})
        return self._patch(url=UserRequestUrl.user_profile, headers=headers, data=json.dumps(body))

    def delete_current_session(self, token):
        headers = self._headers.update({"x-auth-token": token})
        return self._delete(url=UserRequestUrl.logout, headers=headers)

    def delete_user(self, token):
        headers = self._headers.update({"x-auth-token": token})
        return self._delete(url=UserRequestUrl.delete_account, headers=headers).json()

    @staticmethod
    def update_profile_data(name="Test Name", phone="", company=""):
        return {
            "name": name,
            "phone": phone,
            "company": company
        }
