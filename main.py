from typing import List, Optional, Set
from pydantic import BaseModel
from fastapi import FastAPI, Query

app = FastAPI()
css_var = """@import url("https://fonts.googleapis.com/css?family=Fira+Sans");
html, body {
  position: relative;
  min-height: 100vh;
  background-color: #E1E8EE;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: "Fira Sans", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.form-structor {
  background-color: #222;
  border-radius: 15px;
  height: 550px;
  width: 350px;
  position: relative;
  overflow: hidden;
}
.form-structor::after {
  content: '';
  opacity: 0.8;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-repeat: no-repeat;
  background-position: left bottom;
  background-size: 500px;
  background-image: url('https://images.unsplash.com/photo-1503602642458-232111445657?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=bf884ad570b50659c5fa2dc2cfb20ecf&auto=format&fit=crop&w=1000&q=100');
}
.form-structor .signup {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  width: 65%;
  z-index: 5;
  -webkit-transition: all 0.3s ease;
}
.form-structor .signup.slide-up {
  top: 5%;
  -webkit-transform: translate(-50%, 0%);
  -webkit-transition: all 0.3s ease;
}
.form-structor .signup.slide-up .form-holder, .form-structor .signup.slide-up .submit-btn {
  opacity: 0;
  visibility: hidden;
}
.form-structor .signup.slide-up .form-title {
  font-size: 1em;
  cursor: pointer;
}
.form-structor .signup.slide-up .form-title span {
  margin-right: 5px;
  opacity: 1;
  visibility: visible;
  -webkit-transition: all 0.3s ease;
}
.form-structor .signup .form-title {
  color: #fff;
  font-size: 1.7em;
  text-align: center;
}
.form-structor .signup .form-title span {
  color: rgba(0, 0, 0, 0.4);
  opacity: 0;
  visibility: hidden;
  -webkit-transition: all 0.3s ease;
}
.form-structor .signup .form-holder {
  border-radius: 15px;
  background-color: #fff;
  overflow: hidden;
  margin-top: 50px;
  opacity: 1;
  visibility: visible;
  -webkit-transition: all 0.3s ease;
}
.form-structor .signup .form-holder .input {
  border: 0;
  outline: none;
  box-shadow: none;
  display: block;
  height: 30px;
  line-height: 30px;
  padding: 8px 15px;
  border-bottom: 1px solid #eee;
  width: 100%;
  font-size: 12px;
}
.form-structor .signup .form-holder .input:last-child {
  border-bottom: 0;
}
.form-structor .signup .form-holder .input::-webkit-input-placeholder {
  color: rgba(0, 0, 0, 0.4);
}
.form-structor .signup .submit-btn {
  background-color: rgba(0, 0, 0, 0.4);
  color: rgba(255, 255, 255, 0.7);
  border: 0;
  border-radius: 15px;
  display: block;
  margin: 15px auto;
  padding: 15px 45px;
  width: 100%;
  font-size: 13px;
  font-weight: bold;
  cursor: pointer;
  opacity: 1;
  visibility: visible;
  -webkit-transition: all 0.3s ease;
}
.form-structor .signup .submit-btn:hover {
  transition: all 0.3s ease;
  background-color: rgba(0, 0, 0, 0.8);
}
.form-structor .login {
  position: absolute;
  top: 20%;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #fff;
  z-index: 5;
  -webkit-transition: all 0.3s ease;
}
.form-structor .login::before {
  content: '';
  position: absolute;
  left: 50%;
  top: -20px;
  -webkit-transform: translate(-50%, 0);
  background-color: #fff;
  width: 200%;
  height: 250px;
  border-radius: 50%;
  z-index: 4;
  -webkit-transition: all 0.3s ease;
}
.form-structor .login .center {
  position: absolute;
  top: calc(50% - 10%);
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  width: 65%;
  z-index: 5;
  -webkit-transition: all 0.3s ease;
}
.form-structor .login .center .form-title {
  color: #000;
  font-size: 1.7em;
  text-align: center;
}
.form-structor .login .center .form-title span {
  color: rgba(0, 0, 0, 0.4);
  opacity: 0;
  visibility: hidden;
  -webkit-transition: all 0.3s ease;
}
.form-structor .login .center .form-holder {
  border-radius: 15px;
  background-color: #fff;
  border: 1px solid #eee;
  overflow: hidden;
  margin-top: 50px;
  opacity: 1;
  visibility: visible;
  -webkit-transition: all 0.3s ease;
}
.form-structor .login .center .form-holder .input {
  border: 0;
  outline: none;
  box-shadow: none;
  display: block;
  height: 30px;
  line-height: 30px;
  padding: 8px 15px;
  border-bottom: 1px solid #eee;
  width: 100%;
  font-size: 12px;
}
.form-structor .login .center .form-holder .input:last-child {
  border-bottom: 0;
}
.form-structor .login .center .form-holder .input::-webkit-input-placeholder {
  color: rgba(0, 0, 0, 0.4);
}
.form-structor .login .center .submit-btn {
  background-color: #6B92A4;
  color: rgba(255, 255, 255, 0.7);
  border: 0;
  border-radius: 15px;
  display: block;
  margin: 15px auto;
  padding: 15px 45px;
  width: 100%;
  font-size: 13px;
  font-weight: bold;
  cursor: pointer;
  opacity: 1;
  visibility: visible;
  -webkit-transition: all 0.3s ease;
}
.form-structor .login .center .submit-btn:hover {
  transition: all 0.3s ease;
  background-color: rgba(0, 0, 0, 0.8);
}
.form-structor .login.slide-up {
  top: 90%;
  -webkit-transition: all 0.3s ease;
}
.form-structor .login.slide-up .center {
  top: 10%;
  -webkit-transform: translate(-50%, 0%);
  -webkit-transition: all 0.3s ease;
}
.form-structor .login.slide-up .form-holder, .form-structor .login.slide-up .submit-btn {
  opacity: 0;
  visibility: hidden;
  -webkit-transition: all 0.3s ease;
}
.form-structor .login.slide-up .form-title {
  font-size: 1em;
  margin: 0;
  padding: 0;
  cursor: pointer;
  -webkit-transition: all 0.3s ease;
}
.form-structor .login.slide-up .form-title span {
  margin-right: 5px;
  opacity: 1;
  visibility: visible;
  -webkit-transition: all 0.3s ease;
}
"""
js_var = """console.clear();

const loginBtn = document.getElementById('login');
const signupBtn = document.getElementById('signup');

loginBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode.parentNode;
	Array.from(e.target.parentNode.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			signupBtn.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});

signupBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode;
	Array.from(e.target.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			loginBtn.parentNode.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});"""
html_login = f"""
<style>{css_var}</style>
<div class="form-structor">
	<div class="signup">
		<h2 class="form-title" id="signup"><span>or</span>Sign up</h2>
		<div class="form-holder">
			<input type="text" class="input" placeholder="Name" />
			<input type="email" class="input" placeholder="Email" />
			<input type="password" class="input" placeholder="Password" />
		</div>
		<button class="submit-btn">Sign up</button>
	</div>
	<div class="login slide-up">
		<div class="center">
			<h2 class="form-title" id="login"><span>or</span>Log in</h2>
			<div class="form-holder">
				<input type="email" class="input" placeholder="Email" />
				<input type="password" class="input" placeholder="Password" />
			</div>
			<button class="submit-btn">Log in</button>
		</div>
	</div>
</div>
<script>{js_var}</scripts>
"""

@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None,depreciated=True)):

    query_items = {"q": q}
    return query_items


#i am testing config
class yeah(BaseModel):
    item: str
    value: str

    class Config:
        schema_extra = {"item":"this is the item",
            "value":"this is the value"}

@app.post("/yeah",summary="Create an item",response_description="The created item")
async def con(item: yeah):
    """
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return {"msg":"validated"}


#this is used to create nested request or response
"""
the output of the below path is

{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
"""
"""
class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []

    image: Optional[Image] = None



@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
"""

#using response model onset

from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder



class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, )
async def read_item(item_id: str):
    print(items[item_id])
    return items[item_id]

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded

#working with form data

from fastapi import  Form




@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    print(password)
    return {"username": username}

#working with files and form data


from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse



@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    f_ile = open("files.txt","wb")
    f_ile.writelines(files)
    f_ile.close()
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/",summary="Create an item",response_description="The created item")
async def create_upload_files(files: List[UploadFile] = File(...)):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return {"filenames": [file.filename for file in files]}

@app.get('/form')
def many():
    content = """
    <style>*, ::after, ::before {
  box-sizing: border-box;
}
body {
  background-color: #212121;
  color: #fff;
  font-family: monospace, serif;
  letter-spacing: 0.05em;
}
h1 {
  font-size: 23px;
}
.form {
  width: 300px;
  padding: 64px 15px 24px;
  margin: 0 auto;
}
.form .control {
  margin: 0 0 24px;
}
.form .control input {
  width: 100%;
  padding: 14px 16px;
  border: 0;
  background: transparent;
  color: #fff;
  font-family: monospace, serif;
  letter-spacing: 0.05em;
  font-size: 16px;
}
.form .control input:hover, .form .control input:focus {
  outline: none;
  border: 0;
}
.form .btn {
  width: 100%;
  display: block;
  padding: 14px 16px;
  background: transparent;
  outline: none;
  border: 0;
  color: #fff;
  letter-spacing: 0.1em;
  font-weight: bold;
  font-family: monospace;
  font-size: 16px;
}
.block-cube {
  position: relative;
}
.block-cube .bg-top {
  position: absolute;
  height: 10px;
  background: #020024;
  background: linear-gradient(90deg, #020024 0%, #340979 37%, #00d4ff 94%);
  bottom: 100%;
  left: 5px;
  right: -5px;
  transform: skew(-45deg, 0);
  margin: 0;
}
.block-cube .bg-top .bg-inner {
  bottom: 0;
}
.block-cube .bg {
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  background: #020024;
  background: linear-gradient(90deg, #020024 0%, #340979 37%, #00d4ff 94%);
}
.block-cube .bg-right {
  position: absolute;
  background: #020024;
  background: #00d4ff;
  top: -5px;
  z-index: 0;
  bottom: 5px;
  width: 10px;
  left: 100%;
  transform: skew(0, -45deg);
}
.block-cube .bg-right .bg-inner {
  left: 0;
}
.block-cube .bg .bg-inner {
  transition: all 0.2s ease-in-out;
}
.block-cube .bg-inner {
  background: #212121;
  position: absolute;
  left: 2px;
  top: 2px;
  right: 2px;
  bottom: 2px;
}
.block-cube .text {
  position: relative;
  z-index: 2;
}
.block-cube.block-input input {
  position: relative;
  z-index: 2;
}
.block-cube.block-input input:focus ~ .bg-right .bg-inner, .block-cube.block-input input:focus ~ .bg-top .bg-inner, .block-cube.block-input input:focus ~ .bg-inner .bg-inner {
  top: 100%;
  background: rgba(255, 255, 255, 0.5);
}
.block-cube.block-input .bg-top, .block-cube.block-input .bg-right, .block-cube.block-input .bg {
  background: rgba(255, 255, 255, 0.5);
  transition: background 0.2s ease-in-out;
}
.block-cube.block-input .bg-right .bg-inner, .block-cube.block-input .bg-top .bg-inner {
  transition: all 0.2s ease-in-out;
}
.block-cube.block-input:focus .bg-top, .block-cube.block-input:hover .bg-top, .block-cube.block-input:focus .bg-right, .block-cube.block-input:hover .bg-right, .block-cube.block-input:focus .bg, .block-cube.block-input:hover .bg {
  background: rgba(255, 255, 255, 0.8);
}
.block-cube.block-cube-hover:focus .bg .bg-inner, .block-cube.block-cube-hover:hover .bg .bg-inner {
  top: 100%;
}
.credits {
  position: fixed;
  left: 0;
  bottom: 0;
  padding: 15px 15px;
  width: 100%;
  z-index: 111;
}
.credits a {
  opacity: 0.6;
  color: #fff;
  font-size: 11px;
  text-decoration: none;
}
.credits a:hover {
  opacity: 1;
}</style>
    <form class="form" action="/login/" method="post">
  <div class="control">
    <h1>
      Sign In
    </h1>
  </div>
  <div class="control block-cube block-input">
  Username
    <input name="username"/><div class="bg-top">
      <div class="bg-inner"></div>
    </div>
    <div class="bg-right">
      <div class="bg-inner"></div>
    </div>
    <div class="bg">
      <div class="bg-inner"></div>
    </div>
  </div>
  <div class="control block-cube block-input">
    
    <input name="password"/><div class="bg-top">
      <div class="bg-inner"></div>
    </div>
    <div class="bg-right">
      <div class="bg-inner"></div>
    </div>
    <div class="bg">
      <div class="bg-inner"></div>
    </div>
  </div>
  <button class="btn block-cube block-cube-hover">
    <div class="bg-top">
      <div class="bg-inner"></div>
    </div>
    <div class="bg-right">
      <div class="bg-inner"></div>
    </div>
    <div class="bg">
      <div class="bg-inner"></div>
    </div>
    <div class="text">
      Log In
    </div></button>
  </form>
    """
    return(HTMLResponse(content))


@app.get("/",deprecated=True)
async def main():
    content = """
<body style="color: blue; font-size: 46px;">
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """

    return HTMLResponse(content=content)


@app.get('/fine')
def api():
    css_var = """@import url("https://fonts.googleapis.com/css?family=Fira+Sans");
    html, body {
      position: relative;
      min-height: 100vh;
      background-color: #E1E8EE;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: "Fira Sans", Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    .form-structor {
      background-color: #222;
      border-radius: 15px;
      height: 550px;
      width: 350px;
      position: relative;
      overflow: hidden;
    }
    .form-structor::after {
      content: '';
      opacity: 0.8;
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      background-repeat: no-repeat;
      background-position: left bottom;
      background-size: 500px;
      background-image: url('https://images.unsplash.com/photo-1503602642458-232111445657?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=bf884ad570b50659c5fa2dc2cfb20ecf&auto=format&fit=crop&w=1000&q=100');
    }
    .form-structor .signup {
      position: absolute;
      top: 50%;
      left: 50%;
      -webkit-transform: translate(-50%, -50%);
      width: 65%;
      z-index: 5;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .signup.slide-up {
      top: 5%;
      -webkit-transform: translate(-50%, 0%);
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .signup.slide-up .form-holder, .form-structor .signup.slide-up .submit-btn {
      opacity: 0;
      visibility: hidden;
    }
    .form-structor .signup.slide-up .form-title {
      font-size: 1em;
      cursor: pointer;
    }
    .form-structor .signup.slide-up .form-title span {
      margin-right: 5px;
      opacity: 1;
      visibility: visible;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .signup .form-title {
      color: #fff;
      font-size: 1.7em;
      text-align: center;
    }
    .form-structor .signup .form-title span {
      color: rgba(0, 0, 0, 0.4);
      opacity: 0;
      visibility: hidden;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .signup .form-holder {
      border-radius: 15px;
      background-color: #fff;
      overflow: hidden;
      margin-top: 50px;
      opacity: 1;
      visibility: visible;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .signup .form-holder .input {
      border: 0;
      outline: none;
      box-shadow: none;
      display: block;
      height: 30px;
      line-height: 30px;
      padding: 8px 15px;
      border-bottom: 1px solid #eee;
      width: 100%;
      font-size: 12px;
    }
    .form-structor .signup .form-holder .input:last-child {
      border-bottom: 0;
    }
    .form-structor .signup .form-holder .input::-webkit-input-placeholder {
      color: rgba(0, 0, 0, 0.4);
    }
    .form-structor .signup .submit-btn {
      background-color: rgba(0, 0, 0, 0.4);
      color: rgba(255, 255, 255, 0.7);
      border: 0;
      border-radius: 15px;
      display: block;
      margin: 15px auto;
      padding: 15px 45px;
      width: 100%;
      font-size: 13px;
      font-weight: bold;
      cursor: pointer;
      opacity: 1;
      visibility: visible;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .signup .submit-btn:hover {
      transition: all 0.3s ease;
      background-color: rgba(0, 0, 0, 0.8);
    }
    .form-structor .login {
      position: absolute;
      top: 20%;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: #fff;
      z-index: 5;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .login::before {
      content: '';
      position: absolute;
      left: 50%;
      top: -20px;
      -webkit-transform: translate(-50%, 0);
      background-color: #fff;
      width: 200%;
      height: 250px;
      border-radius: 50%;
      z-index: 4;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .login .center {
      position: absolute;
      top: calc(50% - 10%);
      left: 50%;
      -webkit-transform: translate(-50%, -50%);
      width: 65%;
      z-index: 5;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .login .center .form-title {
      color: #000;
      font-size: 1.7em;
      text-align: center;
    }
    .form-structor .login .center .form-title span {
      color: rgba(0, 0, 0, 0.4);
      opacity: 0;
      visibility: hidden;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .login .center .form-holder {
      border-radius: 15px;
      background-color: #fff;
      border: 1px solid #eee;
      overflow: hidden;
      margin-top: 50px;
      opacity: 1;
      visibility: visible;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .login .center .form-holder .input {
      border: 0;
      outline: none;
      box-shadow: none;
      display: block;
      height: 30px;
      line-height: 30px;
      padding: 8px 15px;
      border-bottom: 1px solid #eee;
      width: 100%;
      font-size: 12px;
    }
    .form-structor .login .center .form-holder .input:last-child {
      border-bottom: 0;
    }
    .form-structor .login .center .form-holder .input::-webkit-input-placeholder {
      color: rgba(0, 0, 0, 0.4);
    }
    .form-structor .login .center .submit-btn {
      background-color: #6B92A4;
      color: rgba(255, 255, 255, 0.7);
      border: 0;
      border-radius: 15px;
      display: block;
      margin: 15px auto;
      padding: 15px 45px;
      width: 100%;
      font-size: 13px;
      font-weight: bold;
      cursor: pointer;
      opacity: 1;
      visibility: visible;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .login .center .submit-btn:hover {
      transition: all 0.3s ease;
      background-color: rgba(0, 0, 0, 0.8);
    }
    .form-structor .login.slide-up {
      top: 90%;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .login.slide-up .center {
      top: 10%;
      -webkit-transform: translate(-50%, 0%);
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .login.slide-up .form-holder, .form-structor .login.slide-up .submit-btn {
      opacity: 0;
      visibility: hidden;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .login.slide-up .form-title {
      font-size: 1em;
      margin: 0;
      padding: 0;
      cursor: pointer;
      -webkit-transition: all 0.3s ease;
    }
    .form-structor .login.slide-up .form-title span {
      margin-right: 5px;
      opacity: 1;
      visibility: visible;
      -webkit-transition: all 0.3s ease;
    }
    """
    js_var = """console.clear();

    const loginBtn = document.getElementById('login');
    const signupBtn = document.getElementById('signup');

    loginBtn.addEventListener('click', (e) => {
    	let parent = e.target.parentNode.parentNode;
    	Array.from(e.target.parentNode.parentNode.classList).find((element) => {
    		if(element !== "slide-up") {
    			parent.classList.add('slide-up')
    		}else{
    			signupBtn.parentNode.classList.add('slide-up')
    			parent.classList.remove('slide-up')
    		}
    	});
    });

    signupBtn.addEventListener('click', (e) => {
    	let parent = e.target.parentNode;
    	Array.from(e.target.parentNode.classList).find((element) => {
    		if(element !== "slide-up") {
    			parent.classList.add('slide-up')
    		}else{
    			loginBtn.parentNode.parentNode.classList.add('slide-up')
    			parent.classList.remove('slide-up')
    		}
    	});
    });"""
    html_login = f"""
    <style>{css_var}</style>
    
    <div class="form-structor">
    	<div class="signup">
    		<h2 class="form-title" id="signup"><span>or</span>Sign up</h2>
    		<div class="form-holder">
            
    			<input type="text" class="input" placeholder="Userame" />
    			<input type="email" class="input" placeholder="Email" />
    			<input type="password" class="input" placeholder="Password" />
    		</div>
    		<button class="submit-btn">Sign up</button>
    	</div>
    	<div class="login slide-up">
    		<div class="center">
    			<h2 class="form-title" id="login"><span>or</span>Log in</h2>
    			<div class="form-holder">
    			<form action="/login/"  method="post">
    				<input type="email" class="input" placeholder="Username" name="username" />
    				<input type="password" class="input" placeholder="Password" name="password"/>
    		    <button class="submit-btn">Log in</button>
    		    </form>
    			</div>
    			
            <script>{js_var}</script>
    		</div>
    	</div>
    </div>
    
    """

    return (HTMLResponse(html_login))


#security  password
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/item/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

