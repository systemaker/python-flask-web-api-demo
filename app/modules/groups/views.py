#!/usr/bin/python
# -*- coding: utf-8 -*-

# ------- IMPORT DEPENDENCIES ------- 
import datetime
import sendgrid
from flask import request, render_template, flash, current_app, redirect, abort, jsonify, url_for
from forms import *
from time import time
from flask_login import login_required, current_user

# ------- IMPORT LOCAL DEPENDENCIES  -------
from app import app, logger
from . import groups_page
from models import Groups
from app.helpers import *

# -------  ROUTINGS AND METHODS  ------- 


# All groups
@groups_page.route('/')
@groups_page.route('/<int:page>')
def groups(page=1):
    try:
        m_groups = Groups()
        list_groups = m_groups.all_data(page, app.config['LISTINGS_PER_PAGE'])
        # html or Json response
        if request.is_xhr == True:
            return jsonify(data = [{'id' : d.id, 'title' : d.title, 'description' : d.description} for d in list_groups.items])
        else:
            return render_template("groups/index.html", list_groups=list_groups, app = app)

    except Exception, ex:
        print("------------ ERROR  ------------\n" + str(ex.message))
        #abort(404)



    

# Show group
@groups_page.route('/show/<int:id>')
def show(id=1):
    try:
        m_groups = Groups()
        m_group = m_groups.read_data(id)
        # html or Json response
        if request.is_xhr == True:
            return jsonify(data = m_group)
        else:
            return render_template("groups/show.html", group=m_group, app = app)

    except Exception, ex:
        print("------------ ERROR  ------------\n" + str(ex.message))
        flash(str(ex.message), category="warning")
        abort(404)


# New group
@groups_page.route('/new', methods=['GET', 'POST'])
def new():
    try :

        form = Form_Record_Add(request.form)

        if request.method == 'POST':
            if form.validate():
                groups = Groups()

                sanitize_form = {
                    'title' : form.title.data,
                    'description' : form.description.data,
                    'is_active' : form.is_active.data,
                    'created_at' : form.created_at.data
                }

                groups.create_data(sanitize_form)
                logger.info("Adding a new record.")
                
                if request.is_xhr == True:
                    return jsonify(data = { message :"Record added successfully.", form: form }), 200, {'Content-Type': 'application/json'}
                else : 
                    flash("Record added successfully.", category="success")
                    return redirect("/groups")

        form.action = url_for('groups_page.new')
        form.created_at.data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

         # html or Json response
        if request.is_xhr == True:
            return jsonify(data = form), 200, {'Content-Type': 'application/json'}
        else:
            return render_template("groups/edit.html", form=form,  title='New', app = app)
    except Exception, ex:
        print("------------ ERROR  ------------\n" + str(ex.message))
        flash(str(ex.message), category="warning")
        abort(404)


# Edit group
@groups_page.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id=1):
    try : 

        # check_admin()

        groups = Groups()
        group = groups.query.get_or_404(id)

        form = Form_Record_Add(request.form)

        if request.method == 'POST':
            if form.validate():

                sanitize_form = {
                    'title' : form.title.data,
                    'description' : form.description.data,
                    'is_active' : form.is_active.data,
                    'created_at' : form.created_at.data
                }

                groups.update_data(group.id, sanitize_form)
                logger.info("Editing a new record.")
                
                if request.is_xhr == True:
                    return jsonify(data = { message :"Record updated successfully.", form: form }), 200, {'Content-Type': 'application/json'}
                else : 
                    flash("Record updated successfully.", category="success")
                    return redirect("/groups")

        form.action = url_for('groups_page.edit', id = group.id)
        form.title.data = group.title
        form.description.data = group.description
        form.is_active.data = group.is_active
        form.created_at.data = string_timestamp_utc_to_string_datetime_utc(group.created_at, '%Y-%m-%d')

        # html or Json response
        if request.is_xhr == True:
            return jsonify(data = form), 200, {'Content-Type': 'application/json'}
        else:
            return render_template("groups/edit.html", form=form, title='Edit', app = app)
    except Exception, ex:
        print("------------ ERROR  ------------\n" + str(ex.message))
        flash(str(ex.message), category="warning")
        abort(404)



# Delete group
@groups_page.route('/delete/<int:id>')
def delete(id=1):
    try:
        groups = Groups()
        group = groups.query.get_or_404(id)
        groups.delete_data(group.id)
        # html or Json response
        if request.is_xhr == True:
            return jsonify(data = {message:"Record deleted successfully.", group : m_group})
        else:
            flash("Record deleted successfully.", category="success")
            return redirect(url_for('groups_page.groups'))

    except Exception, ex:
        print("------------ ERROR  ------------\n" + str(ex.message))
        flash(str(ex.message), category="warning")
        abort(404)