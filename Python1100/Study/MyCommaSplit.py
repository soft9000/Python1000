# File: MyCommaSplit.py

data = []
data.append("John Doe, 1235 Fifth Ave., 813-318-9999")
data.append("Mr. Goober, 8712 Main Street, 415-514-9999")
data.append("Prof. Nagy, 105 Baker Street, 742-427-9999")
data.append("Doctor Quote, 666 Social Security Lane, 781-187-9999")

ss = 0
for line in data:
    fields = line.split(',')
    if(len(fields) != 3):
        print("Field Error!")
    else:
        ss = ss + 1
        print(str(ss) + ".) " + fields[2])


