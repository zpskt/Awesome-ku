# Tools
一些实用工具的记录
tools_file文件存放一些需要的安装文件
## 说明
### 编写自己的启动服务开机启动
1.新建服务

        sudo nano /etc/systemd/system/npsc.service  
2.编辑  
>[Unit]  
Description=nps Client  
After=network.target  
Wants=network.target  
[Service]  
Type=simple  
ExecStart=/home/pi/homeassistant/config/nps_client/ npc -server=IP:8012 -vkey=123456asdkj  
[Install]  
WantedBy=multi-user.target  
3.开机启动服务，启动服务  

    sudo systemctl  enable npsc.service  #开机自动运行
     
    sudo systemctl start npsc.service  
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



