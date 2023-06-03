# XSS

### Enter an URL ( including parameters ) of an endpoint that is vulnerable to XSS

<details>
<summary><b>Answer</b></summary>
<b>http://marketing.nahamstore.thm/?error=</b>
</details>

- Add `<IP>    nahamstore.thm` to `/etc/hosts` 
- Start `wfuzz` to enumerate subdomains on the machine

![wfuzz screenshot](https://raw.githubusercontent.com/divu050704/assets-holder/77a4b39666cec823c7f07b707617bdac52363577/tryhackme-screenshots/Screenshot%202023-06-01%20195740.png)

- Found 3 interesting subdomains `marketing`, `shop`, `stock`. 
- Added these to `/etc/hosts`.
- Scan `marketing.nahamstore.thm` for directories using `gobuster`, but didn't find anything interesting.
- Tried changing campaign URL by a single alphabet and got an error as campaign not found.
- Tried escaping error `Campaingn not found` and found XSS. 

![screenshot for XSS on marketing subdomain](https://raw.githubusercontent.com/divu050704/assets-holder/cf988af4bfda7f9d7b674ec3c7aeeb465e6d75bb/tryhackme-screenshots/Screenshot%202023-06-01%20201355.png)

### What HTTP header can be used to create a Stored XXS

<details>
<summary><b>Answer</b></summary>
<b>User-Agent</b>
</details>

- On `shop.nahamstore.thm`, we can add `XSS` to User-Agent while placing order. 

![XSS on order page with burbsuite](https://raw.githubusercontent.com/divu050704/assets-holder/aead568a3a87fd21d51e16d407f024f350240fb7/tryhackme-screenshots/Screenshot%202023-06-01%20202256.png)

- Now go to My Orders page and check the latest order.

![screenshot for XSS confirmation on orders page](https://raw.githubusercontent.com/divu050704/assets-holder/a6cee254bf3d72a294b5a8bfdf29162a6c024f30/tryhackme-screenshots/Screenshot%202023-06-01%20202507.png)

### What HTML tag needs to be escaped on the product page to get the XSS to work?

<details>
<summary><b>Answer</b></summary>
<b>title</b>
</details>

- On clicking the image of the product we were redirected to the details page which had id and name of the products as parameters. 
- On changing the name parameter, I noticed that the name of the products was directly dependent on this page. 
- Escaped the `<title>` attribute and injected javascript code.

![screenshot for XSS on product page](https://raw.githubusercontent.com/divu050704/assets-holder/0549ec146b910462dc680019937021dac9e8e37b/tryhackme-screenshots/Screenshot%202023-06-01%20203710.png)

### What JavaScript variable needs to be escaped to get the XSS to work?

<details>
<summary><b>Answer</b></summary>
<b>search</b>
</details>

- On the shop subdomain's home page we can see a javascript code for searching products, which seems to vulnerable to code injection.
- Finally added injection and URL encoded it.

![screenshot for XSS on search page](https://raw.githubusercontent.com/divu050704/assets-holder/21323b03b9bbb39272b45920bef3ce880b6bf149/tryhackme-screenshots/Screenshot%202023-06-01%20204533.png)


### What hidden parameter can be found on the shop home page that introduces an XSS vulnerability.

<details>
<summary><b>Answer</b></summary>
<b>q</b>
</details>

- As we have seen above we can get `XSS` from the `q` parameter.


### What HTML tag needs to be escaped on the returns page to get the XSS to work?

<details>
<summary><b>Answer</b></summary>
<b>textarea</b>
</details>

- On the returns page in the return information escape textarea to get XSS.

![screenshot for XSS on the returns page](https://github.com/divu050704/assets-holder/blob/90d595e4925dcb68f95e999bf55002211961491e/tryhackme-screenshots/Screenshot%202023-06-02%20190423.png?raw=true)

- We can see alert in the screenshot below.

![screenshot to confirm XSS on return page](https://raw.githubusercontent.com/divu050704/assets-holder/90d595e4925dcb68f95e999bf55002211961491e/tryhackme-screenshots/Screenshot%202023-06-02%20190435.png)


### What is the value of the H1 tag of the page that uses the requested URL to create an XSS


<details>
<summary><b>Answer</b></summary>
<b>Page Not Found</b>
</details>


### What other hidden parameter can be found on the shop which can introduce an XSS vulnerability


<details>
<summary><b>Answer</b></summary>
<b>discount</b>
</details>

- On the products page while ordering I captured an empty parameter, named `discount`, which is directly dependent on the value hidden parameter of discount on the page. 

![burpsuite screenshot](https://raw.githubusercontent.com/divu050704/assets-holder/891a8b139303de6e6195da9c01f612f93a0e5cac/tryhackme-screenshots/Screenshot%202023-06-03%20204104.png)

- We can confirm this by adding this parameter to the URL.

![screenshot for the GET testing](https://github.com/divu050704/assets-holder/blob/af0cb6dcd9b20dc006d55451e15eb1f666f1fdad/tryhackme-screenshots/Screenshot%202023-06-03%20204400.png?raw=true)

```html
<div style="margin-bottom:10px"><input placeholder="Discount Code" class="form-control" name="discount" value="random"></div>
```

- In the above code snippet we can see, we can escape this HTML code with `"` .

- Added `onfocus` parameter with code to run custom javascript code.

![Screenshot for code injected](https://raw.githubusercontent.com/divu050704/assets-holder/af0cb6dcd9b20dc006d55451e15eb1f666f1fdad/tryhackme-screenshots/Screenshot%202023-06-03%20204706.png)


