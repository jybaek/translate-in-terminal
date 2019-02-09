#!/usr/bin/env python
# coding=utf8

"""
====================================
 :mod: Test case
====================================
.. module author:: Raven Lim <hong18s@gmail.com>
.. note:: MIT License
"""

import os
import unittest

from translate.translate import parser, translate, main, clipboard

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

try:
    import pyperclip
    pyperclip.paste()
    CLIPBOARD = True
except pyperclip.PyperclipException:
    CLIPBOARD = False


################################################################################
class TestUnit (unittest.TestCase):
    """
    Test Unit for Locate Image
    """

    # ==========================================================================
    def setUp(self):
        pass

    # ==========================================================================
    def tearDown(self):
        pass

    # ==========================================================================
    def test_010_argument_clipboard(self):
        if not CLIPBOARD:
            return
        argspec = parser('-c'.split())
        self.assertTrue('clipboard' in argspec)
        self.assertTrue(argspec.clipboard)

    # ==========================================================================
    def test_011_argument_dumb(self):
        argspec = parser('-d'.split())
        self.assertTrue('dumb' in argspec)
        self.assertTrue(argspec.dumb)

    # ==========================================================================
    def test_012_argument_data(self):
        argspec = parser('Hello'.split())
        self.assertTrue('data' in argspec)
        self.assertEqual('Hello', ''.join(argspec.data))

    # ==========================================================================
    def test_020_mixed_arguments(self):
        argspec = parser('Hello -d'.split())
        self.assertTrue('data' in argspec)
        self.assertTrue('dumb' in argspec)
        self.assertEqual('Hello', ''.join(argspec.data))
        self.assertTrue(argspec.dumb)

    # ==========================================================================
    def test_021_mixed_arguments(self):
        argspec = parser('-d Hello'.split())
        self.assertTrue('data' in argspec)
        self.assertTrue('dumb' in argspec)
        self.assertEqual('Hello', ''.join(argspec.data))
        self.assertTrue(argspec.dumb)

    # ==========================================================================
    def test_022_mixed_arguments(self):
        if not CLIPBOARD:
            return
        pyperclip.copy('Hi')
        argspec = parser('-c Hello'.split())
        self.assertTrue('data' in argspec)
        self.assertTrue('clipboard' in argspec)
        self.assertEqual('Hi', ''.join(argspec.data))
        self.assertTrue(argspec.clipboard)

    # ==========================================================================
    def test_023_mixed_arguments(self):
        if not CLIPBOARD:
            return
        pyperclip.copy('Hi')
        argspec = parser('-c Hello -d'.split())
        self.assertTrue('data' in argspec)
        self.assertTrue('clipboard' in argspec)
        self.assertTrue('dumb' in argspec)
        self.assertEqual('Hi', ''.join(argspec.data))
        self.assertTrue(argspec.clipboard)
        self.assertTrue(argspec.dumb)

    # ==========================================================================
    def test_030_translate(self):
        text = translate(['Hello'])
        self.assertEqual('여보세요', text)

    # ==========================================================================
    def test_031_translate_statement(self):
        text = translate('Hello World'.split())
        self.assertEqual('안녕하세요 세계', text)

    # ==========================================================================
    def test_032_translate_statement_with_cr(self):
        text = translate('Hello, World.\n Good Morning'.split())
        self.assertEqual('안녕, 세상. 좋은 아침', text)

    # ==========================================================================
    def test_032_translate_clipboard_text(self):
        if not CLIPBOARD:
            return
        pyperclip.copy('Hello World')
        text = translate('Hello, World.\n Good Morning'.split())
        self.assertEqual('안녕, 세상. 좋은 아침', text)


