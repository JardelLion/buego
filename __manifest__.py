{
    'name': 'BueGo',
    'odoo_version': "18.0.0",
    'version': '1.0.0',
    'description': """BweGo is a collaborative mobility platform designed to connect people traveling to similar destinations, helping them organize shared transportation and reduce individual travel costs.

        The platform enables users to publish travel intentions, discover people with compatible routes, create travel groups, coordinate meeting points, and share transportation expenses.

        Key Features:
        - User registration and profile management.
        - GPS-based location and destination selection.
        - Travel intentions for immediate, scheduled, and recurring trips.
        - Intelligent route matching based on origin, destination, distance, and departure time.
        - Travel group creation and participant management.
        - Meeting point coordination.
        - Shared transportation cost calculation and management.
        - Notifications and travel status updates.
        - Interactive maps and location visualization.
        - Integration capabilities with Traccar for authorized GPS tracking.
        - Administrative tools for platform management and monitoring.

        BweGo is built on Odoo, providing a centralized backend for user management, business logic, data management, and platform administration.

        Our mission is simple:

        "Let's go together. Spend less."

        BweGo — Collaborative mobility made simple.""",
    'summary': 'Collaborative mobility platform that connects people with similar routes to organize shared trips and split transportation costs.',
    'author': 'Jardel Elias Bernardo',
    'website': 'https://github.com/JardelLion/buego',
    'license': 'LGPL-3',
    'category': 'Services',
    'depends': ['contacts', 'base_geolocalize'],
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/buego_dashboard_views.xml",
        "views/res_partner_views.xml"
        
    ],
    'demo': [],
    'auto_install': False,
    'application': True,
    'assets': {
        
    }
}