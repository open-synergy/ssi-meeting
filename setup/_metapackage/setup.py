import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-meeting",
    description="Meta package for open-synergy-ssi-meeting Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_meeting_outsource_work',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
