from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def test():
    return "Does this work? Yes."

@app.route("/application-form")
def index_page():
    # Return this as a strange
    return render_template("application-form.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application", methods=["POST"])
def result_page():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salaryreq")
    job = request.form.get("job")

    return """

    <!DOCTYPE html>
    <html>
        <head>
            <title>Thanks for inquiring!</title>
            <link rel="stylesheet" type="text/css" href="static/styles.css">
        </head>
        <body>
            <center>
                <h1>Melinquiry Melanaged</h1>
                <div id="instructions"><p>Inquiry received! Thanks for applying for the %s role, %s %s. If our budget accommodates your $%s requirements, we'll be in touch. In the meantime: melon on!</p></div>
            </center>
        </body>
    </html>""" % (job, firstname, lastname, salary)

if __name__ == "__main__":
    app.run(debug=True)
