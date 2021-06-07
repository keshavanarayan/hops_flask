from flask import Flask
import ghhops_server as hs

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/test",
    name="test",
    inputs=[
        hs.HopsInteger(" number", "n", "test parameter"),
    ],
    outputs=[
        hs.HopsInteger("list", "I", "list of numbers" ,hs.HopsParamAccess.TREE)
    ]
)
def test(n):

    nested = [[j for j in range(n)] for i in range(n)]      
    return nested

if __name__ == "__main__":
    app.run(debug=True)

