from flask import Flask, request, render_template
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import e, sin, cos, tan, log10, log
import numpy as np
import matplotlib.pyplot as plt
import math, time, os, glob, datetime, io, sys

app = Flask(__name__)
x_list = np.array(np.arange(-100, 101, 0.1))
counter = 0
def solver1(x0,f):
    time_start = time.perf_counter()
    result = {}
    x_n = x0
    x_n_1 = x_n + .01
    step = x_n_1-x_n
    count = 0
    while abs(step) > 0.00001 and count <= 1000:
        count += 1
        try:
            denominator = df(x_n,f)
        except Exception as err:
            result['value'] = np.nan
            result['message'] = err
            result['callFunctions'] = count
            result['timer'] = time.perf_counter() - time_start
            return result

        numerator = f(x_n)
        if denominator != 0 and not np.isnan(numerator):
            x_n_1 = x_n - numerator / denominator
        else:
            result['value'] = np.nan
            result['message'] = 'Error div zero'
            result['callFunctions'] = count
            result['timer'] = time.perf_counter() - time_start
            return result
        step = x_n_1-x_n
        x_n = x_n_1
    result['value'] = x_n
    result['message'] = Validation(x_n, f)
    result['callFunctions'] = count
    result['timer'] = time.perf_counter() - time_start
    return result

def df(x,f):
    h = .00001
    return (f(x+h) - f(x)) / h

def Validation(x,f):
    epsilon = .00001
    norm_fx = abs(f(x))
    if norm_fx < epsilon:
        return ["Correct", 1, norm_fx]
    else:
        return ["Incorrect", 0, norm_fx]


@app.route('/')
def my_form():
    test = 'static/graphs/*'
    r = glob.glob(test)
    for i in r:
        os.remove(i)

    fig = plt.figure()
    fig.savefig("static/graphs/my_plot0.png")
    link = "../static/graphs/my_plot0.png"
    return render_template('my-form.html', link = link)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    x0 = float(request.form['x0']) if request.form['x0'] != '' else 0
    text = text.replace('^', '**')

    def f(x):
        try:
            sol = eval(text)
        except Exception as err:
            sol = err
        return sol
    
    global counter
    test = 'static/graphs/*'

    r = glob.glob(test)
    for i in r:
        os.remove(i)

    counter = datetime.datetime.now().microsecond
    final = f(x_list)
    if not isinstance(final, Exception):
        newton = solver1(x0, f)
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)    
        axis.plot(x_list, final)
        axis.scatter(newton['value'], f(newton['value']), c='red')
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        fig.savefig(f'static/graphs/my_plot{counter}.png')
        link = f"../static/graphs/my_plot{counter}.png"
        text = text.replace('**', '^')
        if isinstance(newton['message'], list):
            message = newton['message'][0]
            precision = newton['message'][2]
        else:
            message = newton['message']
            precision = 'n/a'
        
        return render_template('my-form.html',  link = link, 
                                                test = text, 
                                                result = newton['value'], 
                                                message = message,
                                                precision = precision,
                                                calls = newton['callFunctions'], 
                                                time = newton['timer'])
    else:
        fig = plt.figure()
        fig.savefig("static/graphs/my_plot0.png")
        return render_template('my-form.html',  link = "../static/graphs/my_plot0.png", 
                                                test = text, 
                                                message = final)
                                            

if __name__ == '__main__':
    
    app.run(debug=False)





