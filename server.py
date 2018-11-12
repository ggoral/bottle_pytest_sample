from bottle import route, run, request, response, post, Bottle
import sys

app = Bottle()

@app.route('/')
def index():
    return 'Hi!'

if __name__ == '__main__':
    print("Python version: {}".format(sys.version))
    print("Preloading...")
    app.run(host='0.0.0.0', port=8080)
