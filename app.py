from flask import Flask, request
import os

app = Flask(__name__)

root_path = os.environ.get('ROOT_PATH', '/')

@app.route(root_path)
def hello_world():
    target = os.environ.get('TARGET', 'World')
    fancy_text = f"""
    <pre>
    _    _      _ _         __        __         _     _ _ 
   | |  | |    | | |        \ \      / /        | |   | | | 
   | |__| | ___| | | ___     \ \ /\ / /__  _ __ | | __| | |
   |  __  |/ _ \ | |/ _ \     \ V  V / _ \| '_ \| |/ _` | |
   | |  | |  __/ | | (_) |     \_/\_/ (_) | | | | | (_| |_|
   |_|  |_|\___|_|_|\___( )         (_) |_| |_|_|\__,_(_)
                       |/                                 
    Hello {target}, API Gateway!
    </pre>
    """

    headers = "<br>".join([f"{key}: {value}" for key, value in request.headers.items()])

    request_info = f"""
    <h2>Request Information:</h2>
    <ul>
        <li><strong>Path:</strong> {request.path}</li>
        <li><strong>URL:</strong> {request.url}</li>
        <li><strong>Method:</strong> {request.method}</li>
        <li><strong>Headers:</strong> <pre>{headers}</pre></li>
        <li><strong>Query Parameters:</strong> {request.args}</li>
        <li><strong>Form Data:</strong> {request.form}</li>
        <li><strong>Raw Data:</strong> {request.data}</li>
        <li><strong>Remote Address:</strong> {request.remote_addr}</li>
        <li><strong>User Agent:</strong> {request.user_agent}</li>
        <li><strong>Cookies:</strong> {request.cookies}</li>
    </ul>
    """
    return fancy_text + request_info

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', "8080")))