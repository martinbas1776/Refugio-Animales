# -*- coding: utf-8 -*-
{
    'name': "refugio_animales",

    'summary': "gestionar los animales, cuidadores y las instalaciones del refugio.",

    'description': """
tercer proyecto en Odoo.
Modulo realizado por Alicia Ramos.
La mejor desarrolladora actualmente.
Si algo falla no es culpa mia.
    """,

    'author': "Dam66",
    'website': "https://tamagotchi-official.com/es/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'reports/animal_report.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    # only loaded in demonstration mode
    'demo': [],
}

