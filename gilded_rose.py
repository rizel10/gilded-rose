# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            QualityUpdateFactory(item).update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class QualityUpdater(ABC):
    def __init__(self, item):
        self.item = item

    @property
    def quality(self):
        return self.item.quality

    @quality.setter
    def quality(self, value):
        if value < 0:
            self.item.quality = 0
        elif value > 50:
            self.item.quality = 50
        else:
            self.item.quality = value
    
    @property
    def sell_in(self):
        return self.item.sell_in

    @sell_in.setter
    def sell_in(self, value):
        self.item.sell_in = value

    @abstractmethod
    def update_quality(self):
        raise NotImplementedError()


class CommonQualityUpdater(QualityUpdater):
    def update_quality(self):
        self.sell_in-= 1
        if self.sell_in <= 0:
            self.quality-= 2
        else:
            self.quality-= 1


class LegendaryQualityUpdater(QualityUpdater):
    """
    Legendary item Sulfuras does not need sell_in and it's quality should remain constant, no other legendary items listed
    """
    @quality.setter
    def quality(self, value):
        pass

    def update_quality(self):
        pass


class AgedQualityUpdater(QualityUpdater):
    def update_quality(self):
        self.sell_in-= 1
        self.quality+= 1


class BackstageQualityUpdater(QualityUpdater):
    def update_quality(self):
        self.sell_in-= 1
        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in > 5 and self.sell_in <= 10:
            self.quality+= 2
        elif self.sell_in > 0 and self.sell_in <= 5:
            self.quality+= 3
        elif self.sell_in <= 0:
            self.quality = 0


class QualityUpdateFactory(object):
    def __init__(self, item):
        self.item = item

    def resolve(self) -> QualityUpdater:
        #TODO: implement this
        pass
