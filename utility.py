import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import textwrap


def demarcation():
    print("---" * 20)
    print("***" * 20)
    print("---" * 20)

def format_labels(axis):
    labels = [textwrap.fill(label.get_text(), width=10) for label in axis.get_xticklabels()]
    return labels

def shorten_labels(axis):
    labels = format_labels(axis)
    axis.set_xticklabels(labels)



class PlotBuilder():
    def __init__(self):
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")


    def _format_labels(self, axis):
        labels = [textwrap.fill(label.get_text(), width=10) for label in axis.get_xticklabels()]
        return labels

    def _shorten_labels(self, axis):
        labels = self._format_labels(axis)
        axis.set_xticklabels(labels)
        return

    def pandas_hist(self, data, x_label, y_label, title="Distribution", bins=15, fig_size= (15,9), axis=None):
        if axis == None:
            fig, ax = plt.subplots(figsize = fig_size)
            data.plot(kind="hist", bins=bins, ax=ax)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            return fig

        else:
            data.plot(kind="hist", bins=bins, ax=axis)
            axis.set_xlabel(x_label)
            axis.set_ylabel(y_label)
            axis.set_title(title)
            return axis
            


    def pyplot_hist(self, data, x_label, y_label, title="Distribution", bins=15, fig_size= (15,9)):
        fig, ax = plt.subplots(figsize = fig_size)
        plt.hist(x=data, bins=bins, ax=ax)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        return fig

    def seaborn_box(self, data, x_label, y_label, title="Box Plot", fig_size= (15,9), axis=None):
        if axis == None:
            fig, ax = plt.subplots(figsize = fig_size)
            sns.boxplot(x=data, ax=ax)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            ax.set_title(title)
            return fig

        else:
            sns.boxplot(x=data, ax=axis)
            axis.set_xlabel(x_label)
            axis.set_ylabel(y_label)
            axis.set_title(title)
            return axis

    def pandas_bar(self, x_label, y_label, df=None, x_col=None, y_col=None, title="Bar Plot", fig_size= (15,9), axis=None):
        if axis == None:
            fig, ax = plt.subplots(figsize = fig_size)

            if df is not None:
                df.plot(kind="bar", x=x_col, y=y_col, ax=ax)
            else:
                ax.bar(x_col, y_col)
            
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            ax.tick_params(axis="x", rotation = 90)
            self._shorten_labels(ax)
            ax.set_title(title)
            return fig

        else:
            if df is not None:
                df.plot(kind="bar", x=x_col, y=y_col, ax=axis)
            else:
                axis.bar(x_col, y_col)
            
            axis.set_xlabel(x_label)
            axis.set_ylabel(y_label)
            axis.tick_params(axis="x", rotation=90)
            self._shorten_labels(axis)
            axis.set_title(title)
            return axis


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


    def multiple_plots(self, grid, fig_size=(15,9), plots=None, sup_title="PLOTS"):

        if plots == None:
            plots = {}

        fig, ax = plt.subplots(*grid, figsize=fig_size, squeeze=False)
        
        for key, values in plots.items():
            plot_type = values["plot_type"]
            
            if plot_type == "boxplot":
                data = values["data"]
                x_label = values["x_label"]
                y_label = values["y_label"]
                title = values["title"]
                axis = values["axis"]

                self.seaborn_box(data=data,
                                x_label=x_label,
                                y_label=y_label,
                                title=title,
                                axis=ax[*axis]
                                )

            elif plot_type == "pandas_bar":
                d_frame = values["d_frame"]
                x_label = values["x_label"]
                y_label = values["y_label"]
                title = values["title"]
                axis = values["axis"]
                x_col = values["x_col"]
                y_col = values["y_col"]
            

                self.pandas_bar(
                   df=d_frame,
                   x_col=x_col,
                   x_label=x_label,
                   y_label=y_label,
                   y_col=y_col,
                   title=title,
                   axis=ax[*axis] 
                )

            elif plot_type == "pandas_hist":
                data = values["data"]
                x_label = values["x_label"]
                y_label = values["y_label"]
                title = values["title"]
                axis = values["axis"]

                self.pandas_hist(
                    data=data,
                    x_label=x_label,
                    y_label=y_label,
                    title=title,
                    axis=ax[*axis]
                )

        plt.tight_layout()
        fig.suptitle(sup_title, y=1.08)

        return fig



    