from os import strerror

#Look at the code in the editor. Let's analyze it:
#
#    - first, we initialize bytearray with subsequent values starting from 10; if you want the file's contents to be clearly readable, replace 10 with something like ord('a') - this will produce bytes containing values corresponding to the alphabetical part of the ASCII code (don't think it will make the file a text file - it's still binary, as it was created with a wb flag);
#    - then, we create the file using the open() function - the only difference compared to the previous variants is the open mode containing the b flag;
#    - the write() method takes its argument (bytearray) and sends it (as a whole) to the file;
#    - the stream is then closed in a routine way.
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
#Let's analyze it:
#
#    - first, we open the file (the one you created using the previous code) with the mode described as rb;
#    - then, we read its contents into the byte array named data, of size ten bytes;
#    - finally, we print the byte array contents - are they the same as you expected?

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


# ################################################################

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

