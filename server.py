from bottle import route, run, request, response, post, Bottle
import sys
import request_filter
import logging

app = Bottle()

@app.route('/')
def index():
    return 'Hi!'

@app.route('/filtred')
def filtred():
    data = {}
    request_filter.filter_data(data)
    print(data)
    return 'filtred'

if __name__ == '__main__':
    print("Python version: {}".format(sys.version))
    print("Preloading...")
    app.run(host='0.0.0.0', port=8080)
