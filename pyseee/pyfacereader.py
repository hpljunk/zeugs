# -*- coding: utf-8 -*-
import sys,locale,pickle
from prnDict import prnDict
language, output_encoding = locale.getdefaultlocale()


def desktop_app():
    from facebook import Facebook

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

    with open('fbdat_1.txt', 'r') as fi:
        alld = pickle.load(fi)

##    fi = open('fbdat_1.txt', 'r')
##    fo = open ('fbdatflat.txt', 'w')
##    alld = pickle.load(fi)
#    fo.write(prnDict(alld))#one row per element

    with open ('fbdatflat.txt', 'w') as fo:
        fo.write(prnDict(alld))#one row per element

    print 'i think this went ok'
    fi.close()
    fo.close()
    exit()


def safeprint(msg, errors="replace"):
    """Safely print the given string.
    see code points for unprintable characters
    errors="xmlcharrefreplace"
    """
    print msg.encode(sys.getdefaultencoding(),errors)



if __name__ == "__main__":
    desktop_app()

##    for user in alld:
##        safeprint('ID :' + str(user))
##        userd = alld[user]
##
##        for item in userd:
##            itemd = userd[item]
##
##            if type(itemd).__name__=='string':
##
##            if type(itemd).__name__=='dict':
##                for i in itemd:
##                    safeprint(i)
##                    safeprint(itemd[i])
##            else
##                safeprint(item)
##                safeprint(itemd)
