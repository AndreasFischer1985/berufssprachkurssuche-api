"""
    Arbeitsagentur Berufssprachkurssuche API

    Eine der größten Berufssprachförderungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** bd24f42e-ad0b-4005-b834-23bb6800dc6c  **ClientSecret:** 6776b89e-5728-4643-8cd5-c93aefb5314b   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.berufssprachkurssuche.api.berufssprachkurse_api import (  # noqa: E501
    BerufssprachkurseApi,
)

from deutschland import berufssprachkurssuche


class TestBerufssprachkurseApi(unittest.TestCase):
    """BerufssprachkurseApi unit test stubs"""

    def setUp(self):
        self.api = BerufssprachkurseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_berufssprachkurssuche(self):
        """Test case for berufssprachkurssuche

        Berufssprachkurssuche  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()