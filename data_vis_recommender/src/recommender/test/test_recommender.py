import pandas as pd
import unittest

from data_vis_recommender.src.recommender.visualization_recommender import VisualizationRecommender
from data_vis_recommender.src.visualization_objects.graphs.api import *


class TestVisualizationRecommender(unittest.TestCase):

    def setUp(self):
        self.recommender = VisualizationRecommender()

    def test_simple_text(self):
        df = pd.DataFrame({"Value": [42]})
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, SimpleText)

    def test_table(self):
        df = pd.DataFrame({
            'Category': ['A', 'B', 'C'],
            'Value1': [10, 20, 30],
            'Value2': [15, 25, 35]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, Table)

    def test_scatter(self):
        df = pd.DataFrame({
            'X': [1, 2, 3, 4],
            'Y': [10, 20, 30, 40]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, Scatter)

    def test_line(self):
        df = pd.DataFrame({
            'Date': pd.to_datetime(['2021-01-01', '2021-01-02', '2021-01-03']),
            'Value': [10, 20, 30]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, Line)

    def test_vertical_bars(self):
        df = pd.DataFrame({
            'Category': ['A', 'B', 'C'],
            'Value': [10, 20, 30]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, VerticalBars)

    def test_heatmap(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, Heatmap)

    def test_slope_map(self):
        df = pd.DataFrame({
            'Category': ['A', 'B', 'C'],
            'Start': [10, 15, 20],
            'End': [20, 25, 30]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, SlopeMap)

    def test_stacked_vertical_bars(self):
        df = pd.DataFrame({
            'Category': ['A', 'B', 'C'],
            'Value1': [10, 15, 20],
            'Value2': [5, 10, 15]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, StackedVerticalBars)

    def test_waterfall(self):
        # Making an assumption on waterfall chart's data format for this test
        df = pd.DataFrame({
            'Items': ['Start', 'Addition1', 'Addition2', 'End'],
            'Values': [10, 5, 5, 20]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, Waterfall)

    def test_horizontal_bars(self):
        df = pd.DataFrame({
            'Category': ['Category A', 'Category B', 'Category C'],
            'Value': [10, 20, 30]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, HorizontalBars)

    def test_stacked_horizontal_bars(self):
        df = pd.DataFrame({
            'Category': ['Category A', 'Category B', 'Category C'],
            'Value1': [10, 15, 20],
            'Value2': [5, 10, 15]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, StackedHorizontalBars)

    def test_area_chart(self):
        df = pd.DataFrame({
            'Date': pd.to_datetime(['2021-01-01', '2021-01-02', '2021-01-03']),
            'Value': [10, 20, 30]
        })
        recommender = self.recommender.recommend(df)
        self.assertIsInstance(recommender, AreaChart)


if __name__ == '__main__':
    unittest.main()
