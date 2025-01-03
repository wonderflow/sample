from flask import Flask, request
import os
import time

app = Flask(__name__)

root_path = os.environ.get('ROOT_PATH', '/')
listener_port = os.environ.get('PORT', 8080)
default_status_code = os.environ.get('STATUS_CODE', 200)

@app.route(root_path)
def hello_world():
    status_code = request.args.get('status_code', default_status_code)
    target = os.environ.get('TARGET', 'World')
    timeout = request.args.get('timeout', 0)
    fancy_text = r"""
    <pre>
    _    _      _ _         __        __         _     _ _ 
   | |  | |    | | |        \ \      / /        | |   | | | 
   | |__| | ___| | | ___     \ \ /\ / /__  _ __ | | __| | |
   |  __  |/ _ \ | |/ _ \     \ V  V / _ \| '_ \| |/ _` | |
   | |  | |  __/ | | (_) |     \_/\_/ (_) | | | | | (_| |_|
   |_|  |_|\___|_|_|\___( )         (_) |_| |_|_|\__,_(_)
                       |/                                 
    </pre>
    <h2>Hello <span style="color:blue;">{target}</span>, this is API Gateway!</h2>
    """

    headers = "<br>".join([f"{key}: {value}" for key, value in request.headers.items()])

    request_info = f"""
    <h3>Request Information:</h3>
    <ul>
        <li><strong>Path:</strong> {request.path}</li>
        <li><strong>URL:</strong> {request.url}</li>
        <li><strong>Method:</strong> {request.method}</li>
        <li><strong>Headers:</strong> <pre>{headers}</pre></li>
        <li><strong>Query String:</strong> {request.query_string.decode()}</li>
    </ul>
    """

    # Sleep for timeout seconds if provided.
    if timeout:
        time.sleep(int(timeout))

    return fancy_text + request_info, status_code

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=listener_port)