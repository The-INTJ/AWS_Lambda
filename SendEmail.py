import boto3
import json
import urllib


ses = boto3.client('ses', region_name='us-east-1')

email_from = '' # Put relevent info in the single quotations
email_to = ''
email_cc = ''
emaiL_subject = 'S3 Python Lambda'
email_body = 'Body' # will be replaced later by relevant info


def lambda_handler(event, context):
    
    name = event['Records'][0]['s3']['object']['key']

    size = event['Records'][0]['s3']['object']['size']
    
    email_body = 'Name: ' + name + '\nSize: ' + str(size)
    
    
    response = ses.send_email(
        Source = email_from,
        Destination={
            'ToAddresses': [
                email_to
            ],
            'CcAddresses': [
                email_cc
            ]
        },
        Message={
            'Subject': {
                'Data': emaiL_subject
            },
            'Body': {
                'Text': {
                    'Data': email_body
                }
            }
        }
    )
    
