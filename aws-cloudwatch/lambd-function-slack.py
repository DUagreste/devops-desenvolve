from botocore.vendored import requests
import boto3
import json

client = boto3.client('sns')

site = 'URL DO SITE'
web_hook = 'URL WEB_HOOK'
mensagem = {'text': '=====Houston, we have a problem!====='}

def lambda_handler(event, context):
   try:
       requests.get(site, timeout=5)
       print('Site OK!')
   except Exception:
       print('Houston, we have a problem!')
       envia_notificacao()

def envia_notificacao():
   client.publish(
       TopicArn='ARN DO TÓPICO',
       Message='Houston, we have a problem!',
       Subject='ALERTA')
   requests.post(web_hook, data=json.dumps(mensagem))