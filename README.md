# py-webkit2png-flask-api

This is a API project that takes in a URL and returns a screenshot (*png format*) of the website.

## Features

  1. Image caching
  2. Fast! Does not wait for page to fully load, you can stop it anytime and grab the image of what's loaded

## Manual installation

  1. `git clone https://github.com/kloudsec/py-webkit2png-flask-api.git`
  2. `virtualenv v_env`
  3. `pip install -r requirements.txt`
  4. `./manage run` - To run on debug mode
  5. `./manage run_standalone` - To run on production

## Fast deployment

  1. `docker pull nubelacorp/py-webkit2png-flask-api`
  2. `docker run -p 8080:80 -it nubelacorp/py-webkit2png-flask-api`


## Usage

`curl http://<HOST>?<PARAMS>`

Params available are:

  * **url (required)** - URL of the website you want to screenshot
  * **width (default:400)** - Width of website window to grab screenshot from
  * **height (default:400)** - Height of website window to grab screenshot from
  * **scale (default:0.5)** - Scale of screenshot relative to the browser window. For example. If your screenshot is 400x400, at a scale of 0.5, the actual browser will be of 800x800 large.
  * **timeout (default:-1)** - If set to -1, the API uses a smart loading scheme by which it'll poll the browser for a screenshot that isn't blank, and then wait another 2 seconds and then return that screenshot. Otherwise, you can set your own timeout seconds. If you specify your own timeout, the timer begins from the moment the initial page request begins, and does not use the smart polling method. For example, if you declare 5s, it'll return the screenshot 5 seconds after the page is requested.
  
  
Some examples:

* `http://localhost:8080/?url=https://getgom.com`
* `http://localhost:8080/?url=https://getgom.com&width=300&height=250&scale=0.25&timeout=7`