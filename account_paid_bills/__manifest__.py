# License OPL-1 (https://www.odoo.com/documentation/16.0/legal/licenses.html).
{
    'name': 'Account Paid Bills',
    'version': '16.0.1.0.0',
    'summary': 'Account Paid Bills',
    'description': 'Account Paid Bills',
    'category': 'All',
    'author': 'SergeyVanyarha',
    "website": "https://github.com/SergeyVanyarha/ViewPaidBills",
    'license': 'OPL-1',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/get_paid_bills_views.xml',
    ],
}
