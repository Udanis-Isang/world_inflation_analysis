import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import textwrap


def demarcation():
    print("---" * 20)
    print("***" * 20)
    print("---" * 20)

def format_labels(xtick_label):
    labels = [textwrap.fill(label.get_text(), width=10) for label in xtick_label ]
    return labels






class PlotBuilder(plot_type="pandas_hist"):
    def __init__(self, plot_type):
        self.plot_type = plot_type

    def pandas_hist(self, data, xlabel, ylabel, title="Distribution", bins=15, fig_size= (15,9)):
        fig, ax = plt.subplots(figsize = fig_size)
        data.plot(kind="hist", bins=bins, ax=ax)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        return fig


    def pyplot_hist(self, data, xlabel, ylabel, title="Distribution", bins=15, fig_size= (15,9)):
        fig, ax = plt.subplots(figsize = fig_size)
        plt.hist(x=data, bins=bins, ax=ax)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        return fig

    def seaborn_box(self, data, xlabel, ylabel, title="Distribution", fig_size= (15,9)):
        fig, ax = plt.subplots(figsize = fig_size)
        sns.boxplot(x=data, ax=ax)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        return fig

    def pandas_bar(self, df, x_col, x_label, y_label, y_col=None, title="Bar Plot", fig_size= (15,9)):
        fig, ax = plt.subplots(figsize = fig_size)
        df.plot(kind="bar", x=x_col, y=y_col, ax=ax)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xticks(rotation = 90)
        plt.title(title)
        return fig


    def plotly_bar(self, data, x_val, y_val, x_label, y_label,title="Bar Plot", color=None):
        fig = px.bar(
        data_frame = data,
        x = x_val,
        y = y_val,
        color = color,
        color_continuous_scale= px.colors.sequential.Blues,
        title = title)
        fig.update_layout(
            xaxis_title = x_label,
            yaxis_title = y_label
        )
        return fig



    def build_choropleth(self, df, color, locations="ISO3_country", title="Inflation By Country"):
        fig = px.choropleth(
            data_frame = df,
            locations = locations,
            #projection = "orthographic",
            projection = "robinson",
            #projection = "equirectangular",
            color = color,
            color_continuous_scale= px.colors.sequential.Reds,
            title = title
        )
        return fig


    