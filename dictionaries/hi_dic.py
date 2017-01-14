import datetime

user = {"name": "murthy",
        "twitter": "https://twitter.com/murthyAvanithsa",
        "email":"murthy_avsn@tecnis.com",
        "dob":datetime.date(1987, 7, 7),
        }

# get all keys

print user.keys()

# search for  a key in dic
print "name" in user

# get all the values
print user.values()