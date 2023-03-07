# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class EmployeeExpenseAccount(models.Model):
    _name = "calendar.event"
    _inherit = [
        "calendar.event",
        "mixin.outsource_work_object"
    ]
