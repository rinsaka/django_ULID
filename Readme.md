# Django の ID を ULID にするプロジェクト
## 参考
- https://qiita.com/ykiu/items/c288b99d0a1956e8ac9f

## ulid パッケージのインストール

~~~
rinsaka@iMac2013 django_ULID % pip list | grep ulid
rinsaka@iMac2013 django_ULID % pip install ulid-py
Collecting ulid-py
  Downloading ulid_py-0.0.12-py2.py3-none-any.whl (16 kB)
Installing collected packages: ulid-py
Successfully installed ulid-py-0.0.12
rinsaka@iMac2013 django_ULID % pip list | grep ulid
ulid-py                            0.0.12
rinsaka@iMac2013 django_ULID %
~~~

## Shell で使ってみる

~~~
rinsaka@iMac2013 django_ULID % python manage.py shell
Python 3.7.5 (default, Oct 25 2019, 10:52:18)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.12.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import ulid

In [2]: ulid.new()
Out[2]: <ULID('01E433FX8J7WZCCJCZDA8NGJNY')>

In [3]: ulid.new()
Out[3]: <ULID('01E433FZB9XGPZSKKG43Z10RCS')>

In [4]: ulid.new()
Out[4]: <ULID('01E433G9RHS2PY5JN8WFWGFHQ7')>

In [5]: exit
rinsaka@iMac2013 django_ULID %
~~~