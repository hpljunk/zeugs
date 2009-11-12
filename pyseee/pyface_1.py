# -*- coding: utf-8 -*-
import locale,pickle,os
from facebook import Facebook
language, output_encoding = locale.getdefaultlocale()


def get_album(uid):
    album = facebook.photos.getAlbums(uid,NULL)





def desktop_app():

    userdata = {}

    apiattr = ['uid', 'name', 'about_me', 'activities', 'birthday_date', 'relationship_status',
            'books', 'current_location', 'email_hashes', 'first_name', 'hometown_location',
            'hs_info', 'interests', 'last_name', 'locale', 'meeting_for', 'meeting_sex',
            'movies', 'music', 'notes_count', 'notes_count', 'pic_with_logo', 'pic_big',
            'pic_big_with_logo','pic_small','pic_small_with_logo','pic_square','pic_square_with_logo',
            'political','profile_blurb','profile_update_time','profile_url','proxied_email',
            'quotes','religion','sex','significant_other_id','status','timezone','tv','username',
            'username','wall_count','website','work_history',
            'education_history', 'affiliations']

    # Get api_key and secret_key from a file
    homedir = os.path.expanduser('~')
    fbs = open(homedir + '/.fbkeys').readlines()
    facebook = Facebook(fbs[0].strip(), fbs[1].strip())

    file = open('fbdat_1.txt', 'w')

    facebook.auth.createToken()
    # Show login window
    facebook.login()
    wait_login()                # somehow wait for the user to log in

    # Login to the window, then press enter
    #print 'After logging in, press enter...'
    #raw_input()

    facebook.auth.getSession()
    info = facebook.users.getInfo([facebook.uid], ['name', 'birthday', 'affiliations', 'sex'])[0]

    for attr in info:
        print '%s: %s' % (attr, info[attr])

    friends = facebook.friends.get()
    print friends

    dat = facebook.users.getInfo(friends,apiattr)
    print '################################ DAT #########################'
    print dat


    for da in dat: # put to dict
        userdata[da[u'uid']] = da

    print '################################ USERDATA ####################'
    print userdata
    pickle.dump(userdata, file)

##    for user in userdata:
##        #if not user.haskey(u'uid'):
##        s = str(userdata[user])
##        sd = s.encode(output_encoding)
##        file.write(sd)


    file.close()
    exit()

##        if 'birthday' in friend:
##            print friend['name'], 'has a birthday on', friend['birthday'], 'and is', friend['relationship_status']
##        else:
##            print friend['name'], 'has no birthday and is', friend['relationship_status']
##    arefriends = facebook.friends.areFriends([friends[0]['uid']], [friends[1]['uid']])
##    photos = facebook.photos.getAlbums(friends[1]['uid'])
##print photos

if __name__ == "__main__":
    desktop_app()

