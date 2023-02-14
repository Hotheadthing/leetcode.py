emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
changer = ""

for i in range(len(emails)):
    for j in range(len(emails[i])):
        if emails[i][j] == "+":
            x = (emails[i].index("+"))
