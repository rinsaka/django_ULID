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
