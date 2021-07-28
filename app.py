from flask import Flask
import ghhops_server as hs
import numpy as np
import string
import tensorflow as tf
import tensorflow.keras

import pickle
from pickle import dump


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

def prediction(Z1):

        filename1 = 'Model_BED.h5'

        model1 = pickle.load(open(filename1, 'rb'))
    
        A = np.array(Z1)
        reshaped= A.reshape(-1,1)
        prediction1 = model1.predict(reshaped)
        list1 = prediction1.tolist()

        filename2 = 'Model_GREEN.h5'
        model2 = pickle.load(open(filename2, 'rb'))
        prediction2 = model2.predict(reshaped)
        list2 = prediction2.tolist()

        filename3 = 'Model_INV.h5'
        model3 = pickle.load(open(filename3, 'rb'))
        prediction3 = model3.predict(reshaped)
        list3 = prediction3.tolist()

        filename4 = 'Model_NEW.h5'
        model4 = pickle.load(open(filename4, 'rb'))
        prediction4 = model4.predict(reshaped)
        list4 = prediction4.tolist()

        filename5 = 'Model_POP.h5'
        model5 = pickle.load(open(filename5, 'rb'))
        prediction5 = model5.predict(reshaped)
        list5 = prediction5.tolist()

        filename6 = 'Model_POV.h5'
        model6 = pickle.load(open(filename6, 'rb'))
        prediction6 = model6.predict(reshaped)
        list6 = prediction6.tolist()

        filename7 = 'Model_PRICE.h5'
        model7 = pickle.load(open(filename7, 'rb'))
        prediction7 = model7.predict(reshaped)
        list7 = prediction7.tolist()

        filename8 = 'Model_ROAD.h5'
        model8 = pickle.load(open(filename8, 'rb'))
        prediction8 = model8.predict(reshaped)
        list8 = prediction8.tolist()

        filename9 = 'Model_SCH.h5'
        model9 = pickle.load(open(filename9, 'rb'))
        prediction9 = model9.predict(reshaped)
        list9 = prediction9.tolist()

        filename10 = 'Model_SOL.h5'
        model10 = pickle.load(open(filename10, 'rb'))
        prediction10 = model10.predict(reshaped)
        list10 = prediction10.tolist()

        filename11 = 'Model_TRANSP.h5'
        model11 = pickle.load(open(filename11, 'rb'))
        prediction11 = model11.predict(reshaped)
        list11 = prediction11.tolist()

        #--------------------------------------------------------------

        filename1a = 'Model_AJUDA.h5'
        model1a = pickle.load(open(filename1a, 'rb'))
        prediction1a = model1a.predict(reshaped)
        list1a = prediction1a.tolist()

        filename2a = 'Model_ALCANTARA_015.h5'
        model2a = pickle.load(open(filename2a, 'rb'))
        prediction2a = model2.predict(reshaped)
        list2a = prediction2a.tolist()

        filename3a = 'Model_BENFICA.h5'
        model3a = pickle.load(open(filename3a, 'rb'))
        prediction3a = model3a.predict(reshaped)
        list3a = prediction3a.tolist()

        filename4a = 'Model_SD_BENFICA_051.h5'
        model4a = pickle.load(open(filename4a, 'rb'))
        prediction4a = model4a.predict(reshaped)
        list4a = prediction4a.tolist()

        filename5a = 'Model_ALVALADE_080.h5'
        model5a = pickle.load(open(filename5a, 'rb'))
        prediction5a = model5a.predict(reshaped)
        list5a = prediction5a.tolist()

        filename6a = 'Model_MARVILA_005.h5'
        model6a = pickle.load(open(filename6a, 'rb'))
        prediction6a = model6a.predict(reshaped)
        list6a = prediction6a.tolist()

        filename7a = 'Model_AREEIRO_022.h5'
        model7a = pickle.load(open(filename7a, 'rb'))
        prediction7a = model7a.predict(reshaped)
        list7a = prediction7a.tolist()

        filename8a = 'Model_S_ANTONIO_048.h5'
        model8a = pickle.load(open(filename8a, 'rb'))
        prediction8a = model8a.predict(reshaped)
        list8a = prediction8a.tolist()

        filename9a = 'Model_S_M_MAIOR_030.h5'
        model9a = pickle.load(open(filename9a, 'rb'))
        prediction9a = model9a.predict(reshaped)
        list9a = prediction9a.tolist()

        filename10a = 'Model_ESTRELA_024.h5'
        model10a = pickle.load(open(filename10a, 'rb'))
        prediction10a = model10a.predict(reshaped)
        list10a = prediction10a.tolist()

        filename11a = 'Model_C_OURIQUE_012.h5'
        model11a = pickle.load(open(filename11a, 'rb'))
        prediction11a = model11a.predict(reshaped)
        list11a = prediction11a.tolist()

        filename12a = 'Model_MISERICORDIA_010.h5'
        model12a = pickle.load(open(filename12a, 'rb'))
        prediction12a = model12a.predict(reshaped)
        list12a = prediction12a.tolist()

        filename13a = 'Model_ARROIOS_005.h5'
        model13a = pickle.load(open(filename13a, 'rb'))
        prediction13a = model13a.predict(reshaped)
        list13a = prediction13a.tolist()

        filename14a = 'Model_BEATO_0029.h5'
        model14a = pickle.load(open(filename14a, 'rb'))
        prediction14a = model14a.predict(reshaped)
        list14a = prediction14a.tolist()

        filename15a = 'Model_S_VICENTE_012.h5'
        model15a = pickle.load(open(filename15a, 'rb'))
        prediction15a = model15a.predict(reshaped)
        list15a = prediction15a.tolist()

        filename16a = 'Model_AV_NOVAS_004.h5'
        model16a = pickle.load(open(filename16a, 'rb'))
        prediction16a = model16a.predict(reshaped)
        list16a = prediction16a.tolist()

        filename17a = 'Model_LUMIAR_0002.h5'
        model17a = pickle.load(open(filename17a, 'rb'))
        prediction17a = model17a.predict(reshaped)
        list17a = prediction17a.tolist()

        filename18a = 'Model_CARNIDE_032.h5'
        model18a = pickle.load(open(filename18a, 'rb'))
        prediction18a = model18a.predict(reshaped)
        list18a = prediction18a.tolist()

        filename19a = 'Model_ST_CLARA_001.h5'
        model19a = pickle.load(open(filename19a, 'rb'))
        prediction19a = model19a.predict(reshaped)
        list19a = prediction19a.tolist()

        filename20a = 'Model_OLIVAIS_024.h5'
        model20a = pickle.load(open(filename20a, 'rb'))
        prediction20a = model20a.predict(reshaped)
        list20a = prediction20a.tolist()

        filename21a = 'Model_P_FRANCA_007.h5'
        model21a = pickle.load(open(filename21a, 'rb'))
        prediction21a = model21a.predict(reshaped)
        list21a = prediction21a.tolist()

        filename22a = 'Model_CAMPOLIDE_001.h5'
        model22a = pickle.load(open(filename22a, 'rb'))
        prediction22a= model22a.predict(reshaped)
        list22a = prediction22a.tolist()


        lista=list1a+list2a+list3a+list4a+list5a+list6a+list7a+list8a+list9a+list10a+list11a+list12a+list13a+list14a+list15a+list16a+list17a+list18a+list19a+list20a+list21a+list22a


        list_f=list1+list2+list3+list4+list5+list6+list7+list8+list9+list10+list11

        list = list_f+lista

        output = []

        # ## iterating over the data
        for item in list:
        # # # appending elements to the flat_list
            output += item
        
        return output



if __name__ == "__main__":
    app.run(debug = True)
