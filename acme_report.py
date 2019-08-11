#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product


# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
      name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
      price = randint(5, 100)
      weight = randint(5, 100)
      flammability = uniform(0, 2.5)
      product = Product(name, price, weight, flammability)
      products.append(product)
    return products


def inventory_report(products):
    unique_set = set()
    #names = set([p.name for p in products])
    avg_price = sum([p.price for p in products]) / len(products)
    avg_weight = sum([p.weight for p in products]) / len(products) 
    avg_flammability = sum([p.flammability for p in products]) / len(products)   
    for product in products:
        unique_set.add(product.name)
        
    
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('unique products',len(unique_set))
    print(f'Average price: {avg_price}')
    print(f'Average weight: {avg_weight}')
    print(f'Average flammability: {avg_flammability}')


if __name__ == '__main__':
    inventory_report(generate_products())