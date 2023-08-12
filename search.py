import json
import sys
import requests
import os

filePath = sys.argv[1]
searchUrl = 'https://yandex.com/images/search'
files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
response = requests.post(searchUrl, params=params, files=files)
query_string = json.loads(response.content)['blocks'][0]['params']['url']
img_search_url= searchUrl + '?' + query_string
os.system("/usr/bin/open '" + img_search_url + "'")