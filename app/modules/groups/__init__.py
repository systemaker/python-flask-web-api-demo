#!/usr/bin/python
# -*- coding: utf-8 -*-

# ------- IMPORT DEPENDENCIES ------- 
from flask import Blueprint

groups_page = Blueprint('groups_page', __name__, template_folder='templates', static_folder='static', static_url_path='/static')

# ------- IMPORT LOCAL DEPENDENCIES  -------
from . import constants, models, forms, views
