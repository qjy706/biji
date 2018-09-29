git 代码协同工具

svn git

代码管理工具　
* 防止代码丢失，做备份　
* 代码版本的管理，可以进行多个节点的备份，在多个版本之间跳跃
*　可以方便的将代码在多人之间进行共享传输　
* 多人开发时有各种模式可以方便代码管理

什么是git
git是一个开源的分布式版本控制系统，可用于高效的管理大小项目．

分布式和集中式

分布式: 每个节点都保存完成的代码，没有明确的中央服务器，节点之间相互推送下载代码完成代码共享
集中式：代码集中管理，每次完成的代码上传到中央管理器，然后再统一从中央管理器下载代码使用（保密性强，但下载慢，


git特点：　
*git 可以管理各种文件，特别是代码项目，多在*nix系统中使用
*　是分布式管理，不同于集中式，这是git和svn的核心区别　
* git可以更好的支持分支，方便多人协同工作
* git分布式代码更安全，有全球唯一的commit版本号　
* git是一个开源的系统
* 使用git可以脱网工作，且数据传输速度较快

git安装　

linux : sudo apt-get install git 
windows : msysgit.github.io


git 配置命令　

git config 

配置级别：
　　　１．　系统中所有用户都使用该配置
　　　　　　　　命令：　git config  --system
　　　　　　　　配置文件：　/etc/gitconfig 

　　　２．　当前用户可以使用该配置　
　　　　　　　　命令：　git config  --global
        配置文件：　~/.gitconfig

　　　３．　当前项目可使用该配置　
　　　　　　　　命令：　git config
        配置文件：　project/.git/config

配置内容：　

　　　１．配置用户名
　　　　　　　e.g. 配置用户名为qjy 
　　　　　　　 sudo git config --system user.name qjy
cat /etc/gitconfig　　查找用户名　

   2. 配置邮箱　
   　　　　sudo git config --global user.email 1096457847@qq.com　　　当前用户
   　　　　cat ~/.gitconfig

   3. 配置编译器　
   　　　　tarena@tedu:~/桌面/git /kobe$ git init
       初始化空的 Git 仓库于 /home/tarena/桌面/git /kobe/.git/  这个文件夹里面写的所有内容都可以用git进行管理　

       git config core.editor sublime   (必须在git仓库里面写)


查看当前项目配置信息　git config --list 
user.name=qjy
user.email=1096457847@qq.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.editor=sublime

   　　　　　

工作区　程序员自己用的

暂存区　暂时保存工作区的工作状态　暂存区起到记录作用　 add 

本地仓库　存放各个工作节点　 commit

初始化仓库　三个区域就都有了　
git init
*　在某个目录下初始化仓库后会自动产生.git目录，该目录下工作的所有文档既可以使用git进行管理



echo 'this is a git test' > Readme.txt 简单的生成一个文件　(在工作区添加了一个文件) 

如果想存放到本地仓库　
先存放到暂存区　用add
git add file1 file2 (*)等等形式　


查看分支状态　
git status 
*默认工作分支为master 可通过创建新的分支切换　



文件提交　
git add [file]
*将文件提交到暂存区　
*提交内容可以是一个文件，多个文件用空格分开　
*如果是*表示所有文件，也可以是目录　


删除暂存区某个文件提交记录
git rm --cached <文件>.


文件同步到本地仓库
git commit -m'whoisyourdaddy'
*需要在-m后面加一些解释　
*所有对工作区的修改想要添加到本地仓库　，都要先add 之后commit 产生一个新的节点　
[master 9c37f54] 666
 1 file changed, 1 insertion(+)

 9c37f54 是唯一的id 

工作去要先上传到暂存区　add 
之后暂存区　commit到本地仓库



提交日志的查看
　　　　查看commit的日志　
　　　　　git log 

　　　　简单查看日志　
　　　　　git log --pretty=oneline



一些工作区命令　
　　　查看本地文件和工作区差异
　　　git diff file 

   从本地仓库恢复文件　(未提交的内容不能回复)
   git checkout file

   丢弃工作区修改　
   git checkout --file 



本地仓库文件的移动和删除　
   移动文件
   git mv file dir

   删除文件
   git rm file 

   *用法和mv　rm命令相同．操作后直接commit即可工作区和本地仓库同步


版本控制命令

　　　　回到之前版本
　　　　git reset --hard HEAD^　　
　　　　* HEAD后的^数量决定了回到上几个版本

　　　　git reset --hard commit_id（或者标签）
    * 使用commit前7位即可，回到指定的版本　


    去往更新的版本　
    １．查看所有历史版本号
    　　　　git reflog
　　　　2.  使用get reset去往指定版本　
　　　　　* git reflog 会有所有的操作记录　，最新的操作始终在最上面　



标签管理　

什么是标签　：　即在当前工作位置添加快照，保存工作状态，一般用于版本的迭代．

　　　添加标签信息　
　　　

   创建新的标签
       git tag v1.0
       *默认在最新的commit_id添加
       git tag v0.9 [commit_id] 指某一个标签处打标签　
   查看标签　
　　　    git tag    #列出当前标签　
       git show v1.0　　　显示标签具体信息　
   删除标签　
　　　    git tag -d v1.0

　　　去往某个标签版本　
　　　　　　　git reset --hard 标签　



临时工作区操作　：　为了验证方法的好坏　
　　　
    创建保存临时工作区
       git stash
Saved working directory and index state WIP on master: dc220c8 dasd
HEAD 现在位于 dc220c8 dasd


    查看保存的工作区　
    　　　git stash list

stash@{0}: WIP on master: dc220c8 dasd
stash@{1}: WIP on master: dc220c8 dasd
stash@{2}: WIP on master: dc220c8 dasd
最新的在最上面　最老的在最下面　


如果刚刚保存的方法不好　，现在修改　然后继续保存临时工作区　　
发现第二个方法好　

　　　　　应用到哪个工作区　
　　　　　　　git stash apply stash@{index}
　　　　　
　　　　　应用上一个工作区，然后删除掉　
　　　　　　　　git stash pop

     删除工作区　
        git stash clear 　　　删除所有　
        git stash drop stash@{index}  删除某一个　




git 版本控制工具

你有github账号么　
一两个操作问题，分支和远程仓库同步相关
什么是分布式，git有什么特点







分支操作　
　　　什么是分支
　　　　分支即每个人获取原有代码，在此基础上创建自己的工作环境，单独开发，不会影响其他分支的操作．
　　　　开发完成后再统一合并到主线分支中．

　　　创建分支的好处：安全，不影响其他人工作，自己控制进度　
　　　

　　　查看分支　
　　　git branch
     * 前面有*号的分支表示当前正在工作的分支　
   
   创建新的分支　
   git branch [branch_name]

   切换分支　
   git checkout [branch]
   主分支　是 master

   创建并切换到新的分支　
   git checkout -b [branch_name]  在创建的分支基础上创建　


　　　合并分支　
   将某个分支合并到当前分支
   git merge branch_name

   * 合并过程中没有冲突则直接合并后当前分支即为干净的状态　
   * 如果产生冲突则需要人为选择然后再进行add commit操作　
   * 在创建分支前，尽量保证当前分支是干净的，以减少冲突的发生　

   删除分支　
   git branch -d [branch_name]
   * 如果在删除之前没有合并　，则不能用d删除　

   强制删除　
   git branch -D [branch_name]




   分支做的工作不会影响到主分支


远程操作　
   远程仓库　：　远程主机上的仓库，实际上git是分布式的，每一台的git结构都相似，只是把其他主机的git仓库叫做远程而已

   １．创建共享仓库　
   　　　　mkdir gitrepo 
   2. 设置文件夹属主　
   　　　　chown tarena:tarena gitrepo
   3. 将该文件夹设置为可共享的git仓库　
       cd gitrepo
       git init --bare fly.git(项目名称)一般以.git结尾
    4. 将本地仓库属主　
    　　　　chown -R tarena:tarena 项目名称

添加远程仓库　(必须要在git仓库中进行　)
　　　　git remote add origin  
*默认使用SSH作为传输手段　
必须在本地的某个git仓库下执行才能使用本地仓库和远程仓库关联　

删除远程主机　

　　　　git remote rm [origin]
   
将本地分支推送到远程　
　　　git push -u　origin 分支　
　　　
从远程仓库获取项目(不需要连接)
　　　　　clone 
　　　　git clone tarena@127.0.0.1:/home/tarena/桌面/git/gitrepo/fly.git

从远程仓库拉取分支或代码　
　　　直接拉取远程分支和当前工作分支合并
　　　git pull origin Tom

   拉取远程分支到本地，不合并　
   git pull origin　　 Tom 　　　: 　　　　Tom
                   远程分支名称　　　本地分支名称


代码推送和拉取　
　　　将本地代码推送到远程仓库
　　　　　git push 


　　　　　git push --force origin (当本地版本比远程版本旧时用本地旧版本覆盖远程新版本)
　　　　　

   从远程仓库更新代码　
   　　git pull
     git fetch (如果有新的分支拉取到本地不会和本地分之合并)

如果远程仓库版本比你的版本新（假如你觉得你做的不太好回到之前的版本）


删除远程分支
　　　git push  -u  origin :Jame

删除标签
　　　git push  origin --delete tag v1.0



其他获取远程仓库代码命令

　　　获取新的分支和标签
　　　git fetch origin

　　　获取更新的代码
　　　git pull



*在第一次向远程仓库



github

github是一个开源项目社区网站．拥有全球最多的开源项目．
开发者可以注册这个网站建立自己的github仓库，然后就可以在本地通过git像操作远程仓库一样操作github仓库

添加　ssh 秘钥　
　　　１．在本地主机生成ssh秘钥对　
　　　　　　ssh-keygen 
     * 默认秘钥对存放在~/.ssh/　　　　
     *　生成过程会提示设置密码，如果直接回车则表示不设置密码　
  　2. 进入~/.ssh 目录　复制 id_rsa.pub 公钥内容　
  　3. 登录github账号　
  　　　　右上角头像下拉菜单　--> settings --> 左侧  SSH and GPG keys --> new ssh key --> 填写title 
  　　　　将复制内容加入key 文本框　点击add


创建新的github 仓库　
  　右上角　＋　下拉菜单　--> new repository --> 填写参考名和基本描述，根据情况选择是否添加readme等内容
  　选择共有还是私有 --> 点击创建　


操作github仓库
　　　　１　git remote 连接远程github仓库　如果需要输入密码输入github密码即可　
　　　　２　使用git push 等操作远程仓库的方法操作即可


　　　　
　　　




　　　　






