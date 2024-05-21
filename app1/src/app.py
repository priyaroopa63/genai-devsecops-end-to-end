from flask import Flask,render_template
import socket
import requests
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')



@app.route("/")
# Vulnerability 1: Command Injection

@app.route("/ping")
def ping():
    try:
        # Get the IP address of 'google.com'
        target_ip = socket.gethostbyname('google.com')# Assuming the response contains JSON with 'ip' key
        if not target_ip:
            return "Failed to get target IP address"
       
        # Run the ping command
        result = subprocess.check_output(['ping', '-c', '10', target_ip], universal_newlines=True)
        return f"Ping result for {target_ip}: {result}"
    except subprocess.CalledProcessError:
        return f"Ping failed for {target_ip}"
    except Exception as e:
        return f"Error: {str(e)}"
    
@app.route("/test")
def test():
    return  "This works!!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
	