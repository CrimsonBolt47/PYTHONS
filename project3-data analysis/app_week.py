import justpy as jp #jp is variable
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data=pandas.read_csv("reviews.csv",parse_dates=["Timestamp"])

data["Week"]= data["Timestamp"].dt.strftime("%Y-%U")
week_avg=data.groupby(["Week"]).mean()
chart_def= """

{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'week'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'average rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'rating by week',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}

"""

def app():
    wp=jp.QuasarPage() #search "quasar style" for different styles
    h1=jp.QDiv(a=wp,text="Analysis of reviews",classes="text-h1 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="these graph represents course review analysis")

    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.xAxis.categories = list(week_avg.index)
    hc.options.series[0].data = list(week_avg["Rating"])

    return wp

jp.justpy(app)