from . import admin
from flask import Flask, render_template

@admin.route('/')
def index():
    return render_template('dashboard/index.html')

# @admin.route('/manage/users')
# def manage_users():
#     return render_template('manage/users/index.html')

