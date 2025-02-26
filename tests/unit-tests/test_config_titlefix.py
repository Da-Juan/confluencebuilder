# SPDX-License-Identifier: BSD-2-Clause
# Copyright 2020-2023 Sphinx Confluence Builder Contributors (AUTHORS)

from tests.lib.testcase import ConfluenceTestCase
from tests.lib.testcase import setup_builder
from tests.lib import parse
import os


class TestConfluenceConfigTitlefix(ConfluenceTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.config['root_doc'] = 'titlefix'
        cls.dataset = os.path.join(cls.datasets, 'titlefix')

    @setup_builder('confluence')
    def test_storage_config_titlefix_none(self):
        out_dir = self.build(self.dataset)

        with parse('titlefix', out_dir) as data:
            page_ref = data.find('ri:page')
            self.assertIsNotNone(page_ref)
            self.assertEqual(page_ref['ri:content-title'],
                'titlefix-child')

        with parse('titlefix-child', out_dir) as data:
            page_ref = data.find('ri:page')
            self.assertIsNotNone(page_ref)
            self.assertEqual(page_ref['ri:content-title'], 'titlefix')

    @setup_builder('confluence')
    def test_storage_config_titlefix_postfix(self):
        config = dict(self.config)
        config['confluence_publish_postfix'] = '-mypostfix'

        out_dir = self.build(self.dataset, config=config)

        with parse('titlefix', out_dir) as data:
            page_ref = data.find('ri:page')
            self.assertIsNotNone(page_ref)
            self.assertEqual(page_ref['ri:content-title'],
                'titlefix-child-mypostfix')

        with parse('titlefix-child', out_dir) as data:
            page_ref = data.find('ri:page')
            self.assertIsNotNone(page_ref)
            self.assertEqual(page_ref['ri:content-title'], 'titlefix-mypostfix')

    @setup_builder('confluence')
    def test_storage_config_titlefix_prefix(self):
        config = dict(self.config)
        config['confluence_publish_prefix'] = 'myprefix-'

        out_dir = self.build(self.dataset, config=config)

        with parse('titlefix', out_dir) as data:
            page_ref = data.find('ri:page')
            self.assertIsNotNone(page_ref)
            self.assertEqual(page_ref['ri:content-title'],
                'myprefix-titlefix-child')

        with parse('titlefix-child', out_dir) as data:
            page_ref = data.find('ri:page')
            self.assertIsNotNone(page_ref)
            self.assertEqual(page_ref['ri:content-title'], 'myprefix-titlefix')

    @setup_builder('confluence')
    def test_storage_config_titlefix_prefix_and_postfix(self):
        config = dict(self.config)
        config['confluence_publish_prefix'] = 'myprefix-'
        config['confluence_publish_postfix'] = '-mypostfix'

        out_dir = self.build(self.dataset, config=config)

        with parse('titlefix', out_dir) as data:
            page_ref = data.find('ri:page')
            self.assertIsNotNone(page_ref)
            self.assertEqual(page_ref['ri:content-title'],
                'myprefix-titlefix-child-mypostfix')

        with parse('titlefix-child', out_dir) as data:
            page_ref = data.find('ri:page')
            self.assertIsNotNone(page_ref)
            self.assertEqual(page_ref['ri:content-title'],
                'myprefix-titlefix-mypostfix')

    @setup_builder('confluence')
    def test_storage_config_titlefix_ignore_root(self):
        config = dict(self.config)
        config['confluence_ignore_titlefix_on_index'] = True
        config['confluence_publish_postfix'] = '-mypostfix'
        config['confluence_publish_prefix'] = 'myprefix-'

        out_dir = self.build(self.dataset, config=config)

        with parse('titlefix', out_dir) as data:
            page_ref = data.find('ri:page')
            self.assertIsNotNone(page_ref)
            self.assertEqual(page_ref['ri:content-title'],
                'myprefix-titlefix-child-mypostfix')

        with parse('titlefix-child', out_dir) as data:
            page_ref = data.find('ri:page')
            self.assertIsNotNone(page_ref)
            self.assertEqual(page_ref['ri:content-title'], 'titlefix')
