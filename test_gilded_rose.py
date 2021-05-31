# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from quality_updater import factory, CommonQualityUpdater, LegendaryQualityUpdater, AgedQualityUpdater, BackstageQualityUpdater, ConjuredQualityUpdater


class GildedRoseTest(unittest.TestCase):
    def test_quality_updater_factory(self):
        instance = factory.resolve(Item(name="+5 Dexterity Vest", sell_in=10, quality=20))
        self.assertIsInstance(instance, CommonQualityUpdater)
        
        instance = factory.resolve(Item(name="Elixir of the Mongoose", sell_in=5, quality=7))
        self.assertIsInstance(instance, CommonQualityUpdater)

        instance = factory.resolve(Item(name="Aged Brie", sell_in=2, quality=0))
        self.assertIsInstance(instance, AgedQualityUpdater)

        instance = factory.resolve(Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80))
        self.assertIsInstance(instance, LegendaryQualityUpdater)

        instance = factory.resolve(Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20))
        self.assertIsInstance(instance, BackstageQualityUpdater)

        instance = factory.resolve(Item(name="Conjured Mana Cake", sell_in=3, quality=6))
        self.assertIsInstance(instance, ConjuredQualityUpdater)

    def item_asserts(self, item):
        """
        assert if quality is within boundaries
        """
        self.assertTrue(item.quality <= 50)
        self.assertTrue(item.quality >= 0)

    def test_common_quality_updater(self):
        item_15_days = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
        item_6_days = Item(name="Elixir of the Mongoose", sell_in=5, quality=7)
        
        for i in range(0,6):
            CommonQualityUpdater(item_6_days).update_quality()

        self.assertEqual(item_6_days.quality, 0)
        self.assertEqual(item_6_days.sell_in, -1)

        for i in range(0,15):
            CommonQualityUpdater(item_6_days).update_quality()
            CommonQualityUpdater(item_15_days).update_quality()

        self.item_asserts(item_6_days) # check if quality is within boundaries
        self.assertEqual(item_15_days.quality, 0)
        self.assertEqual(item_15_days.sell_in, -5)

    def test_aged_quality_updater(self):
        brie_0_to_50 = Item(name="Aged Brie", sell_in=2, quality=0)
        brie_25_to_50 = Item(name="Aged Brie", sell_in=30, quality=25)

        for i in range(0, 25):
            AgedQualityUpdater(brie_25_to_50).update_quality()
            AgedQualityUpdater(brie_0_to_50).update_quality()

        self.assertEqual(brie_0_to_50.quality, 25)
        self.assertEqual(brie_25_to_50.quality, 50)

        for i in range(0, 25):
            AgedQualityUpdater(brie_25_to_50).update_quality()
            AgedQualityUpdater(brie_0_to_50).update_quality()        

        self.assertEqual(brie_0_to_50.quality, 50)
        self.assertEqual(brie_25_to_50.quality, 50)

    def test_legendary_quality_updater(self):
        legendary_item = factory.resolve(Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80))

        for i in range(0, 100):
            LegendaryQualityUpdater(legendary_item).update_quality()

        self.assertEqual(legendary_item.quality, 80)

    def test_conjured_quality_updater(self):
        conjured_5_days = Item(name="Conjured Mana Cake", sell_in=4, quality=14)

        for i in range (0, 3):
            ConjuredQualityUpdater(conjured_5_days).update_quality()

        self.assertEqual(conjured_5_days.quality, 8)

        for i in range(0, 2):
            ConjuredQualityUpdater(conjured_5_days).update_quality()

        self.assertEqual(conjured_5_days.quality, 0)


if __name__ == '__main__':
    unittest.main()
