# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Development Team: Stanislav WEB
"""

from __future__ import absolute_import
import unittest2 as unittest
from mock import Mock
from src import Controller, SrcError

class TestController(unittest.TestCase):
    """TestController class"""

    def test_init_exception(self):
        """ Controller.init() exception test """

        with self.assertRaises(SrcError) as context:
            Controller().scan_action({})
        self.assertTrue(SrcError == context.expected)

    def test_scan_action_exception(self):
        """ Controller.scan_action() exception test """

        controller = Controller.__new__(Controller)
        with self.assertRaises(SrcError) as context:
            controller.scan_action(params={
                'host': 'http://example.com',
                'port': 80
            })
        self.assertTrue(SrcError == context.expected)


if __name__ == "__main__":
    unittest.main()
