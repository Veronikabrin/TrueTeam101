from time import sleep
import plotly
import plotly.graph_objects as go

import numpy as np
import json


class Model(object):  # todo SINGLETON class

    @staticmethod
    def send_report(report):
        print(report)  # todo initialization SINGLETON if python can

    @staticmethod
    def get_response():
        sleep(1)  # todo waiting for "report processing" and then return response of model
        return "Отчёт принят!"

    @staticmethod
    def create_plot():  # todo ???
        n = 100000
        fig = go.Figure(data=go.Scattergl(
            x=np.random.randn(n),  # todo
            y=np.random.randn(n),  # todo
            mode='markers',
            marker=dict(
                color=np.random.randn(n),  # todo
                colorscale='Viridis',
                line_width=1
            )
        ))

        graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graph_json
