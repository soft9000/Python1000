
import array
data = array.array('b')

print(data)

zbytes = b'123'
data.append(zbytes[0])
data.append(zbytes[1])
data.append(zbytes[2])

data.append(b'ABC'[0])

print(data)

data = array.array("b", b"Bizinga")
print(data)


data.append("Badinga")
