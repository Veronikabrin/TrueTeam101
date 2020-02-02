from flask import Flask, redirect, render_template, make_response
from forms.report_form import ReportForm
from forms.response_form import ResponseForm
from model import Model

STATIC_FOLDER = 'templates/'

app = Flask(__name__, static_folder=STATIC_FOLDER)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",  # todo
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


@app.route('/')
def index():
    return redirect('/submit')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    report_form = ReportForm()
    if report_form.validate_on_submit():
        Model.send_report(report_form.name.data)
        return redirect('/response')
    return render_template('submit.html', form=report_form)


@app.route('/response', methods=['GET', 'POST'])
def response():
    response_form = ResponseForm()
    response_form.name.data = Model.get_response()
    return make_response(render_template('response.html', form=response_form))


if __name__ == '__main__':
      app.run(host='0.0.0.0',port=5000)
