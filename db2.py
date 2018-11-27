_users = {
    'paul': {
        'name': 'Pavel Okdvd',
        'course': '5d course',
        'workplace': 'HSE'
    },
    'sergey': {
        'name': 'Sergey Ogvsdv',
        'course': '2sd course',
        'workplace': 'HSE'
    },
    'petr': {
        'name': 'Petr Okcvds',
        'course': '2sd course',
        'workplace': 'HSE'
    },
    'tanya': {
        'name': 'Tatiana Okhy',
        'course': '2sd course',
        'workplace': 'HSE'
    },
    'vasya': {
        'name': 'Vasiliy Ok',
        'course': '2sd course',
        'workplace': 'HSE'
    },
    'dasha': {
        'name': 'Daria Ok',
        'course': '3d course',
        'workplace': 'HSE'
    },
    'anton': {
        'name': 'Anton Ok',
        'course': '2sd course',
        'workplace': 'HSE'
    },
    'masha': {
        'name': 'Maria Okvrfrgre',
        'course': '2sd course',
        'workplace': 'HSE'
    },
    'nika': {
        'name': 'Nika Jefadak',
        'course': '1st course',
        'workplace': 'HSE'
    },
    'igor': {
        'name': 'igor Ot',
        'course': '1st course',
        'workplace': 'HSE'
    }
}



_user_list = []

for login, user_data in _users.items():
    _new_element = {'login': login}
    _new_element.update(user_data)
    _user_list.append(_new_element)


# Get users filtered by name
def get_users_by_name(q):
    results = []
    # SEARCH

    for user in _user_list:
       if user['name'].lower() .find(q.lower()) >=0:
            results.append(user)

    return results




def get_user(username):
    return _users.get(username)



