from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return '<p> Welcome To My! %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title> Proud Armenian </title> </head>\n<body>'''
instructions = '''
    <p>
    <h1 style="padding: 60px; background-color:red ; color: white"> PROUD </h1>
    <h1 style="padding: 60px; background-color:blue ; color: white"> ARMENIAN</h1>
    <h1 style="padding: 60px; background-color:orange ; color: white"> GIRL:) </h1>
    <br/>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/r_3SQs-Eaa0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <br/>
    <h1>Armenia is a nation, and former Soviet republic, in the mountainous Caucasus region between Asia and Europe. Among the earliest Christian civilizations, it’s defined by religious sites including the Greco-Roman Temple of Garni and 4th-century Etchmiadzin Cathedral, headquarters of the Armenian Church. Khor Virap Monastery is a pilgrimage site near Mount Ararat, a dormant volcano just across the border in Turkey.<h1/>
     <h1>Capital: Yerevan<h1/>
     <h1>Population: 2.965 million (2019) Eurostat<h1/>
     <h1>Continent: Asia<h1/>
     <h1>Currency: Armenian dram<h1/>
     <h1>President: Armen Sarkissian<h1/>
     <hr/>
    <em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
