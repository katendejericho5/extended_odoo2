{
    'name': 'Custom RFQ',
    'version': '1.0',
    'depends': [
        'purchase',
        'hr',
        'product',
        'base'
    ],
    'author': 'Jericho Katende',
    'category': 'Purchases',
    'description': """
    This module extends the standard Odoo Purchase application to add:
    - Multiple vendor assignment to RFQs
    - Bid management
    - Winning bid selection
    - Purchase request workflow
    """,
    "data": [
        "security/ir.model.access.csv",
        "views/purchase_order_views.xml"
    ],
    'installable': True,
    'application': False,
}