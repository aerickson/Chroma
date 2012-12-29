#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Chroma Test Suite
~~~~~~~~~~~~~~~~~~~

A series of unittests to check the basic functionality of the Chroma API.

"""

import unittest
import argparse

# Path hack. (for importing)
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))
import chroma

class ChromaTestSuite(unittest.TestCase):
    def setUp(self):
        c = chroma.Color()

    def test_color_initialization(self):
        """
        Test construction (and setters) of color object with all formats
        Compare against known rgb256 conversion
        """
        rgb256_value = (85,119,153)
        # Default format
        self.assertEqual(chroma.Color('#557799').rgb256, rgb256_value)
        # HEX
        self.assertEqual(chroma.Color('#557799', 'HEX').rgb256, rgb256_value)
        # RGB
        self.assertEqual(chroma.Color((0.333, 0.465, 0.6), 'RGB').rgb256, rgb256_value)
        # RGB256
        self.assertEqual(chroma.Color((85, 119, 153), 'RGB256').rgb256, rgb256_value)
        # HLS
        self.assertEqual(chroma.Color((0.583, 0.467, 0.286), 'HLS').rgb256, rgb256_value)
        # HSV
        self.assertEqual(chroma.Color((0.583, 0.444, 0.60), 'HSV').rgb256, rgb256_value)
        # Error
        self.assertRaises(Exception, chroma.Color, (210, 44, 60), 'ERROR')


if __name__ == '__main__':
    # Run unit tests
    unittest.main()
