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
  
    1、manage.py：项目管理器，与项目进行交互的命令行工具集入口，执行 python manage.py 来查看所有命令
    
    启动服务命令
    ```javascript
    $ python manage.py runserver
    $ python manage.py runserver 9999 
    ```
    
    2、myblog目录：项目的一个容器，包含项目最基本的一些配置，目录名称不建议修改
    
    3、wsgi.py：WSGI（Web Server Gateway Interface）中文名：Python服务器网关接口 Python应用与Web服务器之间的接口
    
    4、urls.py：URL配置文件，Django项目中所有地址（页面）都需要我们自己去配置其URL
    
    5、settings.py：项目的总配置文件，里面包含了数据库、Web应用、时间等各种配置
    
    6、__init__.py: Python中声明模版的文件，内容默认为空

#### 创建应用步骤

    1、打开命令行，进入项目中manage.py同级目录
    2、命令行输入：python manage.py startapp blog
    3、添加应用名到setting.py中的INSTALLED_APPS里
    
#### 应用目录结构

    migrations
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
 
    1、migrations：数据移植（迁移）模块，内容自动生成
    
    2、admin.py：该应用的后台管理系统设置
    
    3、apps.py：该应用的一些配置，Django-1.9以后自动生成
    
    4、models.py：数据模块，使用ORM框架，类似于结构中的Models（模型）
    
    5、tests.py：自动化测试模块，Django提供了自动化测试功能，在这里编写测试脚本（语句）
    
    6、views.py：执行响应的代码所在模块，代码逻辑处理的主要地点，项目中大部分代码均在这里编写
    
#### 创建第一个页面（响应）

编辑blog.views

    1、每个响应对应一个函数，函数必须返回一个响应
    2、函数必须存在一个参数，一般约定为request
    3、每一个响应（函数）对应一个
    
编辑urls.py
    
    1、每个URL都以url的形式写出来
    2、url函数放在urlpatterns列表中
    3、url函数三个参数：URL（正则），对应方法，名称
    
### 第一个Templates

第二种URL配置：包含其他URL
    
    1、在根urls.py中引入include
    2、在APP目录下创建urls.py文件，格式与根urls.py相同
    3、根urls.py中url函数第二个参数改为include('blog.urls')
    
注意事项：
    
    1、根urls.py针对APP配置的URL名称，是该APP所有URL的总路径
    2、配置URL时注意正则表达式结尾符号$和/
    
#### 什么是Templates？(Templates介绍)

    1、HTML文件
    2、使用了Django模板语言(Django Template Language, DTL)
    3、可以使用第三方模板(如Jinja2)
    
    
#### 开发Templates步骤

    1、在APP的根目录下创建名叫Templates的目录
    2、在该目录下创建HTML文件
    3、在views.py中返回render()
    
#### DTL初步使用

    1、render()函数中支持一个dict类型参数
    2、该字典是后台传递到模板的参数，键为参数名
    3、在模板中使用{{参数名}}来直接使用
    
#### Django查找Template

    1、Django按照INSTALLED_APPS中的添加顺序查找Templates
    2、不同APP下Templates目录下的同名.html文件会造成冲突
    
#### 解决Templates冲突方案
    
    1、在APP的Templates目录下创建以APP名为名称的目录，将html文件放入新创建的目录下
    
    
### Models

#### Django中的Models是什么？

    1、通常，一个Model对应数据库的一张数据表
    2、Django中Models以类的形式表现
    3、它包含了一些基本字段以及数据的一些行为
    
#### ORM
    
    1、对象关系映射(Object Relation Mapping)
    2、实现了对象和数据库之间的映射
    3、隐藏了数据访问的细节，不需要编写SQL语句
    
#### 编写Models步骤

    1、在应用根目录下创建models.py，并引入models模块
    2、创建类，继承models.Model，该类即是一张数据表
    3、在类中创建字段
    
#### 字段创建
    
    1、字段即类里面的属性(变量)，如attr = models.CharField(max_length=64)
    
[参考链接](https://docs.djangoproject.com/en/1.11/ref/models/fields/)

#### 生成数据表步骤

    1、命令行中进入manage.py同级目录
    2、执行python manage.py makemigrations app名(可选)
    3、再执行python manage.py migrate
    
#### 生成数据表查看

    1、Django会自动在app/migrations/目录下生成移植文件
    2、执行python manage.py sqlmigrate 应用名 文件id 查看SQL语句
    
#### 生成数据表查看并编辑db.sqlite3

    1、使用第三方软件 SQLite Expert Personal 轻量级、完全免费
    
#### 页面呈现数据后台步骤

    1、views.py中import models
    2、article = models.Article.objects.get(pk=1)
    3、render(request, page, {'article': article})
    
#### 页面呈现数据前端步骤

    1、模板可直接使用对象以及对象的"."操作，如
    
    