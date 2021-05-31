# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


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


class ConjuredQualityUpdater(QualityUpdater):
    def update_quality(self):
        self.sell_in-= 1
        if self.sell_in <= 0:
            self.quality-= 4
        else:
            self.quality-= 2


class QualityUpdateFactory(object):
    def resolve(self, item) -> QualityUpdater:
        name = item.name.lower()
        if name.startswith("conjured"):
            return ConjuredQualityUpdater(item)
        elif name.startswith("backstage"):
            return BackstageQualityUpdater(item)
        elif name.startswith("sulfuras"):
            return LegendaryQualityUpdater(item)
        elif name == "aged brie":
            return AgedQualityUpdater(item)
        else:
            return CommonQualityUpdater(item)

factory = QualityUpdateFactory()