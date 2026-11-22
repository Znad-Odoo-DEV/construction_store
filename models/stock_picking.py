# -*- coding: utf-8 -*-
"""A transfer says which job it served."""
from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    construction_project_id = fields.Many2one(
        'project.project', string="Construction Project", index=True,
        help="The job this transfer served: the site it was consumed on, or "
             "the store it was received into.",
    )
