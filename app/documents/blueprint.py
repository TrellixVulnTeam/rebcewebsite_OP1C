from flask import Blueprint, flash, render_template, request, redirect, url_for,g,current_app
from app import app,db
from documents.forms import DocumentForm, ImageForm
import os

documents = Blueprint('documents', __name__, template_folder='templates')

@documents.route('/')
@login_required #will handle the next_page redirect alone
def index():
    return document_list('documents/index.html', documents) # checks if search was used and returns paginated result

@documents.route('/tags/')
@login_required #will handle the next_page redirect alone
def tag_index():
    tags = Tag.query.order_by(Tag.name)
    return object_list('documents/tag_index.html', tags)

@documents.route('/tags/<slug>/')
@login_required #will handle the next_page redirect alone
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    documents = tag.documents.query.filter(Document.author == g.user)  \
                                    .order_by(Document.created_timestamp.desc())
    return document_list('documents/tag_detail.html', documents, tag=tag)
    # return object_list('documents/tag_detail.html', documents, tag=tag)

####### The detail function
@documents.route('/<slug>/')
@login_required #will handle the next_page redirect alone
def detail(slug):
    document = Document.query.filter(and_(Document.slug == slug,
                                              Document.author == g.user)) \
                                .first_or_404()
    return render_template('documents/detail.html', document=document)

######## CREATING and EDITING and DELETING Posts
#this function is being hit twice. First time when the user opens the page and
#and second time when the user posts the form

@documents.route('/<slug>/edit/', methods=['GET', 'POST'])
@login_required
def edit(slug):
    document = Document.query.filter(and_(Document.slug == slug,
                                          Document.author == g.user)) \
                            .first_or_404()
    if request.method == 'POST':
        form = DocumentForm(request.form, obj=document)
        if form.validate():
            document = form.save_document(document)
            image_url = upload_image_file(request.files.get('image'))
            if image_url:
                document.imageUrl = image_url
            db.session.add(document)
            db.session.commit()
            flash('Document "%s" has been saved.' % document.title, 'success')
            return redirect(url_for('documents.detail', slug=document.slug))
    else:
        form = DocumentForm(obj=document)

    return render_template('documents/edit.html', document=document, form=form)
