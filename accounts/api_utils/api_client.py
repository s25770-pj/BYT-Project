import requests
from rest_framework.response import Response
from rest_framework import status


def get_user_details(user_token):
    url = 'https://127.0.0.1:8008/api/v1/user-details/'
    headers = {'Authorization': f'Token {user_token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return Response({'error': 'Something went wrong'}, status=status.HTTP_404_BAD_REQUEST)
