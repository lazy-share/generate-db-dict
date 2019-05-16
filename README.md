# generate-db-dict
自动生成数据库字典


## windows安装

```
1、克隆项目

git clone https://github.com/lazy-share/generate-db-dict.git

2、安装好python3

python下载地址：https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe
下载好之后双击安装。
安装完毕后可以通过python -V查看安装版本情况

3、安装虚拟环境
pip install virtualenv

4、打开cmd命令行，进入generate-db-dict
virtualenv venv

5、激活当前虚拟环境
venv\Scripts\activate.bat

6、安装依赖到当前虚拟环境
pip3 install -r requirements.txt

7、启动
python generate-db-dict.py runserver

8、访问地址
http://127.0.0.7:5000/

```


## linux-centos7安装

```

1、下载python3
进入你平常下载软件tarball目录，执行：
 wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz

2、安装编译依赖包
yum -y install zlib zlib-devel
yum -y install bzip2 bzip2-devel
yum -y install ncurses ncurses-devel
yum -y install readline readline-devel
yum -y install openssl openssl-devel
yum -y install openssl-static
yum -y install xz lzma xz-devel
yum -y install sqlite sqlite-devel
yum -y install gdbm gdbm-devel
yum -y install tk tk-devel
yum -y install libffi libffi-devel

3、解压

tar -xvf Python-3.7.3.tgz

4、编译

cd Python-3.7.3
./configure
make
make install

5、测试安装情况

python3 -V

6、克隆项目

git clone https://github.com/lazy-share/generate-db-dict.git

7、进入项目

cd generate-db-dict

8、安装/创建虚拟环境

pip3 install virtualenv
virtualenv venv

9、激活当前项目虚拟环境

source venv/bin/activate

10、安装依赖到当前虚拟环境

pip3 install -r requirements.txt

11、启动

nohup venv/bin/python3 generate-db-dict.py runserver &

12、访问

http://ip:5000

```

在线演示地址：http://www.laizhiy.cn:8000/


![预览界面](https://github.com/lazy-share/generate-db-dict/blob/master/images/success.png)

## 关注我

![微信公众号](https://github.com/lazy-share/generate-db-dict/blob/master/images/weixin.jpg)
