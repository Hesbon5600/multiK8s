from unittest.mock import patch, Mock
from rest_framework.views import status
from .base_test import TestBaseCase


class TestDocker(TestBaseCase):
    """
    Handle tests
    """

    def test_docker_succeeds(self):
        res = self.docker_successfull()
        self.assertIsInstance(res.data, dict)
