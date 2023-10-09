import pandas as pd
from data_vis_recommender.src.visualization_objects.graphs.api import *


class VisualizationRecommender:
    """
    All graph conditions are a work in progress.
    """

    def is_simple_text(self, df):
        return df.size == 1 and (
                pd.api.types.is_numeric_dtype(df.iloc[0, 0]) or pd.api.types.is_datetime64_any_dtype(
            df.iloc[0, 0]))

    def is_table(self, df):
        return df.shape[1] > 1

    def is_scatter(self, df):
        return df.shape[1] == 2 and all(pd.api.types.is_numeric_dtype(df[col]) for col in df.columns)

    def is_line(self, df):
        return df.shape[1] == 2 and any(
            pd.api.types.is_datetime64_any_dtype(df[col]) for col in df.columns) and any(
            pd.api.types.is_numeric_dtype(df[col]) for col in df.columns)

    def is_vertical_bars(self, df):
        return df.shape[1] == 2 and any(
            pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == object for col in df.columns) and any(
            pd.api.types.is_numeric_dtype(df[col]) for col in df.columns)

    def is_heatmap(self, df):
        return df.shape[1] > 2 and all(pd.api.types.is_numeric_dtype(df[col]) for col in df.columns)

    def is_slope_map(self, df):
        # Assuming slope maps compare two points across categories.
        return df.shape[1] == 3 and any(
            pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == object for col in df.columns) and all(
            pd.api.types.is_numeric_dtype(df[col]) for col in
            df.select_dtypes(include=['float64', 'int64']).columns)

    def is_stacked_vertical_bars(self, df):
        return df.shape[1] > 2 and any(
            pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == object for col in df.columns) and all(
            pd.api.types.is_numeric_dtype(df[col]) for col in
            df.select_dtypes(include=['float64', 'int64']).columns)

    def is_waterfall(self, df):
        # Assuming waterfall charts display incremental values leading to a final value.
        return df.shape[1] == 2 and df[col].dtype == object and pd.api.types.is_numeric_dtype(df.iloc[:, 1])

    def is_horizontal_bars(self, df):
        return df.shape[1] == 2 and df[col].dtype == object and pd.api.types.is_numeric_dtype(df.iloc[:, 1])

    def is_stacked_horizontal_bars(self, df):
        return df.shape[1] > 2 and any(
            pd.api.types.is_categorical_dtype(df[col]) or df[col].dtype == object for col in df.columns) and all(
            pd.api.types.is_numeric_dtype(df[col]) for col in
            df.select_dtypes(include=['float64', 'int64']).columns)

    def is_area_chart(self, df):
        # Assuming area charts show a metric over time.
        return df.shape[1] == 2 and pd.api.types.is_datetime64_any_dtype(
            df.iloc[:, 0]) and pd.api.types.is_numeric_dtype(df.iloc[:, 1])

    def recommend(self, dataframe):

        graph_conditions = [
            (self.is_simple_text, SimpleText),
            (self.is_table, Table),
            (self.is_scatter, Scatter),
            (self.is_line, Line),
            (self.is_vertical_bars, VerticalBars),
            (self.is_heatmap, Heatmap),
            (self.is_slope_map, SlopeMap),
            (self.is_stacked_vertical_bars, StackedVerticalBars),
            (self.is_waterfall, Waterfall),
            (self.is_horizontal_bars, HorizontalBars),
            (self.is_stacked_horizontal_bars, StackedHorizontalBars),
            (self.is_area_chart, AreaChart)
        ]
        for condition, graph_class in graph_conditions:
            if condition(dataframe):
                return graph_class(dataframe)

        return None
