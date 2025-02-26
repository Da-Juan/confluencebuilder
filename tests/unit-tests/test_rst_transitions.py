# SPDX-License-Identifier: BSD-2-Clause
# Copyright 2016-2023 Sphinx Confluence Builder Contributors (AUTHORS)

from tests.lib.testcase import ConfluenceTestCase
from tests.lib.testcase import setup_builder
from tests.lib import parse
import os


class TestConfluenceRstTransitions(ConfluenceTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.dataset = os.path.join(cls.datasets, 'rst', 'transitions')

    @setup_builder('confluence')
    def test_storage_rst_transitions_default(self):
        out_dir = self.build(self.dataset)

        with parse('index', out_dir) as data:
            hr = data.find('hr')
            self.assertIsNotNone(hr)
