_requests = {
    'pan': {
        'name': 'pan for pancakes',
        'condition': 'clean, non-stick',
        'time': '2 weeks',
        'benefits': '10 pancakes'
    },
    'hair dryer': {
        'name': 'hair dryer',
        'condition': 'three speeds, cold and hot airflow',
        'time': 'until 25 november',
        'benefits': '2 sweets milka'
    },
    'laptop': {
        'name': 'laptop',
        'condition': '--',
        'time': '2 weeks',
        'benefits': '10 pancakes',
    },
    'nude shoes, heels ': {
        'name': 'nude shoes, heels ',
        'condition': 'new, 38size',
        'time': '27 nov',
        'benefits': '500 rub',
    },
    'shoe dryer': {
        'name': 'shoe dryer',
        'condition': 'clean',
        'time': '1 week',
        'benefits': 'lays and orange juice',
    },
    'mirror': {
        'name': 'mirror',
        'condition': 'around 1 meters, clean',
        'time': '3 weeks',
        'benefits': '700rub',
    },
    'Bakeware': {
        'name': 'Bakeware',
        'condition': 'cute',
        'time': '1 week',
        'benefits': '5 cakes',
    },
    'charging on iphone': {
        'name': 'charging on iphone',
        'condition': '--',
        'time': 'until 22 nov',
        'benefits': '100rub and chocolate',
    },
    'outlet extension': {
        'name': 'outlet extension',
        'condition': '--',
        'time': 'until friday',
        'benefits': 'chocolate',
    },
    'flash drive': {
        'name': 'fash drive',
        'condition': 'free 1gb',
        'time': '1 weeks',
        'benefits': '200rub',
    }
}

_request_list = []

for staff, request_data in _requests.items():
    _new_element = {'staff': staff}
    _new_element.update(request_data)
    _request_list.append(_new_element)


# Get requests filtered by name
def get_requests_by_name(q):
    results = []
    # SEARCH

    for request in _request_list:
       if request['name'].lower() .find(q.lower()) >=0:
            results.append(request)

    return results






def get_request(requestname):
        return _requests.get(requestname)
