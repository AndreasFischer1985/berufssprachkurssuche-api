"""
    Arbeitsagentur Berufssprachkurssuche API

    Eine der größten Berufssprachförderungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** bd24f42e-ad0b-4005-b834-23bb6800dc6c  **ClientSecret:** 6776b89e-5728-4643-8cd5-c93aefb5314b   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.berufssprachkurssuche.model.response_embedded_links_first import (
    ResponseEmbeddedLinksFirst,
)

from deutschland import berufssprachkurssuche

globals()["ResponseEmbeddedLinksFirst"] = ResponseEmbeddedLinksFirst
from deutschland.berufssprachkurssuche.model.response_embedded_links import (
    ResponseEmbeddedLinks,
)


class TestResponseEmbeddedLinks(unittest.TestCase):
    """ResponseEmbeddedLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseEmbeddedLinks(self):
        """Test ResponseEmbeddedLinks"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseEmbeddedLinks()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
