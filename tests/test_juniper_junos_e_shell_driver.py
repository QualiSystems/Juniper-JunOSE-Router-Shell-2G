#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from driver import JuniperJunOSEShellDriver


class TestJuniperJunOSShellDriver(unittest.TestCase):
    def setUp(self):
        self._instance = JuniperJunOSEShellDriver()

    def test_init(self):
        self.assertIsNone(self._instance._cli)
