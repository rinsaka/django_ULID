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

## Shell でモデルを登録してみる

~~~
rinsaka@iMac2013 django_ULID % python manage.py shell
Python 3.7.5 (default, Oct 25 2019, 10:52:18)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.12.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from comments.models import Comment

In [2]: c = Comment(title="Title", body="Body of comment")

In [3]: c.save()

In [5]: c.id
Out[5]: <ULID('01E435WX3CE5WAT6MS9BQ8MT4B')>

In [6]: c = Comment(title="Second comment", body="How to use ULID")

In [7]: c.save()

In [8]: c.id
Out[8]: <ULID('01E435YE56ETV25PB2B64170NQ')>

In [9]: exit()
rinsaka@iMac2013 django_ULID %
~~~


## DB で確認

~~~
rinsaka@iMac2013 django_ULID % sqlite3 db.sqlite3
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> .tables
auth_group                  comments_comment
auth_group_permissions      django_admin_log
auth_permission             django_content_type
auth_user                   django_migrations
auth_user_groups            django_session
auth_user_user_permissions
sqlite> select * from comments_comment;
01E435WX3CE5WAT6MS9BQ8MT4B|Title|Body of comment|2020-03-23 16:49:51.385305|2020-03-23 16:49:51.385333
01E435YE56ETV25PB2B64170NQ|Second comment|How to use ULID|2020-03-23 16:50:39.357332|2020-03-23 16:50:39.357354
sqlite> .exit
rinsaka@iMac2013 django_ULID %
~~~
