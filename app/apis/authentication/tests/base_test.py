from unittest.mock import patch, Mock
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse


class TestBaseCase(APITestCase):
    def setUp(self):
        """
        Method for setting up user
        """
        self.test_docker = api_reverse('authentication:test-docker')

        self.valid_user = {
            'first_name': 'jane',
            'last_name': 'Doe',
            'surname': 'jDoe',
            'username': 'jDoe',
            'email': 'jane@doe.com',
            'password': 'janeDoe@123',
            'id_number': 123,
            'phone_number': "+25412534545"
        }

    @patch("app.apis.authentication.views.test_docker", Mock(return_value=True))
    def docker_successfull(self):
        """
        methid to login user
        """
        response = self.client.post(self.test_docker,
                                    self.valid_user, format='json')
        return response

