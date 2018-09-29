import re 
import sys 

# p = 'this is a number 23564-235-22-423'

# r=re.match(r'.+(\d+-\d+-\d+-\d+)',p)
# a=r.group()
# print(a)

# p = r'\d+\.\d+\.\d+\.\d+\/\d*\b'
# regex = re.compile(p)
# p = open('1.txt')

# L=[]
# def bvi():
#     global L
#     for i in p:
#         try: 
#             L += regex.findall(i)
#         except:



# data = input('请输入')
# if data == 'BVI1':
#     bvi()

# print(L)

def get_address(port):
    f = open('./1.txt')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line 
            else:
                break
        # print(data)
        if not data:
            break#获取字段　 
        try:
            PORT = re.match(r'\S+',data).group()
            # print(PORT)
        except Exception as e:
            print(e)
            continue
        if PORT == port:
            p = r'address is (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d+|Unknown)'
            addr = re.search(p,data).group(1)
            return addr






if __name__ == '__main__':
    port = sys.argv[1]
    print(get_address(port))














# f = open('text.txt')
# p = r'[A-Z]\w*'
# l=[]
# for line in f:
#     l　+= re.findall(p,line)
# print(l)

# r'-?\d+\.?/?\d*%?'

