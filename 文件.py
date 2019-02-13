1.
Http协议？
Http协议就是一个传输数据格式。

我原来学习django框架，从socket服务端开始学起。
自己创造了一个socket服务器来充当：网站。
浏览器当socket客户端。
更清楚的明白到底http协议是什么？
- 请求头
请求头
- 响应头
响应头

一次请求响应后，断开连接（无状态、短连接）。
2.
常见请求头
- Content - Type
- User - Agent
- referer，可以做图片防盗链。
- Host
- cookies

5.
常见的请求方法：
- GET / POST / DELETE / PUT / PATCH / OPTIONS
6.
常见的状态码：
- 200
- 301 / 302
- 403 / 404
- 500

3.
常见的请求体？
Form表单提交：
POST / index
http1
.1\r\nhost: www.luffycity.com...\r\n\r\nusername = alex & password = 123 & ...
Ajax请求：
POST / index
http1
.1\r\nhost: www.luffycity.com...\r\n\r\nusername = alex & password = 123 & ...
POST / index
http1
.1\r\nhost: www.luffycity.com...\r\n\r\n
{“username”:"alex", "password": 123}

补充：django中获取请求体
- request.POST
- request.body

4.
django请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
- wsgi, 他就是socket服务端，用于接收用户请求并将请求进行初次封装，然后将请求交给web框架（Flask、Django）
- 中间件，帮助我们对请求进行校验或在请求对象中添加其他相关数据，例如：csrf、request.session
- 路由匹配
- 视图函数，在视图函数中进行业务逻辑的处理，可能涉及到：orm、templates = > 渲染
- 中间件，对响应的数据进行处理。
- wsgi, 将响应的内容发送给浏览器。

WSGI协议是什么：
　　　　        WSGI(Web
Server
Gateway
Interface)：Web服务器网关接口。是Python中定义的服务器程序和应用程序之间的接口。
　　        2.
作用：
　　　　        可以很好使web框架与Web服务器进行分离。也就是说服务器只管与客户端连接，而具体的业务逻辑代码由框架来完成！这样他们就可以各司其职了
实现该协议的模块：
- wsgiref
- werkzurg
- uwsig

5.
中间件
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出
- 5
个方法
在请求阶段：两个钩子可用
process_request()
process_view()

在响应阶段，在调用视图之后，中间件从下往上以相反的顺序应用。三个挂钩可供选择：
process_exception() （只有当视图引发异常时）
process_template_response() （仅适用于模板响应）
process_response(）
- 应用场景：
- 登录认证，不再需要在每个函数中添加装饰器
       - 权限，当用户登录时候获取当前用户所有权限并放入session，然后再次访问其他页面，获取当前url并在session中进行匹配。如果没有匹配成功，则在中间件返回“无权访问”
- 跨域，
- jsonp，动态创建一个script标签。
- cors，设置响应头
应用：本地开始前后端分离的时使用。
6.
视图
- FBV
url - 函数
用户发送url请求, Django会依次遍历路由映射表中的所有记录, 一旦路由映射表其中的一条匹配成功了,
就执行视图函数中对应的函数名, 这是fbv的执行流程
- CBV
method写的比较多的话可以用CBV
Python是一个面向对象的编程语言，如果只用函数来开发，有很多面向对象的优点就错失了（继承、封装、多态）
所以Django在后来加入了Class - Based - View。可以让我们用类写View。这样做的优点主要下面两种：
1.
提高了代码的复用性，可以使用面向对象的技术，比如Mixin（多继承）
2.
可以用不同的函数针对不同的HTTP方法处理，而不是通过很多if判断，提高代码可读性
url - view
当服务端使用cbv模式的时候, 用户发给服务端的请求包含url和method, 这两个信息都是字符串类型
服务端通过路由映射表匹配成功后会自动去找dispatch方法, 然后Django会通过dispatch反射的方式找

6.
django
rest
framework的作用？
快速搭建基于restful规范的接口。
什么是接口？
- URL \
- 约束我原来学习DJANG777777777框架，从socket服务端开始学起。
补充：DJANG777777777中获取请求体
DJANG777777777请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变DJANG777777777的输入与输出
DJANG777777777
我原来学习django框架，从socket服务端开始学起。
补充：django中获取请求体
django请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出
django
我原来学习django框架，从socket服务端开始学起。
补充：django中获取请求体
django请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出
django
我原来学习django框架，从socket服务端开始学起。
补充：django中获取请求体
django请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出
django
我原来学习django框架，从socket服务端开始学起。
补充：django中获取请求体
django请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出
django
我原来学习django框架，从socket服务端开始学起。
补充：django中获取请求体
django请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出
django
我原来学习django框架，从socket服务端开始学起。
补充：django中获取请求体
django请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出
django
我原来学习django框架，从socket服务端开始学起。
补充：django中获取请求体
django请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出
django
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
我原来学习aaaaaaaaaa框架，从socket服务端开始学起。
补充：aaaaaaaaaa中获取请求体
aaaaaaaaaa请求生命周期 - --> >> url - --wsgi - --中间件 - --视图 - --拿数据模板渲染后 - --中间件 - --wsgi返回
是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变aaaaaaaaaa的输入与输出
aaaaaaaaaa
