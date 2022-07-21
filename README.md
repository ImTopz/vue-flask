# 全栈开发

# 1.后端基础（python-flask）

```python
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('hello.html', result = dict)
if __name__ == '__main__':
   app.run(debug = True)
```

基础代码

### 从flask中通过模板返回html代码

```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
   return render_template(‘hello.html’)  #会从templates目录下寻找 hello.html
if __name__ == '__main__':
   app.run(debug = True)
```

render_template函数，开发人员在开发flask的过程中，如果使用jinga2的引擎，应当注意避免SSTI漏洞

相关漏洞学习网站如下 

```URL
https://morblog.cc/posts/2946623354/
```

   **Jinga2**模板引擎使用以下分隔符从HTML转义。 

-   控制结构： {％...％}用于语句 
-   变量取值： {{...}}表达式可以打印到模板输出 
-   注释：  {＃...＃}用于注释未包含在模板输出中 
-   ＃... ##用于行语句 

```html
<html>
   <head>
      <script type = "text/javascript"
         src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
   </head>
   <body>
      <input type = "button" onclick = "sayHello()" value = "Say Hello" />
   </body>
</html>
```

这里的input type是button,按钮，onclik则是按钮触发后触发的函数，这段代码的解析需要具有html和js的一般基础。

### 页面form提交跳转

``` 
在以下示例中， '/' URL呈现具有表单的网页（student.html）。 填充的数据将发布到'/result' result'URL，触发result()函数。 
```

code

```python
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def student():
   return render_template('student.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
if __name__ == '__main__':
   app.run(debug = True)
```

```html
<html>
   <body>
      <form action = "http://localhost:5000/result" method = "POST">
         <p>Name <input type = "text" name = "Name" /></p>
         <p>Physics <input type = "text" name = "Physics" /></p>
         <p>Chemistry <input type = "text" name = "chemistry" /></p>
         <p>Maths <input type ="text" name = "Mathematics" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>
```

html代码解析:

<form大标签 action表示输入表单后提取到的入口页面，表示提交的form表单会根据post的方法送到http://localhost:5000/result这个页面中。同时观察后端处理代码，后端检测了访问的方法，如果是POST的话，就获取表单并且把结果赋给result再return给result.html

```
<form action="form_action.asp" method="get">
 <p>这里输名字: <input type="text" name="fname" /></p>
 <p>接着输名字: <input type="text" name="lname" /></p>
 <input type="submit" value="Submit" />
</form>
```

比如说这里的话就会把页面送到form_action.asp页面。





