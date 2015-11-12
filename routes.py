
import re
import requests, simplejson
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.embed import components
from flask.ext.bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, flash

# from wsgi import main


app = Flask(__name__)
bootstrap = Bootstrap()


# Initialize extensions
bootstrap.init_app(app)

# Bokeh tools
TOOLS = "resize,pan,wheel_zoom,box_zoom,reset,previewsave"

# Initialize the URL for dataset location
url_path = 'https://www.quandl.com/api/v3/datasets/USCENSUS/IE_7530.json?auth_token=W_c-rhUo457bjeN2xHgy'
session = requests.Session()
r = requests.get(url_path)
new_data = r.json()


column_names = new_data['dataset']['column_names']
inp_dataset = new_data['dataset']['data']
dframe = pd.DataFrame(inp_dataset, columns=column_names)
dframe.Month = pd.to_datetime(dframe['Month'])

TOOLS = "resize,pan,wheel_zoom,box_zoom,reset,previewsave"


def make_figure():
    plot = figure(tools=TOOLS, width=750, height=450,
                  title='United States Import/Exports - Nigeria',
                  x_axis_label='date',
                  x_axis_type='datetime')
    plot.line(dframe['Month'], dframe.get('Exports'), color='#A6CEE3', legend='Exports')
    plot.line(dframe['Month'], dframe.get('Imports'), color='#33A02C', legend='Imports')
    plot.line(dframe['Month'], dframe.get('Balance'), color='#FB9A99', legend='Balance')
    return plo




@app.route('/')
def index():
    """ Homepage """
    plot = make_figure()
    script, div = components(plot)

    return render_template('index.html', script=script, div=div)


@app.route('/about/')
def about():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


