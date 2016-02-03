pupils = [("John", 17), ("Sarah", 19), ("Angie", 23)]

for name, age in pupils:
    if age < 20:
        print ("Hi %s, you are still in school" % name)
    else:
        print ("You are ready for university %s" % name)