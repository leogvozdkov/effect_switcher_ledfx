import requests
import random
import time
import json

scenes_ids = json.loads(requests.get('http://127.0.0.1:8888/api/scenes').text)
ids = []
for preset in scenes_ids['scenes']:
    ids.append(preset)

while True:
    effect = random.choice(ids)
    data = '{"id":"%s","action":"activate"}' % effect
    r = requests.put('http://127.0.0.1:8888/api/scenes', data=data)
    time1 = random.randint(30, 60)
    if effect == 'strobe':
        time1 = 10
    time.sleep(time1)
    print(f'switch preset {effect} for {time1} seconds')
