from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 100 + i

try:
    bf = open('C:\\Users\\olly1215\\Desktop\\file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Your code that reads bytes from the stream should go here.
data = bytearray(10)

try:
    bf = open('C:\\Users\\olly1215\\Desktop\\file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

print("\n")

try:
    bf = open('C:\\Users\\olly1215\\Desktop\\file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

