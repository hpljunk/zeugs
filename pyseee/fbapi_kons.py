# -*- coding: utf-8 -*-
import locale,pickle,os
from facebook import Facebook
language, output_encoding = locale.getdefaultlocale()

# Get api_key and secret_key from a file
homedir = os.path.expanduser('~')
fbs = open(homedir + '/.fbkeys').readlines()
facebook = Facebook(fbs[0].strip(), fbs[1].strip())
facebook.auth.createToken()
# Show login window
facebook.login()

facebook.auth.getSession()

info = facebook.users.getInfo([facebook.uid], ['name', 'birthday', 'affiliations', 'sex'])[0]

friends = facebook.friends.get()

dat = facebook.users.getInfo(friends,apiattr)

for da in dat: # put to dict
    userdata[da[u'uid']] = da
#

###############################################################################
#                               try outs

'SELECT uid,status_id,message from status where uid in (select uid2 from friend where uid1= uid)'

uidi=1229657643
 query = 'SELECT uid,status_id,message FROM status WHERE uid IN (SELECT uid FROM status WHERE uid = uidi)'

my_events = app.fql('''select name from event
                where eid in (select eid from event_member
                where uid = 8112822)



query = 'SELECT uid,status_id,message FROM status WHERE uid IN (SELECT uid2 FROM friend WHERE uid1=1317318580)'
FacebookError: Error 604: Can't lookup all friends of 1317318580; can only lookup for the logged in user (1056165140) or for pairs of users

query = 'SELECT uid,status_id,message FROM status WHERE uid IN (SELECT uid2 FROM friend WHERE uid1=1056165140)'
No JSON object could be decoded




