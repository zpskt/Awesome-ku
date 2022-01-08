# Tools
一些实用工具的记录
tools_file文件存放一些需要的安装文件
## 说明
### 内网穿透  
项目地址：https://github.com/ehang-io/nps/releases  
1.服务端安装  

        tar -zxvf linux_amd64_server.tar.gz
        cd nps
        nohup ./nps start/ &  
之后访问 [服务器 IP]:8080，登录 web 页面。默认用户名 admin，密码 123  
2.客户端安装，树莓派看系统是多少位的，就用多少位的nps  

        tar -zxvf linux_amd64_client.tar.gz
        cd nps
        ./npc -server=xxx.xxx.xxx.xxx:8024 -vkey=hxxxxx4hzc -type=tcp  

登陆服务端的web管理就可以看到你的vkey是多少以及快捷连接命令了



