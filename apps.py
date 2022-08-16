import pickle
import streamlit as st
from streamlit_option_menu import option_menu

Diabetes_model = pickle.load(open('Dia.pkl', 'rb'))
Heart_model = pickle.load(open('hert.pkl', 'rb'))
Prakinson_model = pickle.load(open('prok.pkl', 'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction Webapp',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Prediction'],
                           icons=['activity','heart','cpu-fill'],
                           default_index=0)
if(selected == 'Diabetes Prediction'):

    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        Blood_Pressure = st.text_input('Blood Pressure Value')

    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')

    with col2:
        insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI Value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')

    with col2:
        Age = st.text_input('Age')


    diagnosis_Diabetes = ""

    if st.button('Diabetes Test Result'):
        diab_prediction = Diabetes_model.predict([[Pregnancies,Glucose,Blood_Pressure,
                                                   SkinThickness,insulin,BMI,DiabetesPedigreeFunction
                                                      ,Age]])

        if diab_prediction[0]==1:
            diagnosis_Diabetes='The Person is Diabetic and need good healthcare'
            st.error(diagnosis_Diabetes)
        else:
            diagnosis_Diabetes='The person is not Diabetic :)'
            st.success(diagnosis_Diabetes)



if(selected == 'Heart Disease Prediction'):

    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')

    with col2:
        Sex = st.text_input('Sex')

    with col3:
        genre = st.selectbox(
            "Chest Pain",
            ('typical', 'nontypical', 'non angial', 'asymptomatic'))

        if genre == 'typical':
            cp = 1
        elif genre == 'nontypical':
            cp = 2
        elif genre == 'non angial':
            cp = 3
        elif genre == 'asymptomatic':
            cp = 4


    with col1:
        trestbps=st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serium Cholestrol in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood sugar >120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart rate Achieved')

    with col3:
        exang = st.text_input('Exercise incluced Angina')

    with col1:
        oldpeak = st.text_input('ST Deepression induced by excercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by floursopy')

    with col1:
        genre = st.selectbox(
            "Thal",
            ('normal', 'reversable defect', 'fixed defect'))
        if genre == 'normal':
                thal = 1
        elif genre == 'reversable defect':
                thal = 2
        elif genre == 'fixed defect':
                thal = 3


    heart_diagnosis=''
    if st.button('Heart Disease test result'):
        heart_prediction = Heart_model.predict([[Age,Sex,cp,trestbps,chol
                                                    ,fbs,restecg,thalach,exang,oldpeak,
                                                 slope,ca,thal]])
        if heart_prediction[0]==1:
            heart_diagnosis='This Person is having Heart Disease and need good healthcare '
            st.error(heart_diagnosis)
        else:
            heart_diagnosis='Good News! You does not have any heart Disease:)'
            st.success(heart_diagnosis)



if selected=='Parkinson Prediction':

    st.title('Parkinson Disease Prediction using ML')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo= st.text_input('MDVP.fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP.fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP.flo(Hz)')

    with col4:
        jitter_percent = st.text_input('MDVP.jitter(%)')

    with col5:
        jitter_abs = st.text_input('MDVP.jitter(Abs)')

    with col1:
        RAP= st.text_input('MDVP.RAP')

    with col2:
        PPQ = st.text_input('MDVP.PPQ')

    with col3:
        DDP = st.text_input('Jittter.DDP')

    with col4:
        shimmer = st.text_input('MDVP.Shimmer')

    with col5:
        shimmer_db = st.text_input('MDVP.Shimmer(db)')

    with col1:
        APQ3= st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP.APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR= st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spreas2')


    with col1:
        D2= st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    parikson_diagnosis =' '
    if st.button('Parkinsons Test Result'):
        parikson_prediction = Prakinson_model.predict([[fo,fhi,flo,jitter_percent
                                                           ,jitter_abs,RAP,PPQ,DDP,shimmer
                                                           ,shimmer_db,APQ3,APQ5,APQ,DDA,NHR
                                                           ,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])

        if parikson_prediction[0]==1:
            parikson_diagnosis='The Person has Parkinsons Disease and you need a good healthcare'
            st.error(parikson_diagnosis)
        else:
            parikson_diagnosis='Good News! you does not have any Parkinsons Disease Stay Healthy :)'
            st.success(parikson_diagnosis)


