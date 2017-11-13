# django-demo
django基础教程，由浅入深，一步一步学习django，最后学到的不单单是基础！

### 环境搭建

#### 准备环境

    1、Python
    2、Django
    3、开发工具
    
#### 安装Python

    1、Windows:Python官网下载对应是MSI安装文件
    2、MAC及Linux自带Python，无需安装

#### 安装Django

    1、命令行安装
    ```javascript
    $ pip install Django==1.11.7
    
    ```
    
    2、源码安装
    ```javascript
    下载源码，进入根目录执行python setup.py install
    ```

[参考链接](https://www.djangoproject.com/download/)

安装完查看版本号
```javascript
$ python -m django --version
```

#### 开发工具

    1、PyCharm(推荐)
    2、Sublime Text
    3、Atom

### 创建项目及应用

#### 创建步骤

    1、打开命令行，进入想要安置项目的目录
    2、命令行输入：django-admin startproject myblog，若没有报错，则创建项目成功
    
#### 项目目录结构

    manage.py
    myblog
        __init__.py
        settings.py
        urls.py
        wsgi.py
  
manage.py：项目管理器，与项目进行交互的命令行工具集入口，执行 python manage.py 来查看所有命令

启动服务命令
```javascript
$ python manage.py runserver
$ python manage.py runserver 9999 
```

myblog目录：项目的一个容器，包含项目最基本的一些配置，目录名称不建议修改

wsgi.py：WSGI（Web Server Gateway Interface）中文名：Python服务器网关接口 Python应用与Web服务器之间的接口

urls.py：URL配置文件，Django项目中所有地址（页面）都需要我们自己去配置其URL

settings.py：项目的总配置文件，里面包含了数据库、Web应用、时间等各种配置

__init__.py: Python中声明模版的文件，内容默认为空