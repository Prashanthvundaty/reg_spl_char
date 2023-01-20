#!/usr/bin/env python
# coding=utf8
"""
====================================
 :mod:`argoslabs.test_project.app`
====================================
.. moduleauthor:: Jerry Chae <mcchae@argos-labs.com>
.. note:: ARGOS-LABS License

Description
===========
ARGOS LABS plugin module : unittest
"""

################################################################################
import os
import sys
from alabs.common.util.vvargs import ArgsError
from unittest import TestCase
# noinspection PyProtectedMember
from argoslabs.test_project.app import _main as main


################################################################################
class TU(TestCase):
    """
    TestCase for argoslabs.test_project.app
    """
    # ==========================================================================
    isFirst = True

    # ==========================================================================
    def test0000_init(self):
        self.assertTrue(True)

    # ==========================================================================
    def test0050_failure(self):
        """
        argoslabs.test_project.app
        :return: raise exception ArgsError
        """
        try:
            _ = main('-vvv')
            self.assertTrue(False)
        except Exception as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(True)

    # ==========================================================================
    # def test0100_success(self):
    #     """
    #     argoslabs.test_project.app tom jerry
    #     :return: True
    #     """
    #     try:
    #         r = main('tom', 'jerry')
    #         self.assertTrue(r == 0)
    #     except ArgsError as e:
    #         sys.stderr.write('\n%s\n' % str(e))
    #         self.assertTrue(False)

    # ==========================================================================
    # def test0110_success_with_opt(self):
    #     """
    #     argoslabs.test_project.app tom jerry
    #     :return: True
    #     """
    #     outfile = 'stdout.txt'
    #     try:
    #         r = main('Tom', 'Jerry', '--opt', 'Brad',
    #                  '--outfile', outfile)
    #         self.assertTrue(r == 0)
    #         with open(outfile, encoding='utf-8') as ifp:
    #             rs = ifp.read()
    #             print(rs)
    #             self.assertTrue(rs == 'Hello world Tom,Jerry with Brad')
    #     except ArgsError as e:
    #         sys.stderr.write('\n%s\n' % str(e))
    #         self.assertTrue(False)
    #     finally:
    #         if os.path.exists(outfile):
    #             os.remove(outfile)

    # ==========================================================================
    def test9999_quit(self):
        try:
            r = main('special# string')
            self.assertTrue(r == 0)
        except ArgsError as e:
            sys.stderr.write('\n%s\n' % str(e))
            self.assertTrue(False)

