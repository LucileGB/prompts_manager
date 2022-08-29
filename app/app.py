
from os import environ

from flask import abort, flash, Flask, redirect, render_template, request, url_for
from markupsafe import escape

from .database import Database
from .forms import TagsetForm, PromptForm
from .scraper import TagSetScraper

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
    
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prompts", methods=['GET', 'POST'])
def prompts():
    tagset_form = TagsetForm()
    prompt_form = PromptForm()

    prompts = [{'content': 'Message One',
            'collection': 'Message One Content'},
        {'content': 'Message Two',
            'collection': 'Message Two Content'}
        ]
    
    if request.method == "GET":
        return render_template("prompts.html",
                                prompts=prompts,
                                tagset_form=tagset_form,
                                prompt_form=prompt_form
            )

    if request.method == "POST":
        if tagset_form.validate_on_submit():
            print(tagset_form.url.data)
            scraper = TagSetScraper(tagset_form.url.data)
            prompts = scraper.get_original()
            print(prompts)

        if prompt_form.validate_on_submit():
            print(tagset_form)

        return render_template("prompts.html",
                                prompts=prompts,
                                tagset_form=tagset_form,
                                prompt_form=prompt_form
            )

@app.route('/500')
def error500():
    abort(500)