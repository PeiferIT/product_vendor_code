{
    'name': 'Product Vendor Code in Sale/Purchase/Mrp/Invoicing/POS',
    'category': 'Sale',
    'summary': 'Product Vendor Code in Sale/Purchase/Mrp/Invoicing/POS',
    'description': """ Product Vendor Code in Sale/Purchase/Mrp/Invoicing/POS""",
    'version': '15.3.2.1',
    'currency': 'EUR',
    'sequence': 1,
    'license': 'LGPL-3',
    'depends': ['point_of_sale','sale','purchase','account','mrp'],
    'data': [
        "views/product_views.xml",
    ],
    'assets': {
        'point_of_sale.assets': [
            "product_vendor_code/static/src/js/db.js",
        ],
    },
    'installable': True,
    'auto_install': False,
}
