import facebook

apikey = '9e1d483876bd7b1068b50b1ffaffec60'
secret = '177e0cfa0c6b84f48bef940e9e2c6475'


fb = facebook.Facebook(apikey, secret)
token = fb.auth.createToken()  #u'AUTH_TOKEN'
fb.login()

session = fb.auth.getSession()  #{u'secret': u'DESKTOP_SECRET', u'session_key': u'SESSION_KEY', u'uid': u'13608493', u'expires': 1181156943}
user =  fb.users.getInfo([fb.uid], ['name', 'birthday'])
#[{u'birthday': u'August 18, 1988', u'name': u'Samuel Cormier-Iijima', u'uid': 13608493}]
