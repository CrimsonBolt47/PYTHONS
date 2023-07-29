from flask import Flask, render_template #render returns html file

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html") #html file should be in "templates" file

@app.route("/about/")  #add /about/ to the website of the first one
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)    #when script executed: __name__="__main__"
                           #when script imported: __name__="app.py"

