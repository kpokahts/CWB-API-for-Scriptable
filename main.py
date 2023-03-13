import json
import re
import requests

def lambda_handler(event, context):
    args = event['queryStringParameters']
    url = get_radar(args['stn'])
    return {
        'statusCode': 200,
        'body': json.dumps({'url': url})
    }


def get_radar(stn:str):
    if stn not in ['RCSL', 'RCNT', 'RCLY']:
        raise ValueError('stn must be RCSL, RCNT, RCLY')
    res = requests.get('https://www.cwb.gov.tw/Data/js/obs_img/Observe_radar_rain.js')
    content = res.text
    image_url = re.findall(fr'(CV1_{stn}[\w\/]+.png)', content)[0]
    full_url = f'https://www.cwb.gov.tw/Data/radar_rain/{image_url}'

    return full_url

#github actions to aws lambda test
