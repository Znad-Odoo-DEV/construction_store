# -*- coding: utf-8 -*-
"""A store belongs to a project, and says who keeps it.

A location knows its warehouse and its company, and on a construction site that
is not enough to answer "what is on this site's store" without knowing which
project the store belongs to.
"""
from odoo import fields, models


class StockLocation(models.Model):
    _inherit = 'stock.location'

    construction_project_id = fields.Many2one(
        'project.project', string="Construction Project", index=True,
        help="The job this store serves. Set it and stock can be read per "
             "project as well as per warehouse.",
    )
    construction_storekeeper_id = fields.Many2one(
        'hr.employee', string="Storekeeper",
        help="Who answers for what is on these shelves.",
    )
