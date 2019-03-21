# Hello World！
## 概要

Djangoに初めて触れる方を対象にしたチュートリアルです

Djangoで`Hello World!`と表示するチュートリアルです

## チュートリアル
### Djangoアプリのひな型を作成する

まず、`django-admin startproject helloworld`を実行します

```shell
django-admin startproject helloworld
```

このコマンドで`Django`アプリのひな型を作成することができます

次に、作成した`helloworld`ディレクトリへと移動します

```shell
cd helloworld
```

`py manage.py runserver`を実行すると作成したアプリのローカルサーバが起動します

`localhost:8000`にアクセスすると起動したローカルサーバの画面が表示されます

### Hello World!とブラウザに表示

まず、`helloworld`内に新しいページを作成します

```shell
py manage.py startapp web
```

コマンド実行後、`helloworld`ディレクトリ以下に`web`が作成されています

次に、`helloworld/web/views.py`に`index`アクションを作成します

```python:helloworld/web/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")
```

次に、`helloworld/web/urls.py`を以下のように作成します

```python:helloworld/web/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

その後、`helloworld/helloworld/urls.py`に作成した`web`へのルーティングを追加します

```python:
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include('web.urls')),
]
```

`py manage.py runserver`を実行してローカルサーバを起動します

`localhost:8000/web`にアクセスして`Hello World!`と表示されていればOKです！

