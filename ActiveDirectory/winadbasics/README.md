# IP 
10.10.20.191

### Changing password of a user with Delegate Control
- Delegate Control is a control in which a person can change password of an user, without Domain admin permissions

` Set-ADAccountPassword <USERNAME> -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose`
- In our case 

```console
PS C:\Users\phillip> Set-ADAccountPassword sophie -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose
New Password: **********                                                                                                    
VERBOSE: Performing the operation "Set-ADAccountPassword" on target "CN=Sophie,OU=Sales,OU=THM,DC=thm,DC=local".
```
