import sqlite3

conn = sqlite3.connect('app.db')

c = conn.cursor()

c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    name TEXT,
    course TEXT,
    workplace TEXT,
    photo TEXT

)
''')

conn.commit()

c.execute('''
    INSERT INTO users (name, course, workplace)
    VALUES ("Paul Okopnyi", "4", "HSE")
''')

c.execute('''
    ALTER TABLE users
    ADD COLUMN login TEXT
''')


conn.commit()

c.execute('''
    UPDATE users
    SET login = "paul"
    WHERE name = "Paul Okopnyi"
''')

conn.commit()

users = [

    {
         'login': 'paul',
         'name': 'Pavel Okdvd',
         'course': '5d course',
         'workplace': 'HSE'
    },
    {
        'login': 'vasya',
        'name': 'Vasiliy Ok',
        'course': '2sd course',
        'workplace': 'HSE'
    },
    {
        'login': 'dasha',
        'name': 'Daria Ok',
        'course': '3d course',
        'workplace': 'HSE'
    },
    {
        'login': 'anton',
        'name': 'Anton Ok',
        'course': '2sd course',
        'workplace': 'HSE'
    },
    {
        'login': 'masha',
        'name': 'Maria Okvrfrgre',
        'course': '2sd course',
        'workplace': 'HSE'
    },
    {
        'login': 'nika',
        'name': 'Nika Jefadak',
        'course': '1st course',
        'workplace': 'HSE'
    },
    {
        'login': 'igor',
        'name': 'igor Ot',
        'course': '1st course',
        'workplace': 'HSE'
    }

]



for user in users:
    c.execute("INSERT INTO users "
              "(login, name, course, workplace)"
              "VALUES "
              "('{login}', '{name}', '{course}', '{workplace}')".format(**user))
    conn.commit()

c.execute('''
    CREATE TABLE requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        conditions TEXT,
        time DATETIME,
        benefits TEXT
    )
''')

conn.commit()


requests = [
    {
        'name': 'pan for pancakes',
        'condition': 'clean, non-stick',
        'time': '2 weeks',
        'benefits': '10 pancakes'
    },
    {
        'name': 'hair dryer',
        'condition': 'three speeds, cold and hot airflow',
        'time': 'until 25 november',
        'benefits': '2 sweets milka'
    },
    {
        'name': 'laptop',
        'condition': '--',
        'time': '2 weeks',
        'benefits': '10 pancakes',
    },
    {
        'name': 'nude shoes, heels ',
        'condition': 'new, 38size',
        'time': '27 nov',
        'benefits': '500 rub',
    },
    {
        'name': 'shoe dryer',
        'condition': 'clean',
        'time': '1 week',
        'benefits': 'lays and orange juice',
    },
    {
        'name': 'mirror',
        'condition': 'around 1 meters, clean',
        'time': '3 weeks',
        'benefits': '700rub',
    },
    {
        'name': 'Bakeware',
        'condition': 'cute',
        'time': '1 week',
        'benefits': '5 cakes',
    },
    {
        'name': 'charging on iphone',
        'condition': '--',
        'time': 'until 22 nov',
        'benefits': '100rub and chocolate',
    },
    {
        'name': 'outlet extension',
        'condition': '--',
        'time': 'until friday',
        'benefits': 'chocolate',
    },
    {
        'name': 'fash drive',
        'condition': 'free 1gb',
        'time': '1 weeks',
        'benefits': '200rub',
    }


]


c.execute('''
    INSERT INTO requests (name, conditions, time, benefits)
    VALUES
    ("Pan","clean, non-stick", "2 weeks", "10 pancakes" )
''')
conn.commit()

c.execute('''
    CREATE TABLE users_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        request_id INTEGER
    )
''')

conn.commit()

c.execute("INSERT INTO users_requests (user_id, request_id) VALUES (1, 1)")
conn.commit()
c.execute("INSERT INTO users_requests (user_id, request_id) VALUES (3, 1)")
conn.commit()


c.execute("SELECT u.* "
          "FROM users_requests ur "
          "JOIN users u ON (u.id=ur.user_id) "
"WHERE ur.request_id=1")

conn.close()