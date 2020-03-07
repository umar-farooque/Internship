from .. import admin
from flask import Flask, render_template


@admin.route('/manage/users')
def manage_users():
    return render_template('manage/users/index.html')