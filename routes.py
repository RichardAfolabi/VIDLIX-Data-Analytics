
import re
import requests
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components
from flask.ext.bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, flash

# from wsgi import main


app = Flask(__name__)
bootstrap = Bootstrap()


# Initialize extensions
bootstrap.init_app(app)


# Initialize the URL for dataset location
api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/stock.json'
session = requests.Session()


# Add retries to the API calls
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
raw_data = session .get(api_url)


# Let Bokeh know it's dealing with time Series
@app.route('/')
def index():
    # plot = figure(tools=TOOLS,
    #               title='Data from Outside Quandle WIKI set',
    #               x_axis_label='date',
    #               x_axis_type='datetime')
    # script, div = components(plot)
    return render_template('index.html')
    # return render_template('index.html', script=script, div=div)


@app.route('/about/')
def about():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


