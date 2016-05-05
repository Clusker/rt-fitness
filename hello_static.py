from flask import Flask, render_template
from flask import Flask, send_from_directory
app = Flask(__name__);

@app.route('/')
def frontpage():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0',debug=True)