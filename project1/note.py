pip的使用

作用：　管理python的标准第三方库中第三方软件包

sudo apt-get install

常用命令:
        安装软件: pip3 install package 

        e.g.  sudo pip3 install ssh



查看当前python软件包 pip3 list 

搜索某个名字的python包　　　pip3 search [name]

查看软件包信息　：　pip3 show [package]

卸载软件包　　sudo pip3 uninstall [package]

导出软件包安装环境　　　pip3 freeze > requirements.txt

根据文档自动安装　　　pip3 install -r requirements.txt


PDB调试方法
　
标准库模块　import pdb 


通过pdb模块完成调试功能

*python3 -m pdb 程序　直接进入调试

功能 ： 断点设置，单步运行，函数查看，代码段查看，变量值查看

break ， b   设置断点　　b 77　在代码77行打上断点　　ｃ是继续运行到下一个断点
continue ，c   继续执行　　　
list ， l   查看当前要运行代码段
next， n   单步执行 
step，  s   进入函数单步执行 函数运行情况
pp  打印变量值　　只显示执行过的变量
help  帮助
exit 退出pab调试

pdb.set_trace()
功能 ： 设置初始断点，开始进入pdb调试模式

以pdb调试模式运行
python3 -m pdb dict_client.py
