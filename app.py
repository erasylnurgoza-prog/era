from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Мой первый сайт</title>
            <style>
                body {
                    background-color: #f2f2f2;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 { color: #333; }
                p { color: #666; }
                button {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover { background-color: #45a049; }
            </style>
        </head>
        <body>
            <h1>Привет 👋</h1>
            <p>Это простой сайт, запущенный на Render!</p>
            <button onclick="alert('Ты нажал на кнопку!')">Нажми меня</button>
        </body>
    </html>
    """
