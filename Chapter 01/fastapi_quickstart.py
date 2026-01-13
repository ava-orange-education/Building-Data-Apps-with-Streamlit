from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
@app.post("/", response_class=HTMLResponse)
async def read_form(request: Request, name: str = Form(None)):
    if request.method == "POST" and name is not None:
        message = f"Hello, {name}!"
    else:
        message = ""
    return f"""
        <form method="post">
            <label for="name">Enter your name:</label>
            <input type="text" name="name" />
            <input type="submit" />
        </form>
        <p>{message}</p>
    """
