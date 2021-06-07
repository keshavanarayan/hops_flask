from flask import Flask
import ghhops_server as hs

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/test",
    name="test",
    inputs=[
        hs.HopsInteger(" number", "N", "test parameter"),
        hs.HopsInteger(" optional ","O","optional parameter",hs.HopsParamAccess.LIST, optional= True),
        hs.HopsInteger(" default ","D", "default parameter",hs.HopsParamAccess.ITEM,  default= 10)

    ],
    outputs=[
        hs.HopsInteger("list", "I", "list of numbers", hs.HopsParamAccess.LIST)
    ]
)
def test(n, o, d):
    
    return o

if __name__ == "__main__":
    app.run(debug=True)

