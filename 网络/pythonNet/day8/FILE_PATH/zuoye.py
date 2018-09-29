    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self):
        #获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send('文件库为空'.encode())
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)

        files=''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH+file):
                files = files + file + '#'
        self.connfd.sendall(files.encode())

    def do_get(self,filename):
        try:
            fd = open(FILE_PATH + filename,'rb')
        except:
            self.connfd.send('文件不存在'.encode())
            return
        self.connfd.send(b'ok')
        time.sleep(0.1)
        #发送文件
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        print('文件发送完毕')

    def do_put(self,filename):
        self.connfd.send(b'ok')
        print('正在接收')
        time.sleep(1)
        p = open(FILE_PATH+filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            p.write(data)
        p.close()
        print('接收完毕')