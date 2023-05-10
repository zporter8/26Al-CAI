import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

url = "https://raw.githubusercontent.com/f-jorge/f-jorge.github.io/main/Al26_CAIs_data%20-%2026Al_27Al.csv"
data = pd.read_csv(url, index_col=0)

x = data["26Al/27Al"]
l = []
# reducing the data to only numerical values by removing words
for i in x:
    if isinstance(i, str):
        # if i[0] != 'M':
        if not i.isalpha() and i[0] != 'M':
            l.append(i)
l.sort()
#need to make data into floats
new_l = [float(x) for x in l]

CO3_0 = data.loc[data['chondrite type'] == 'CO3.0']
c = CO3_0["26Al/27Al"]
l1 = []
for i in c:
    if isinstance(i, str):
        if not i.isalpha() and i[0] != 'M':
            l1.append(i)
l1.sort()
new_l1 = [float(x) for x in l1]

CV3 = data.loc[data['chondrite type'] == 'CV3']
cv = CV3["26Al/27Al"]
l2 = []
for i in cv:
    if isinstance(i, str):
        if not i.isalpha() and i[0] != 'M':
            l2.append(i)
l2.sort()
new_l2 = [float(x) for x in l2]

CM2 = data.loc[data['chondrite type'] == 'CM2']
cm = CM2["26Al/27Al"]
l3 = []
for i in cm:
    if isinstance(i, str):
        if not i.isalpha() and i[0] != 'M':
            l3.append(i)
l3.sort()
new_l3 = [float(x) for x in l3]

CR2 = data.loc[data['chondrite type'] == 'CR2']
cr = CR2["26Al/27Al"]
l4 = []
for i in cr:
    if isinstance(i, str):
        if not i.isalpha() and i[0] != 'M':
            l4.append(i)
l4.sort()
new_l4 = [float(x) for x in l4]

#need to be list of lists in order to plot
hist_data = [new_l, new_l1, new_l2, new_l3, new_l4]
labels = ["All Chondrites", "CO3.0", "CV3", "CM2", "CR2"]
fig = ff.create_distplot(hist_data=hist_data, group_labels=labels, show_rug=False)
fig.update_xaxes(title = "26Al/27Al", range = [-1,7])
# want the histogram bars to be less opaque or for the KDE curves to be more opaque
#fig.update_traces(opacity=.75)
#fig.update_layout(newselection_line_width= 5)

small = data.loc[data["CAI size x"] <= '100']
g1 = small["CAI size x"]

medium = data[(data['CAI size x'] > '100') & (data['CAI size x'] <= '500')]
g2 = medium["CAI size x"]

large = data.loc[data["CAI size x"] > '500']
g3 = large["CAI size x"]

# add traces to scatter plot... small, medium and large grains
trace1 = go.Scatter(x=l, y=g1, name = "CAI size <100", mode= 'markers', xaxis='x2', yaxis= 'y2')
trace2 = go.Scatter(x=l, y=g2, name = "CAI size 100-500", mode= 'markers', xaxis='x2', yaxis= 'y2')
trace3 = go.Scatter(x=l, y=g3, name = "CAI size >500", mode= 'markers', xaxis='x2', yaxis= 'y2')
fig.add_traces([trace1, trace2, trace3])

# initialize xaxis2 and yaxis2
fig['layout']['xaxis2'] = {}
fig['layout']['yaxis2'] = {}

# Edit layout for subplots
fig.layout.xaxis.update({'domain': [0, .5]})
fig.layout.xaxis2.update({'domain': [0.6, 1.]})
fig.layout.xaxis2.update({'title': '26Al/27Al'})

# The graph's yaxis MUST BE anchored to the graph's xaxis
fig.layout.yaxis2.update({'anchor': 'x2'})
fig.layout.yaxis2.update({'title': 'Size'})
#fig.update_layout(yaxis2_range = [0, 30000])

# Update the margins to add a title and see graph x-labels.
fig.layout.margin.update({'t':50, 'b':100})
#fig.layout.update({'title': '26Al'})

fig.show()


######################################
#html = io.to_html(fig, full_html=True, include_plotlyjs='cdn')
#import plotly.io as io
#with open('facetted.html', 'w') as f:
    #f.writelines(io.to_html(fig, include_plotlyjs='cnd', full_html=True))
