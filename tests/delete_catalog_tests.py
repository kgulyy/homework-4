# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopMarketPage
from tests.common import get_driver, Auth, Main, Shop, Catalog, Product


class DeleteCatalogTests(unittest.TestCase):
    NUMBER_OF_PRODUCTS = 5

    def setUp(self):
        self.driver = get_driver()
        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        Shop(self.driver).create()

    def tearDown(self):
        Shop(self.driver).remove()
        self.driver.quit()

    def test_remove_empty_catalog(self):
        shop_market_page = ShopMarketPage(self.driver)

        # check stub
        catalog_stub = shop_market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

        catalog = Catalog(self.driver)
        catalog.create()

        # check widget
        catalog_widget = shop_market_page.catalog_widget
        is_exist_catalog_widget = catalog_widget.is_exist()
        self.assertTrue(is_exist_catalog_widget)

        # check counter
        catalog_counter = shop_market_page.catalog_counter
        number_of_catalogs = catalog_counter.get_number_of_catalogs()
        self.assertEqual(1, number_of_catalogs)

        catalog.open()
        catalog.remove_saving_products()

        # check stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

        # check counter
        is_not_exist_counter = catalog_counter.is_not_exist()
        self.assertTrue(is_not_exist_counter)

    def test_remove_catalog_with_products(self):
        catalog = Catalog(self.driver)
        catalog.create()
        catalog.open()

        for i in xrange(self.NUMBER_OF_PRODUCTS):
            Product(self.driver).create()

        catalog.remove_with_products()
        self.driver.refresh()

        shop_market_page = ShopMarketPage(self.driver)

        # check stubs
        catalog_stub = shop_market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

        product_stub = shop_market_page.product_stub
        is_exist_product_stub = product_stub.is_exist()
        self.assertTrue(is_exist_product_stub)

        # check counters
        catalog_counter = shop_market_page.catalog_counter
        is_not_exist_catalog_counter = catalog_counter.is_not_exist()
        self.assertTrue(is_not_exist_catalog_counter)

        product_counter = shop_market_page.product_counter
        is_not_exist_product_counter = product_counter.is_not_exist()
        self.assertTrue(is_not_exist_product_counter)

    def test_remove_catalog_saving_products(self):
        catalog = Catalog(self.driver)
        catalog.create()
        catalog.open()

        for i in xrange(self.NUMBER_OF_PRODUCTS):
            Product(self.driver).create()

        catalog.remove_saving_products()
        self.driver.refresh()

        shop_market_page = ShopMarketPage(self.driver)

        # check catalog stub
        catalog_stub = shop_market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist()
        self.assertTrue(is_exist_catalog_stub)

        # check product widget
        product_widget = shop_market_page.product_widget
        is_exist_product_widget = product_widget.is_exist()
        self.assertTrue(is_exist_product_widget)

        # check counters
        catalog_counter = shop_market_page.catalog_counter
        is_not_exist_catalog_counter = catalog_counter.is_not_exist()
        self.assertTrue(is_not_exist_catalog_counter)

        product_counter = shop_market_page.product_counter
        number_of_products = product_counter.get_number_of_all_products()
        self.assertEqual(self.NUMBER_OF_PRODUCTS, number_of_products)
