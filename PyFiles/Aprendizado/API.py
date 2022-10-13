import json
import requests


def API_request(url, **kwargs):

    url = url + "?"

    for item, value in kwargs.items():
        query = f"{item}="

        if type(value) in [list, tuple]:
            for v in value:
                query += f"{{{v}}},"
            query = query[:-1]
        else:
            query += f"{value}"

        url += query + "&"
    url = url[:-1]

    request = requests.get(url)
    request = json.loads(request.text)

    if type(request) not in [tuple, list]:
        return request
    return request
