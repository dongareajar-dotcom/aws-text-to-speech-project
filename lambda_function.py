import boto3
import os
from datetime import datetime
from urllib.parse import unquote_plus

s3 = boto3.client('s3')
polly = boto3.client('polly')
sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

TABLE_NAME = os.environ['TABLE_NAME']
TOPIC_ARN = os.environ['TOPIC_ARN']

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = unquote_plus(event['Records'][0]['s3']['object']['key'])

    print(f"Bucket: {bucket}")
    print(f"Key: {key}")

    try:
        response = s3.get_object(
            Bucket=bucket,
            Key=key
        )

        text = response['Body'].read().decode('utf-8')

        speech = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )

        audio_file = os.path.basename(key).replace('.txt', '.mp3')

        s3.put_object(
            Bucket=bucket,
            Key=f"audio/{audio_file}",
            Body=speech['AudioStream'].read(),
            ContentType='audio/mpeg'
        )

        table = dynamodb.Table(TABLE_NAME)

        table.put_item(
            Item={
                'FileName': key,
                'ProcessedTime': datetime.now().isoformat(),
                'Status': 'SUCCESS',
                'AudioFile': audio_file
            }
        )

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject='Text Converted',
            Message=f'{key} converted successfully.'
        )

        return {
            'statusCode': 200,
            'body': 'Success'
        }

    except Exception as e:
        print(str(e))
        raise e
