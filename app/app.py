
from os import environ

from flask import (
    abort, Flask, redirect, render_template,
    request, url_for
    )

from .database import Database
from .forms import EditPromptForm, PromptForm, TagsetForm
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
    edit_form = EditPromptForm()
    db = Database()
    prompts = sorted(db.get_prompts_list())

    if request.method == "GET":
        return render_template(
            "prompts.html",
            prompts=prompts,
            tagset_form=tagset_form,
            prompt_form=prompt_form,
            edit_form=edit_form
            )

    if request.method == "POST":
        if tagset_form.validate_on_submit():
            scraper = TagSetScraper(tagset_form.url.data)
            prompts = scraper.get_original()
            db.create_prompt_list(prompts)

        if prompt_form.validate_on_submit():
            db.create_prompt(prompt_form.prompt.data)

        if edit_form.validate_on_submit():
            db.edit_prompt_body(edit_form.id.data, edit_form.body.data)
            return redirect(url_for('prompts'))

        return redirect(url_for('prompts'))


@app.route('/prompts/delete/<int:id>', methods=('POST',))
def prompt_delete(id):
    db = Database()
    db.delete_prompt(id)
    return redirect(url_for('prompts'))


@app.route('/500')
def error500():
    abort(500)
