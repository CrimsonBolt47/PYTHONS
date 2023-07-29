import justpy as jp #jp is variable
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt #plt is sort of variable
data=pandas.read_csv("reviews.csv",parse_dates=["Timestamp"])

data["Month"]= data["Timestamp"].dt.strftime("%Y-%m")
month_crs=data.groupby(["Month","Course Name"])["Rating"].count().unstack()



chart_def="""
 {
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'average rating by course per month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
             '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}


"""


def app():
    wp=jp.QuasarPage() #search "quasar style" for different styles
    h1=jp.QDiv(a=wp,text="Analysis of reviews",classes="text-h1 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="these graph represents course review analysis")


    hc=jp.HighCharts(a=wp,options=chart_def)
    
    hc.options.xAxis.categories = list(month_crs.index)
    
    hc_data=[{"name":v1, "data":[v2 for v2 in month_crs[v1]]} for v1 in month_crs.columns]
    
    hc.options.series=hc_data
    return wp



jp.justpy(app)