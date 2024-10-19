from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    user = os.getenv("USER") or os.getenv("USERNAME")
    time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    
    top = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True).stdout

    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> Sunil Kharra</p>
    <p><strong>Username:</strong> {user}</p>
    <p><strong>Server Time (IST):</strong> {time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <pre>{top}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
