# 说明

## 1、安装依赖

安装和redis、mysql交互的驱动

```bash
pip install redis
pip install mysql-connector
```

## 2、使用说明

首先，安装所有依赖模块

```
pip install -r requirements.txt
```

模块demo跑不了的话，请参照这篇解决方案：

<a href="https://github.com/qq20004604/Python3_Django_Demo#842%E5%BC%95%E5%85%A5mysql%E9%A9%B1%E5%8A%A8">8.4.2、引入mysql驱动</a>


然后在需要的地方，引入，并注册你需要的key

```
from kv_manager import c

# 注册key
c.register_key([app.key], [default value][, expire_time=time(s)])

# 示例
# c.register_key('test.foo', 'default foo', expire_time=10)
```

获取值：

```
c.get_value([key])
```

示例：

```
def index(request):
    # return HttpResponse('Home Page')
    return render(request, 'dynamic.html', {
        'foo': c.get_value('foo')
    })
```