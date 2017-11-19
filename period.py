# -*- coding: utf-8 -*-

""" Set period (month and year) dor financial docs """

import datetime
import sys

class Period:

    _month = None
    _year = None

    def __init__(self):
        self._month = datetime.datetime.now().month - 1
        self._year = datetime.datetime.now().year

    def get_period(self):
        return [str(self._month), str(self._year)] if self._month != 0 else [str(12), str(self._year-1)]

    def set_period(self, new_period):
        self._month = new_period[0]
        self._year = new_period[1]
        sys.stdout.write('Отчетный период %s %s установлен в качестве текущего\n' % (self._month, self._year))