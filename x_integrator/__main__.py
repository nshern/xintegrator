import requests
import os


class Integration:
    def __init__(self, username):
        if not isinstance(username, str):
            raise ValueError("Username must be a string")
        self.username = username
        self._bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
        self.user_id = self._get_id_from_username()

    def _bearer_oauth(self, r, user_agent):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {self._bearer_token}"
        r.headers["User-Agent"] = user_agent
        return r

    def _connect_to_endpoint(self, url, user_agent):
        response = requests.request(
            "GET",
            url,
            auth=lambda r: self._bearer_oauth(r, user_agent),
        )
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    def _get_id_from_username(self):
        url = f"https://api.twitter.com/2/users/by?usernames={self.username}"
        json_response = self._connect_to_endpoint(
            url=url, user_agent="v2UserLookupPython"
        )

        # TODO: Make some kind of try-except here,
        # TODO:  to check if the user actually exists

        id = json_response["data"][0]["id"]
        return id
