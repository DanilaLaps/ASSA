import unittest

from appstorespy_niche_monitor.config import load_config
from appstorespy_niche_monitor.niche_classifier import classify_app


class ClassifierTests(unittest.TestCase):
    def test_extended_dimensions_for_goods_sort(self):
        config, _ = load_config("config.yaml")
        app = {
            "name": "Goods Sort Supermarket Puzzle",
            "developer_name": "Tiny Team",
            "category": "GAME_PUZZLE",
            "description": "Sort goods in a supermarket and collect shelf rewards.",
        }

        classified = classify_app(app, config)

        self.assertEqual(classified["niche"], "sort puzzle")
        self.assertEqual(classified["market_category"], "puzzle")
        self.assertEqual(classified["core_mechanic"], "sort")
        self.assertEqual(classified["theme"], "supermarket")
        self.assertEqual(classified["meta"], "collection")
        self.assertEqual(classified["audience"], "women_25_45")
        self.assertEqual(classified["production_complexity"], "low")


if __name__ == "__main__":
    unittest.main()
