# Importing the essentials
from flask import Flask, render_template
from web import number_of_deaths, number_of_patians, number_of_recovered, lates_news
from post import posts


app =Flask(__name__)


@app.route('/')
def index():
   return render_template('base.html', post=posts)

@app.route('/test')
def xedni():
   return render_template('test.html', post=posts)

# mainloop
if __name__ == '__main__':
    app.run(debug=False)
# print(posts)