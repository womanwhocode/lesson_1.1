import json

with  open('/Users/alyona_zaytseva/PycharmProjects/note.txt') as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = {}


print(res)
