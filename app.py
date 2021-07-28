from flask import Flask
import ghhops_server as hs
import numpy as np
import string
import tensorflow as tf
import tensorflow.keras
from mymodel import prediction
import rhino3dm as rg


# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)
@hops.component(
    "/prediction",
    name="prediction",
    inputs=[
        hs.HopsNumber("year_to_predict","Z1","Float", hs.HopsParamAccess.LIST),
    ],
    outputs=[
        hs.HopsNumber("metric","Z2","Float", hs.HopsParamAccess.LIST),
        #hs.HopsNumber("remapped","r","Float" , hs.HopsParamAccess.LIST)
    ]
)

def MyMLPred(Z1):
        output = prediction(Z1)
        return output


if __name__ == "__main__":
    app.run(debug = True)
