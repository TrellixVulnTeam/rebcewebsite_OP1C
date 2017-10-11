from flask import Blueprint, flash, render_template, request, redirect, url_for,g,current_app
from app import app
import os

documents = Blueprint('documents', __name__, template_folder='templates')

@documents.route('/')
def index():
    return document_list('documents/index.html') # checks if search was used and returns paginated result

# @documents.route('/tags/<slug>/')
# def tag_detail(slug):
#     tag = Tag.query.filter(Tag.slug == slug).first_or_404()
#     documents = tag.documents.query.filter(Document.author == g.user)  \
#                                     .order_by(Document.created_timestamp.desc())
#     return document_list('documents/tag_detail.html', documents, tag=tag)
#     # return object_list('documents/tag_detail.html', documents, tag=tag)
#
# #
