浏览器　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　后台　

http协议　　　　　　　request            　httpserver        后端服务程序　

tcp 传输　　　　　　　　　　　　　　　　　　　　　　　　　　　　　接收http请求　　　　　　　　业务逻辑处理

tcpip模型　　　　　　　　　　　　　　　　　　　　　　　　　　　　解析请求　　　　　　　　　　　静态文件调用

　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　（得到数据　　　　　　　　　　　　　　　　　回传数据给httpserver
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　组织响应）


httpserver

前台　　　　　前段　　　　　　客户端　　　　用户端　

功能：提供给用户直接使用

要求：　良好的用户体验
　　　　　　更全面的交互功能
　　　　　　很好的和后端进行数据交互
　　　　　　有良好的跨平台性
　　　　　　有一定的优化



后台　　　　　后端　　　　　　　服务端　

功能：　逻辑处理
　　　　　　算法实现
　　　　　　磁盘交互（数据库　静态文件处理）
要求：　健壮性，安全性
　　　　　　并发性能和处理速度
　　　　　　架构合理便于维护扩展



网站后端　

httpserver + WebFrame 

http3.0 : 


　　　　httpserver 
　　　　　　　　　获取http请求　　
　　　　　　　　　解析http请求　
　　　　　　　　　将数据发送给WebFrame
    　　　　　从WebFrame接收反馈数据
        　将数据组织为Response格式发送给客户端
 
    WebFrame:
        从httpserver接收具体请求
        根据请求进行逻辑处理和数据处理
        *静态页面
        *逻辑数据
        将需要的数据反馈给httpserver
　　　　
　　　　升级点　：　１　采用httpserver和应用处理分离的模式
　　　　　　　　　　　　　２　降低了耦合度
　　　　　　　　　　　　　３　原则上httpserver可以搭配任意的WebFrame




项目结构:

                  httpserver  --httpserver.py(主程序)相当于第二个版本的代码　功能处理在这里处理
                  |           --settings(httpserver配置)　　　让用户通过配置文件配件
                  |
                  |
                  |
                  |
                  |           static(存放静态网页的文件夹)
　　　　　　　project -- WebFrame     views.py (应用处理程序)
                               urls.py(存放路由)
                               settings(框架配置)
                               WebFrame.py(主程序代码)


python 自带httpserver 

from http.server import BaseHTTPRquestHandler,HTTPServer

通过这个可以完成简单的httpserver


