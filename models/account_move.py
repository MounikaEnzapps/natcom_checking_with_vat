from odoo import fields,models,api
import convert_numbers
# from deep_translator import GoogleTranslator
from uuid import uuid4
import qrcode
from odoo.exceptions import UserError

import base64
import logging

from lxml import etree

logger = logging.getLogger(__name__)

from odoo import api, fields, models, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError
from odoo.tools import float_compare, date_utils, email_split, email_re
from odoo.tools.misc import formatLang, format_date, get_lang
from odoo import fields, models
import requests
import json
from datetime import datetime,date



class AccountMove(models.Model):
    _inherit = 'account.move'
    _order = "invoice_nat_times desc"

    advance_with_vat = fields.Char(string="Adavnce With Vat")
    a_advance_with_vat = fields.Char(string="A Adavnce With Vat")
