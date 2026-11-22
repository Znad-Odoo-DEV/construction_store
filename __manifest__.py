# -*- coding: utf-8 -*-
{
    'name': "Construction Store",
    'summary': "The site stores, as locations of the native inventory",
    'description': """
Construction Store
==================

A site store is a location, an item is a product, and what is on the shelf is
a quant. What Odoo does not have is the one thing a construction site cares
about - which project a store belongs to - so that is what this adds: a
project and a storekeeper on the location, and a project on the transfer.

Quantities only. Nothing here posts an accounting entry: the cost of materials
is already on the project through the bill that bought them, and valuing the
same material again on issue would count it twice.
""",
    'author': "Znad-Odoo-DEV",
    'website': "https://github.com/Znad-Odoo-DEV/construction_store",
    'category': 'Inventory',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['stock', 'project', 'hr'],
    'data': [
        'views/stock_location_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
}
