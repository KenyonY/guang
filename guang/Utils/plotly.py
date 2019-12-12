import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Subplots:
    def __init__(self, rows=1, cols=1, **kwargs):
        self.rows = rows
        self.cols = cols
        x_title = kwargs.get('x_title', 'x_title')
        y_title = kwargs.get('y_title', 'y_title')
        self.fig = make_subplots(rows=rows, cols=cols, x_title=x_title, y_title=y_title)
        self.count = 0

    def plot(self,x, y, **kwargs):
        '''
        Params:
            legend: like matplotlib's legend
            mode: 'lines', 'markers', 'lines+markers', 'text'

        '''
        
        legend = kwargs.get('legend', self.count+1)
        mode = kwargs.get('mode', 'lines') # 
        row, col = np.divmod(self.count, self.cols)
        row, col = int(row+1), int(col+1)
        
        self.fig.add_trace(go.Scatter(x=x, y=y, mode=mode, name=legend), row=row, col=col)
#         self.fig.update_layout(go.Layout(xaxis=dict(title='X'),
#                                          yaxis=dict(title='Y')),
#                                 overwrite= 0
#                               )
        self.count += 1

    def show(self, *args, **kwargs):
        self.fig.show(*args, **kwargs)


class Multiplots:
    def __init__(self, **kwargs):

        self.title = 'title'
        self.fig = go.Figure()
        self.x_label = 'X'
        self.y_label = 'Y'
        self.count = 0

    def plot(self, x, y, **kwargs):
        '''
        Params:
            legend: like matplotlib's legend
            mode: 'lines', 'markers', 'lines+markers', 'text'
        '''

        legend = kwargs.get('legend', self.count + 1)
        mode = kwargs.get('mode', 'lines')  #

        self.fig.add_trace(go.Scatter(x=x, y=y, mode=mode, name=legend))
        self.count += 1

    def show(self, *args, **kwargs):
        self.fig.update_layout(title=f'{self.title:}',overwrite=1,
                      xaxis=dict(title= self.x_label),
                      yaxis=dict(title= self.y_label),
#                       yaxis_zeroline=False, xaxis_zeroline=False
                     )
        self.fig.show(*args, **kwargs)