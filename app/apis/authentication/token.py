# generates token used bu user to reset password
import datetime
import jwt
from django.conf import settings
from rest_framework import exceptions
# from ..authentication.models import User
# from .serialization_errors import jwt_errors


# def generate_password_reset_token(email, id_):
#     """
#     generates token that expires in an hour
#     Args:
#         email (str): user email
#         id_ (str): user id
#     Return:
#         token (str): a token that expires in the specified time
#     """
#     time = datetime.datetime.utcnow(
#     ) + datetime.timedelta(hours=int(settings.RESET_TOKEN_EXP_TIME))
#     payload = {
#         'email': email,
#         'id': id_,
#         'exp': time
#     }
#     token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
#     return token.decode('utf-8')


def get_token_data(token):
    """
    checks validity of a token
    Args:
        token (str): token to be validated
    Return:
        user (obj): valid user object
    """
    pass
    # try:
    #     payload = jwt.decode(
    #         token, settings.SECRET_KEY, algorithms="HS256", )
    #     user = User.objects.get(email=payload['email'])
    # except Exception as error:
    #     exception_mapper = {
    #         jwt.ExpiredSignatureError: jwt_errors['token_expired'],
    #         jwt.DecodeError: jwt_errors['invalid_token'],
    #         jwt.InvalidIssuerError: jwt_errors['invalid_secret'],
    #         User.DoesNotExist: jwt_errors['token_user_not_found']
    #     }
    #     message = exception_mapper.get(
    #         type(error), 'Authorization failed.')
    #     raise exceptions.AuthenticationFailed(message)
    # return user
