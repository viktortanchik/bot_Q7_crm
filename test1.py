import csv
from db import *



names= '/test1/test2/test3/test4/test5/test6'
name=[]
tempname=''
for i in names:
    if i !='/':
        tempname+=i

    else:
        name.append(tempname)
        tempname = ''


print(name)



# myData = ('real_name', 'username', 'user_id', 'chat', 'agency', 'payid', 'strikes', 'hyperlink', 'tag', 'notes',
#           'wallet', 'cash_out')
# temp_db = get_all(con)
#
# myFile = open('db.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerow(myData)
#     for i in temp_db:
#         print(i[1:])
#         writer.writerow(i[1:])


