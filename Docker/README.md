# Docker相关  
## 常用容器  
1. mysql  
/opt/mysql是本机挂载  
   
        docker run -p 3306:3306 -v /opt/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password --name mysql -d mysql:5.7
设置外部可访问

    docker exec -it mysql bash
    mysql -uroot -ppassword  
    grant all privileges on *.* to 'root'  
2. portainer  
                
        docker run -d -p 9000:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock --name portainer  docker.io/portainer/portainer

3.FATE  
        自己设置version

        export version=1.7.0 
        docker run -d --name standalone_fate -p 8080:8080 federatedai/standalone_fate:${version};
4.nginx  

    sudo docker run --name some-nginx -d -p 8080:80 -v $PWD/www:/www -v $PWD/conf/nginx.conf:/etc/nginx/nginx.conf -v $PWD/logs:/wwwlogs registry.docker-cn.com/library/nginx

ps:挂载规则，还有nginx配置文件自己看
#