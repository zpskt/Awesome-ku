# 绘图知识  
### Pycharm绘图
[csdn参考链接](https://blog.csdn.net/weixin_51740371/article/details/109555345)        
绘图文件夹  
demo1.py是绘图demo代码，simhei.zip是中文包。
Mac端会出现中文乱码问题，解决如下  
>import matplotlib  
>print (matplotlib.matplotlib_fname()) # 将会获得matplotlib配置文件  
>\#我的是在"/Library/Python/3.8/site-packages/matplotlib/mpl-data/matplotlibrc  
> 解压中文包得到一个ttf文件,复制文件到"/Library/Python/3.8/site-packages/matplotlib/mpl-data/fonts/ttf
文件夹里面   
> cd ~   
> ls -a  
> cd .matplotlib  && rm fontlist-v330.json  
> 重启pycharm搞定

在当前文件夹中，我放置了一些绘图示例代码，主要包括：  
1. 准确率画图
2. 数据处理绘图  
3. 同一画布画多图  
4. 画局部放大图  
5. 读取csv数据  