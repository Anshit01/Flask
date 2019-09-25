from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/about')
def about():
    if(request.args.get('q')):
        return render_template('about.html', var = request.args.get('q'))
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug = True)