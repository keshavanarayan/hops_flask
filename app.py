from flask import Flask
import ghhops_server as hs

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/test",
    name="test",
    inputs=[
        hs.HopsString("Name", "N", "Your name"),
    ],
    outputs=[
        hs.HopsString("Welcome", "W", "Welcome to")
    ]
)
def test(n):

    return "Welcome, {} to the MaCAD Heroku server", format(n) 

if __name__ == "__main__":
    app.run(debug=True)

