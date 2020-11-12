import urllib.request
import json
with urllib.request.urlopen('https://unsplash.com/napi/topics/wallpapers/photos?page=1&per_page=10') as response:
   html = response.read()
   res_json=json.loads(html)
print(len(res_json))
for i in range(len(res_json)):
   print(res_json[i]['urls']['full'])
for i in range(len(res_json)):
   filename=str(i)
   filename=filename+".jpg"
   urllib.request.urlretrieve(res_json[i]['urls']['full'],filename)