#!/usr/bin/env python

import unittest

from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    def test_stealabilty(self):
        prod = Product('test product',10,20)
        self.assertEqual(prod.stealability(),'Kind stealable')
    def test_explode(self):
        prod = Product('test product',10,20)
        self.assertEqual(prod.explode(),'...boom')


        


if __name__ == '__main__':
    unittest.main()