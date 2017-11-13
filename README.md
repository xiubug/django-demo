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

#### 创建项目步骤

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

#### 创建应用步骤

    1、打开命令行，进入项目中manage.py同级目录
    2、命令行输入：python manage.py startapp blog
    3、添加应用名到setting.py中的INSTALLED_APPS里
    
#### 项目目录结构

    migrations
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
 
migrations：数据移植（迁移）模块，内容自动生成

admin.py：该应用的后台管理系统设置

apps.py：该应用的一些配置，Django-1.9以后自动生成

models.py：数据模块，使用ORM框架，类似于结构中的Models（模型）

tests.py：自动化测试模块，Django提供了自动化测试功能，在这里编写测试脚本（语句）

views.py：执行响应的代码所在模块，代码逻辑处理的主要地点，项目中大部分代码均在这里编写
    