from .. import admin
from flask import Flask, render_template


@admin.route('/manage/courses')
def manage_courses():
    return render_template('manage/courses/index.html')