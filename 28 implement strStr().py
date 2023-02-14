haystack = "aaaaa"
needle = "bba"

if needle in haystack:
    # a=haystack.__getitem__(needle)
    # print(a)
    # a=haystack.index(needle)
    # print(a)
    b=haystack.find(needle)
    print(b)
else:
    print("-1")
    # c=haystack.startswith(needle)
    # print(c)
    # haystack.__getitem__(needle)
    # haystack.__init__(needle)
    # d=haystack.__getattribute__(needle)
    # print(d)
