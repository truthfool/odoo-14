# -*- coding: utf-8 -*-
# Copyright 2020 OpenG2P (https://openg2p.org)
# @author: Salton Massally <saltonmassally@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api
from odoo.exceptions import UserError


class NoCopyMixin(models.AbstractModel):
    _name = "openg2p.mixin.no_copy"
    _description = "OpenG2P Mixin: No Copy"

    def copy(self, default=None):
        raise UserError("Duplicate operation not supported")
