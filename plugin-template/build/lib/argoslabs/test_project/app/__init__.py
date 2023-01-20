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
ARGOS LABS plugin module sample
"""
# Authors
# ===========
#
# * Jerry Chae
#
# Change Log
# --------
#
#  * [2019/03/08]
#     - add icon
#  * [2018/11/28]
#     - starting

################################################################################
import os
import sys
from alabs.common.util.vvargs import ModuleContext, func_log, \
    ArgsError, ArgsExit, get_icon_path


################################################################################
# @func_log
# def helloworld(mcxt, argspec):
#     """
#     plugin job function
#     :param mcxt: module context
#     :param argspec: argument spec
#     :return: True
#     """
#     mcxt.logger.info('>>>starting...')
#     try:
#         outstr = 'Hello world %s' % ','.join(argspec.name)
#         if argspec.opt:
#             outstr += f' with {argspec.opt}'
#         print(outstr, end='')
#         mcxt.logger.info('>>>end...')
#         return 0
#     except Exception as err:
#         msg = str(err)
#         mcxt.logger.error(msg)
#         sys.stderr.write('%s%s' % (msg, os.linesep))
#         return 99
#     finally:
#         sys.stdout.flush()
#         mcxt.logger.info('>>>end...')
import re
@func_log
def remove_special_characters(mcxt, argspec):
        try:
            outstr = re.sub(r"[^a-zA-Z0-9\s]", "", str(argspec.string))
            if argspec.opt:
                outstr += f' with {argspec.opt}'
            print(outstr, end='')
            mcxt.logger.info('>>>end...')
            return 0
        except Exception as err:
            msg = str(err)
            mcxt.logger.error(msg)
            sys.stderr.write('%s%s' % (msg, os.linesep))
            return 99
        finally:
            sys.stdout.flush()
            mcxt.logger.info('>>>end...')
    #return re.sub(r"[^a-zA-Z0-9\s]", "", argspec.string)



################################################################################
def _main(*args):
    """
    Build user argument and options and call plugin job function
    :param args: user arguments
    :return: return value from plugin job function
    """
    try:
        with ModuleContext(
            owner='ARGOS-LABS-DEMO',
            group='test_project',
            version='1.0',
            platform=['windows', 'darwin', 'linux'],
            output_type='text',
            display_name='Hello World',
            icon_path=get_icon_path(__file__),
            description='Hello World friends',
        ) as mcxt:
            # ##################################### for app dependent parameters
            mcxt.add_argument('string', nargs='+', help='Give the string that had some special charecters')
            # ######################################## for app dependent options
            mcxt.add_argument('-o', '--opt',
                              display_name='Opt Arg', show_default=True,
                              help='Give the string that had some special charecters')

            argspec = mcxt.parse_args(args)
            return remove_special_characters(mcxt, argspec)
    except Exception as e:
        sys.stderr.write(f'Error: {str(e)}')
        return 98


################################################################################
def main(*args):
    try:
        return _main(*args)
    except ArgsError as err:
        sys.stderr.write('Error: %s\nPlease -h to print help\n' % str(err))
    except ArgsExit as _:
        pass
