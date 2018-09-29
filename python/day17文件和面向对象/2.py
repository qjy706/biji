# f=open('qqq.txt','wb')
# while True:
#     a=input('请输入')
#     if not a:
#         break
#     b=a.encode()
#     f.write(b)

# f.close()



f=open('qqq.txt','rb')
f.seek(-16,2)
b=f.read(3).decode()   # b=b'abcd\n1234
print(b)
f.close()