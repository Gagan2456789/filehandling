print('print')
f=open('test.txt', 'r+')
f.write("hello")
f.writelines (["gagan\n", "gurjot\n", "gurlirat\n"])
# print(f.read())
f.close()
t=open('test1.txt', 'r')
# print('char', t.read())  
l=t.readlines()
for x in 1:
    print(x)
