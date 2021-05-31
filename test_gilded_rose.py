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

            
if __name__ == '__main__':
    unittest.main()
