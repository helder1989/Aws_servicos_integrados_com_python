import boto3

import os

access_key = os.environ.get("AWS_ACCESS_KEY_ID")
secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")


# Criando o serviço com as credenciais da AWS

client = boto3.client(
    service_name='sns',
    region_name='us-east-1',  # ***REGIÃO DO SEU SERVIÇO***
    aws_access_key_id='***SUA ACCESS_KEY***',
    aws_secret_access_key='***SUA SECRET_KEY**'
)

# Enviando o SMS para o número desejado

client.publish(
    PhoneNumber="+55310000000",
    Message="Exame da aws Associate? :)"
)

