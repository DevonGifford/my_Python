# Web Development with Python

ETA: 5 hours
Reviewed: No
Section: +extra, Section 19
Summary: No
complete: follow-up

Django vs Flask

Django is a big framework

Flask is a micro framework - clean and small

### Virtual Environment

---

[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

[Python Virtual Environments: A Primer – Real Python](https://realpython.com/python-virtual-environments-a-primer/)

[Where in a virtualenv does the custom code go?](https://stackoverflow.com/questions/1783146/where-in-a-virtualenv-does-the-custom-code-go)

# Flask

---

---

[Welcome to Flask — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/)

---

The setup can be complicated and depends upon a lot of variables 

- It took me an hour or so to get the initial setup working
- differences between what terminal/OS you are on

## **Adding a favicon**

---

[Adding a favicon — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/)

A “favicon” is an icon used by browsers for tabs and bookmarks. This helps to distinguish your website and to give it a unique brand.

A common question is how to add a favicon to a Flask application. First, of course, you need an icon. It should be 16 × 16 pixels and in the ICO file format. This is not a requirement but a de-facto standard supported by all relevant browsers. Put the icon in your static directory as `favicon.ico`.

### URL Building

To build a URL to a specific function, use the **`[url_for()](https://flask.palletsprojects.com/en/2.0.x/api/#flask.url_for)`** function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.

- `url_for` uses “Jinja” - a templating language
- “Jinja” comes with Flask

- Why would you want to build URLs using the URL reversing function **`[url_for()](https://flask.palletsprojects.com/en/2.0.x/api/#flask.url_for)`** instead of hard-coding them into your templates?
    1. Reversing is often more descriptive than hard-coding the URLs.
    2. You can change your URLs in one go instead of needing to remember to manually change hard-coded URLs.
    3. URL building handles escaping of special characters transparently.
    4. The generated paths are always absolute, avoiding unexpected behavior of relative paths in browsers.
    5. If your application is placed outside the URL root, for example, in `/myapplication` instead of `/`, **`[url_for()](https://flask.palletsprojects.com/en/2.0.x/api/#flask.url_for)`** properly handles that for you.

[Create dynamic URLs in Flask with url_for()](https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for)

[Jinja (template engine)](https://en.wikipedia.org/wiki/Jinja_(template_engine))

---

**Variable Rules**

You can add variable sections to a URL by marking sections with `<variable_name>`. Your function then receives the `<variable_name>` as a keyword argument. Optionally, you can use a converter to specify the type of the argument like `<converter:variable_name>`

- allows us to create dynamic URL’s
- b
- c

[Quickstart — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules)

**MIME types**

[MIME types (IANA media types) - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)

Free templates

[Mashup Template - Free Bootstrap Themes & Templates for Responsive HTML5 Websites](https://themewagon.com/author/mashuptemplate/)

[HTML5 UP](https://html5up.net/)

## Accessing Request Data

For web applications it’s crucial to react to the data a client sends to the server. In Flask this information is provided by the global **`[request](https://flask.palletsprojects.com/en/2.0.x/api/#flask.request)`** object. If you have some experience with Python you might be wondering how that object can be global and how Flask manages to still be threadsafe. The answer is context locals:

- more info
    
    Certain objects in Flask are global objects, but not of the usual kind. These objects are actually proxies to objects that are local to a specific context. What a mouthful. But that is actually quite easy to understand.
    
    Imagine the context being the handling thread. A request comes in and the web server decides to spawn a new thread (or something else, the underlying object is capable of dealing with concurrency systems other than threads). When Flask starts its internal request handling it figures out that the current thread is the active context and binds the current application and the WSGI environments to that context (thread). It does that in an intelligent way so that one application can invoke another application without breaking.
    
    So what does this mean to you? Basically you can completely ignore that this is the case unless you are doing something like unit testing. You will notice that code which depends on a request object will suddenly break because there is no request object. The solution is creating a request object yourself and binding it to the context. The easiest solution for unit testing is to use the **`[test_request_context()](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.test_request_context)`** context manager. In combination with the `with` statement it will bind a test request so that you can interact with it. Here is an example:
    
    ```python
    **from** flask **import** request
    
    **with** app.test_request_context**(**'/hello'**,** method='POST'**):***# now you can do something with the request until the# end of the with block, such as basic assertions:***assert** request.path == '/hello'
        **assert** request.method == 'POST'
    ```
    
    The other possibility is passing a whole WSGI environment to the **`[request_context()](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.request_context)`** method:
    
    ```python
    **with** app.request_context**(**environ**):assert** request.method == 'POST'
    ```
    

### The Request Object

The request object is documented in the API section and we will not cover it here in detail (see **`[Request](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request)`**). Here is a broad overview of some of the most common operations. First of all you have to import it from the `flask` module:

**`from** flask **import** request`

The current request method is available by using the **`[method](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request.method)`** attribute. To access form data (data transmitted in a `POST` or `PUT` request) you can use the **`[form](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request.form)`** attribute. Here is a full example of the two attributes mentioned above:

```python
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
```

What happens if the key does not exist in the `form` attribute? In that case a special **`[KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)`** is raised. You can catch it like a standard **`[KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)`** but if you don’t do that, a HTTP 400 Bad Request error page is shown instead. So for many situations you don’t have to deal with that problem.

To access parameters submitted in the URL (`?key=value`) you can use the **`[args](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request.args)`** attribute:

```python
searchword = request.args.get**(**'key'**,** ''**)**
```

We recommend accessing URL parameters with get or by catching the **`[KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)`** because users might change the URL and presenting them a 400 bad request page in that case is not user friendly.

For a full list of methods and attributes of the request object, head over to the **`[Request](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request)`** documentation.

# Portfolio Website

[Title page](http://devongifford.pythonanywhere.com/index.html)

[](https://www.pythonanywhere.com/user/DevonGifford/webapps/#tab_id_devongifford_pythonanywhere_com)

[https://github.com/DevonGifford/portfo.pythonanywhere](https://github.com/DevonGifford/portfo.pythonanywhere)