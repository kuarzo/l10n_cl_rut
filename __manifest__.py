# -*- coding: utf-8 -*-
{
    'name': "Modulo - Validador de RUT",

    'summary': """
        Validador de RUT para Localización es_CL""",

    'description': """
        Este modulo tiene como finalidad proporcionar la localización del software en es_CL (Chile) y validar el RUT de Personas, Clientes y Proveedores de forma correcta.
    """,

    'author': "k0derz Systems SpA.",
    'website': "http://www.k0derz.systems",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
