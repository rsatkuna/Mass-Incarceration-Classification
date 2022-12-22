'''
Total Trained Cases: 800000 cases
Data columns (total 28 columns): Use "VARIABLE: <variable name>" in Find feature to move to how that variable is used in the app
NOTE: Many variables wer preset to mode values, bu thave commented out code for their use in the application 
'''

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import pickle

from sklearn.linear_model import LogisticRegression
from skopt import BayesSearchCV

# Create header
st.title("Sentencing Outcomes in the US Federal Justice System")

st.header("Exploratory Data Analysis")
data = pd.read_csv('./data/eda_booker_report.csv', index_col='Unnamed: 0')
st.subheader("Sample of Sentencing Data")
st.write(data.head())

st.subheader("Input Variables")

# Index: 25
USSCIDN = -999

# VARIABLE: OFFTYPE2
input_OFFTYPE2 = st.selectbox("**Defendant's  Primary Offense**", ("Murder", "Manslaughter", "Kidnapping/Hostage Taking", "Sexual Abuse", "Assault", "Robbery", "Arson",
"Drugs - Trafficking, Manufacturing, and Importing", "Drugs - Communication Facilities", "Drugs: - Simple Possession", 
"Firearms", "Burglary/Breaking and Entering", "Auto Theft", "Larceny", "Fraud", "Embezzlement", "Forgery/Counterfeiting",
"Bribery", "Tax Offenses", "Money Laundering", "Racketeering /Extortion", "Gambling/Lottery", "Civil Rights Offenses", 
"Immigration", "Pornography/Prostitution", "Prison Offenses", "Administration of Justice", "Environmental, Game, Fish, and Wildlife Offenses", 
"National Defense Offenses", "Antitrust Violations", "Food and Drug Offenses", "Traffic Violations and Other Offenses", 
"Child Pornography", "Obscenity", "Prostitution"))

if input_OFFTYPE2 == "Drugs - Trafficking, Manufacturing, and Importing": OFFTYPE2 = 10
elif input_OFFTYPE2 == "Murder": OFFTYPE2 = 1
elif input_OFFTYPE2 == "Manslaughter": OFFTYPE2 = 2
elif input_OFFTYPE2 == "Kidnapping/Hostage Taking": OFFTYPE2 = 3
elif input_OFFTYPE2 == "Sexual Abuse": OFFTYPE2 = 4
elif input_OFFTYPE2 == "Assault": OFFTYPE2 = 5
elif input_OFFTYPE2 == "Robbery": OFFTYPE2 = 6
elif input_OFFTYPE2 == "Arson": OFFTYPE2 = 9
elif input_OFFTYPE2 == "Drugs - Trafficking, Manufacturing, and Importing": OFFTYPE2 = 10
elif input_OFFTYPE2 == "Drugs - Communication Facilities": OFFTYPE2 = 11
elif input_OFFTYPE2 == "Drugs: - Simple Possession": OFFTYPE2 = 12
elif input_OFFTYPE2 == "Firearms": OFFTYPE2 = 13
elif input_OFFTYPE2 == "Burglary/Breaking and Entering": OFFTYPE2 = 15
elif input_OFFTYPE2 == "Auto Theft": OFFTYPE2 = 16
elif input_OFFTYPE2 == "Larceny": OFFTYPE2 = 17
elif input_OFFTYPE2 == "Fraud": OFFTYPE2 = 18
elif input_OFFTYPE2 == "Embezzlement": OFFTYPE2 = 19
elif input_OFFTYPE2 == "Forgery/Counterfeiting": OFFTYPE2 = 20
elif input_OFFTYPE2 == "Bribery": OFFTYPE2 = 21
elif input_OFFTYPE2 == "Tax Offenses": OFFTYPE2 = 22
elif input_OFFTYPE2 == "Money Laundering": OFFTYPE2 = 23
elif input_OFFTYPE2 == "Racketeering /Extortion": OFFTYPE2 = 24
elif input_OFFTYPE2 == "Gambling/Lottery": OFFTYPE2 = 25
elif input_OFFTYPE2 == "Civil Rights Offenses": OFFTYPE2 = 26
elif input_OFFTYPE2 == "Immigration": OFFTYPE2 = 27
elif input_OFFTYPE2 == "Pornography/Prostitution": OFFTYPE2 = 28
elif input_OFFTYPE2 == "Prison Offenses": OFFTYPE2 = 29
elif input_OFFTYPE2 == "Administration of Justice": OFFTYPE2 = 30
elif input_OFFTYPE2 == "Environmental, Game, Fish, and Wildlife Offenses": OFFTYPE2 = 31
elif input_OFFTYPE2 == "National Defense Offenses": OFFTYPE2 = 32
elif input_OFFTYPE2 == "Antitrust Violations": OFFTYPE2 = 33
elif input_OFFTYPE2 == "Food and Drug Offenses": OFFTYPE2 = 34
elif input_OFFTYPE2 == "Traffic Violations and Other Offenses": OFFTYPE2 = 35
elif input_OFFTYPE2 == "Child Pornography)": OFFTYPE2 = 42
elif input_OFFTYPE2 == "Obscenity": OFFTYPE2 = 43
elif input_OFFTYPE2 == "Prostitution": OFFTYPE2 = 44
else: OFFTYPE2 = 0
st.write("OFFTYPE2 set to ", OFFTYPE2)
st.write("")
st.write("")

# Index: 0
ACCAP = 0
# input_ACCAP = st.selectbox("**Armed Career Status**", ("Not applied", "Applied", "Inapplicable"))
# if input_ACCAP == "Applied": ACCAP = 1 
# else: ACCAP = 0
# st.write("ACCAP set to ", ACCAP)
# st.write("")
# st.write("")

# Index: 1
input_AGE = st.slider("**Defendant's Age** ( >= 16 years )", 16, 98)
AGE = input_AGE
st.write("AGE set to ", AGE)
st.write("")
st.write("")


# VARIABLE: GGDUM
GGDUM = 0
# https://content.next.westlaw.com/Document/NE79C68F0B8AD11D8983DF34406B5929B/View/FullText.html?transitionType=Default&contextData=(sc.Default)&firstPage=true
# input_GGDUM = st.selectbox("**Defendant's Aggravating Role**", ("No Adjustment Applied", "Valid Value (1-4) Applied", "Indeterminable, invalid value applied, or Inapplicable"))
# if input_GGDUM == "No Adjustment Applied": GGDUM = 0
# elif input_GGDUM == "Valid Value (1-4) Applied": GGDUM = 1
# els: GGDUM = 99
# st.write("GGDUM set to ", GGDUM)
# st.write("")
# st.write("")

# VARIABLE: BOOKER2
BOOKER2 = 0
# input_BOOKER2 = st.selectbox("**Sentence Length Relative to Guidleline Range**", ("Within Range", "Above Departure", "Government Sponsored", "Below Range"))
# # https://en.wikipedia.org/wiki/United_States_Federal_Sentencing_Guidelines
# if input_BOOKER2 == "Within Range": BOOKER2 = 0
# elif input_BOOKER2 == "Above Departure": BOOKER2 = 1
# elif input_BOOKER2 == "Government Sponsored": BOOKER2 = 2
# elif input_BOOKER2 == "Below Range": BOOKER2 = 4
# else: BOOKER2 = 0 
# st.write("BOOKER2 set to", BOOKER2)
# st.write("")
# st.write("")

# VARIABLE: AROFFAP
AROFFAP = 0
# input_AROFFAP = st.selectbox("**Career Offender Status**", ("Not Applied", "Applied"))
# if input_AROFFAP == "Applied": AROFFAP = 1 
# elif input_AROFFAP == "Not Applied": AROFFAP = 0
# else: AROFFAP = 0
# st.write("AROFFAP set to ", AROFFAP)
# st.write("")
# st.write("")

# VARIABLE: CIRCDIST 
CIRCDIST = 1

# VARIABLE: MITDUM
MITDUM = 5
# input_MITDUM = st.selectbox("**Mitigating Role Adjustment**", ("Inapplicable", "No Adjustment Applied", "Valid Value (1-4) Applied"))
# if input_MITDUM == "No Adjustment Applied": MITDUM = 1 
# elif input_MITDUM == "Valid Value (1-4) Applied": MITDUM = 0
# else: MITDUM = 0
# st.write("MITDUM set to ", MITDUM)
# st.write("")
# st.write("")

# VARIABLE: MONCIRC
MONCIRC = 5
# input_MONCIRC = st.number_input("**Judicial Circuit**", 0, 11)
# MONCIRC = input_MONCIRC
# st.write("MONCIRC set to ", MONCIRC)
# st.write("")
# st.write("")

# VARIABLE: ONSEX
input_ONSEX = st.radio("**Offender's Sex**", ("Unspecified", "Male", "Female"))
if input_ONSEX == "Male": ONSEX = 1 
elif input_ONSEX == "Female": ONSEX = 0
else: ONSEX = 0
st.write("ONSEX set to ", ONSEX) 
st.write("")
st.write("")

# VARIABLE: NEWCNVTN
input_NEWCNVTN = st.radio("**Case Type**", ["Plea", "Trial"])
if input_NEWCNVTN == "Plea": NEWCNVTN = 1 
else: NEWCNVTN = 0
st.write("NEWCNVTN set to ", NEWCNVTN)
st.write("")
st.write("")

# VARIABLE: NEWCIT
input_NEWCIT = st.radio("**Defendant's Citizenship Status**", ["U.S.", "Non-U.S."])
if input_NEWCIT == "U.S.": NEWCIT = 1 
elif input_NEWCIT == "Non-U.S.": NEWCIT = 0
else: NEWCIT = 1
st.write("NEWCIT set to ", NEWCIT)
st.write("The US Sentencing Commission does not differentiate between Legal and Illegal Immigrants for their data collection nor analysis of sentencing data.")
st.write("")
st.write("")

# VARIABLE: EWEDUC
input_EWEDUC = st.selectbox("**Defendant's Education Level**", ("H.S. Graduate", "Less Than H.S. Graduate", "Some College", "College Graduate"))
if input_EWEDUC == "Less Than H.S. Graduate": EWEDUC = 1
elif input_EWEDUC == "H.S. Graduate": EWEDUC = 3
elif input_EWEDUC == "Some College": EWEDUC = 5
elif input_EWEDUC == "College Graduate": EWEDUC = 6
else: NEWCNVTN = 3
st.write("EWEDUC set to ", EWEDUC)
st.write("")
st.write("")

# VARIABLE: NEWRACE
input_NEWRACE = st.selectbox("**Defendant's Race**", ("Other", "White", "Black", "Hispanic"))
if input_NEWRACE == "White": NEWRACE = 1
elif input_NEWRACE == "Black": NEWRACE = 2
elif input_NEWRACE == "Hispanic": NEWRACE = 3
else: NEWRACE = 6
st.write("NEWRACE set to ", NEWRACE)
st.write("")
st.write("")

# VARIABLE: PRIMARY
input_PRIMARY = st.selectbox("**Primary drug type involved in the Defendant's  case**", ("None", "Cocaine", "Crack", "Heroin", "Marijuana", "Methamphetamine", "Other"))
if input_PRIMARY == "Cocaine": PRIMARY = 1 
elif input_PRIMARY == "Crack": PRIMARY = 2
elif input_PRIMARY == "Heroin": PRIMARY = 3
elif input_PRIMARY == "Marijuana": PRIMARY = 4
elif input_PRIMARY == "Methamphetamine": PRIMARY = 6
elif input_PRIMARY == "Other": PRIMARY = 77
else: PRIMARY = 78
st.write("PRIMARY set to ", PRIMARY)
st.write("")
st.write("")

# VARIABLE: A
A = 0
# input_A = st.radio("**Government Sponsored Categories**", ("Within Range", "Safety Valve Not Applied", "Safety Valve Applied", "Missing, Indeterminable, or Inapplicable"))
# if input_A == "Within Range": A = 0
# elif input_A == "Safety Valve Not Applied": A = 1
# elif input_A == "Safety Valve Applied": A = 2
# elif input_A == "Missing, Indeterminable, or Inapplicable": A = 3
# st.write("A set to ", A)
# st.write("")
# st.write("")

# VARIABLE: SAFEVALVE
SAFEVALVE = 0
# input_SAFEVALVE = st.radio("**Safety Valve' provision for drug offense by individuals with low criminal history**", ["Inapplicable", "Not Applied", "Applied"])
# if input_SAFEVALVE == "Not Applied": SAFEVALVE = 0
# elif input_SAFEVALVE == "Applied": SAFEVALVE = 1
# else: SAFEVALVE = 2
# st.write("SAFEVALVE set to ", SAFEVALVE)
# st.write("")
# st.write("")

# VARIABLE: OTCHPTS
OTCHPTS = 0
# input_OTCHPTS = st.number_input("**type of sentence**", 0, 99)
# OTCHPTS = input_OTCHPTS
# st.write("OTCHPTS set to ", OTCHPTS)
# st.write("")
# st.write("")

# VARIABLE: WEAPON
WEAPON = 0
# input_WEAPON = st.radio("**SOC weapon enhancement**", ("No SOC Weapon Enhancement Nor 18§924(c) Charge Present", "SOC Weapon Enhancement or 18§924(c) Charge Present"))
# if input_WEAPON == "No SOC Weapon Enhancement Nor 18§924(c) Charge Present": WEAPON = 0
# elif input_WEAPON == "SOC Weapon Enhancement or 18§924(c) Charge Present": WEAPON = 1
# else: WEAPON = 0
# st.write("WEAPON set to ", WEAPON)
# st.write("")
# st.write("")

# VARIABLE: XCRHISSR
XCRHISSR = 1 
# input_XCRHISSR = st.number_input("**Defendant's final criminal history category (I-VI)**", 1, 6)
# XCRHISSR = input_XCRHISSR 
# st.write("XCRHISSR set to ", XCRHISSR)
# st.write("")
# st.write("")

# VARIABLE: ENSPLT0
ENSPLT0 = 0
# input_ENSPLT0 = st.number_input("**The trumped total prison sentence, in months (sentence of 470 months or more, including life, are reported as 470 months), plus alternatives, with zeros (probation)**", 0, 470)
# ENSPLT0 = input_ENSPLT0
# st.write("ENSPLT0 set to ", ENSPLT0)
# st.write("")
# st.write("")


# VARIABLE: GDL
GDL = 2
# input_GDL = st.number_input("**Chapter 2 Guideline Applied**", 0, 162)
# GDL = input_GDL
# st.write("GDL set to ", GDL)
# st.write("")
# st.write("")


# TEST USER INPUT AS AN EXAMPLE
st.title("Test Production Model with Inputs")

# MODEL 1
st.subheader("Time Period by Court Decision: Random Forest Classifier")

# Performance Metrics
st.write("**Accuracy Score during Training**")
st.write("Train Score: 0.9929")
st.write("Test Score: 0.9899")

# VARIABLE: FY
input_FY1 = st.number_input("**Fiscal Year for SENTIMP Model**", 1996, 2011)
FY = input_FY1 
st.write("FY set to ", FY)

# VARIABLE: QUARTER
input_QUARTER = st.number_input("**Fiscal Year quarter**", 1, 4)
QUARTER = input_QUARTER
st.write("QUARTER set to ", QUARTER)
st.write("")
st.write("")

# VARIABLE: LMIN
input_LMIN = st.number_input("**Guideline Minimum for ERIOD Model**", 0, 470)
LMIN = input_LMIN
st.write("LMIN set to ", LMIN)
st.write("This field takes statutory maximum and minimum trumps into account. Guideline minimums greater than 470 (including life) are trumped at 470 months.")
st.write("")
st.write("")

# correlated feature
input_CIRCDIST = st.selectbox("**Select Location of District Circuit Court for ERIOD Model**", ("Dist of Columbia", "Maine", "Massachusetts", "New Hampshire", "Puerto Rico", "Rhode Island", 
"Connecticut", "New York East", "New York North", "New York South", "New York West", "Vermont",
"Delaware", "New Jersey", "Penn. East", "Penn. Mid", "Penn. West", "Virgin Islands",
"Maryland", "N Carolina East", "N Carolina Mid", "N Carolina West", "South Carolina", "Virginia East",
"Virginia West", "W Virginia North", "W Virginia South", "Louisiana East", "Louisiana Middle",
"Louisiana West", "Miss. North", "Miss. South", "Texas East", "Texas North",
"Texas South", "Texas West", "Kentucky East", "Kentucky West", "Michigan East",
"Michigan West", "Ohio North", "Ohio South", "Tennessee East", "Iowa South",
"Minnesota", "Missouri East", "Missouri West", "Nebraska", "North Dakota",
"South Dakota", "Alaska", "Arizona ", "California Cent", "California East",
"California North", "California South", "Guam", "Hawaii", "Idaho",
"Montana", "Nevada", "N Mariana", "Oregon", "Washington East",
"Washington West", "Colorado", "Kansas", "New Mexico", "Oklahoma East",
"Oklahoma North", "Oklahoma West", "Utah", "Wyoming", "Alabama Mid",
"Alabama North", "Alabama South", "Florida Mid", "Florida North", "Florida South", "Georgia Mid", "Georgia North", "Georgia South"))
if input_CIRCDIST == "Dist of Columbia": CIRCDIST = 1
elif input_CIRCDIST == "Maine": CIRCDIST = 2
elif input_CIRCDIST == "Massachusetts": CIRCDIST = 3
elif input_CIRCDIST == "New Hampshire": CIRCDIST = 4
elif input_CIRCDIST == "Puerto Rico": CIRCDIST = 5
elif input_CIRCDIST == "Rhode Island": CIRCDIST = 6
elif input_CIRCDIST == "Connecticut": CIRCDIST = 7
elif input_CIRCDIST == "New York East": CIRCDIST = 8
elif input_CIRCDIST == "New York North": CIRCDIST = 9
elif input_CIRCDIST == "New York South": CIRCDIST = 10
elif input_CIRCDIST == "New York West": CIRCDIST = 11
elif input_CIRCDIST == "Vermont": CIRCDIST = 12
elif input_CIRCDIST == "Delaware": CIRCDIST = 13
elif input_CIRCDIST == "New Jersey": CIRCDIST = 14
elif input_CIRCDIST == "Penn. East": CIRCDIST = 15
elif input_CIRCDIST == "Penn. Mid": CIRCDIST = 16
elif input_CIRCDIST == "Penn. West": CIRCDIST = 17
elif input_CIRCDIST == "Virgin Islands": CIRCDIST = 18
elif input_CIRCDIST == "Maryland": CIRCDIST = 19
elif input_CIRCDIST == "N Carolina East": CIRCDIST = 20
elif input_CIRCDIST == "N Carolina Mid": CIRCDIST = 21
elif input_CIRCDIST == "N Carolina West": CIRCDIST = 22
elif input_CIRCDIST == "South Carolina": CIRCDIST = 23
elif input_CIRCDIST == "Virginia East": CIRCDIST = 24
elif input_CIRCDIST == "Virginia West": CIRCDIST = 25
elif input_CIRCDIST == "W Virginia North": CIRCDIST = 26
elif input_CIRCDIST == "W Virginia South": CIRCDIST = 27
elif input_CIRCDIST == "Louisiana East": CIRCDIST = 28
elif input_CIRCDIST == "Louisiana Middle": CIRCDIST = 29
elif input_CIRCDIST == "Louisiana West": CIRCDIST = 30
elif input_CIRCDIST == "Miss. North": CIRCDIST = 31
elif input_CIRCDIST == "Miss. South": CIRCDIST = 32
elif input_CIRCDIST == "Texas East": CIRCDIST = 33
elif input_CIRCDIST == "Texas North": CIRCDIST = 34
elif input_CIRCDIST == "Texas South": CIRCDIST = 35
elif input_CIRCDIST == "Texas West": CIRCDIST = 36
elif input_CIRCDIST == "Kentucky East": CIRCDIST = 37
elif input_CIRCDIST == "Kentucky West": CIRCDIST = 38
elif input_CIRCDIST == "Michigan East": CIRCDIST = 39
elif input_CIRCDIST == "Michigan West": CIRCDIST = 40
elif input_CIRCDIST == "Ohio North": CIRCDIST = 41
elif input_CIRCDIST == "Ohio South": CIRCDIST = 42
elif input_CIRCDIST == "Tennessee East": CIRCDIST = 43
elif input_CIRCDIST == "Tennessee Mid": CIRCDIST = 44
elif input_CIRCDIST == "Tennessee West": CIRCDIST = 45
elif input_CIRCDIST == "Illinois Cent": CIRCDIST = 46
elif input_CIRCDIST == "Illinois North": CIRCDIST = 47
elif input_CIRCDIST == "Illinois South": CIRCDIST = 48
elif input_CIRCDIST == "Indiana North": CIRCDIST = 49
elif input_CIRCDIST == "Indiana South": CIRCDIST = 50
elif input_CIRCDIST == "Wisconsin East": CIRCDIST = 51
elif input_CIRCDIST == "Wisconsin West": CIRCDIST = 52
elif input_CIRCDIST == "Arkansas East": CIRCDIST = 53
elif input_CIRCDIST == "Arkansas West": CIRCDIST = 54
elif input_CIRCDIST == "Iowa North": CIRCDIST = 55
elif input_CIRCDIST == "Iowa South": CIRCDIST = 56
elif input_CIRCDIST == "Minnesota": CIRCDIST = 57
elif input_CIRCDIST == "Missouri East": CIRCDIST = 58
elif input_CIRCDIST == "Missouri West": CIRCDIST = 59
elif input_CIRCDIST == "Nebraska": CIRCDIST = 60
elif input_CIRCDIST == "North Dakota": CIRCDIST = 61
elif input_CIRCDIST == "South Dakota": CIRCDIST = 62
elif input_CIRCDIST == "Alaska": CIRCDIST = 63
elif input_CIRCDIST == "Arizona": CIRCDIST = 64
elif input_CIRCDIST == "California Cent": CIRCDIST = 65
elif input_CIRCDIST == "California East": CIRCDIST = 66
elif input_CIRCDIST == "California North": CIRCDIST = 67
elif input_CIRCDIST == "California South": CIRCDIST = 68
elif input_CIRCDIST == "Guam": CIRCDIST = 69
elif input_CIRCDIST == "Hawaii": CIRCDIST = 70
elif input_CIRCDIST == "Idaho": CIRCDIST = 71
elif input_CIRCDIST == "Montana": CIRCDIST = 72
elif input_CIRCDIST == "Nevada": CIRCDIST = 73
elif input_CIRCDIST == "N Mariana Island": CIRCDIST = 74
elif input_CIRCDIST == "Oregon": CIRCDIST = 75
elif input_CIRCDIST == "Washington East": CIRCDIST = 76
elif input_CIRCDIST == "Washington West": CIRCDIST = 77
elif input_CIRCDIST == "Colorado": CIRCDIST = 78
elif input_CIRCDIST == "Kansas": CIRCDIST = 79
elif input_CIRCDIST == "New Mexico": CIRCDIST = 80
elif input_CIRCDIST ==  "Oklahoma East": CIRCDIST = 81
elif input_CIRCDIST ==  "Oklahoma North": CIRCDIST = 82
elif input_CIRCDIST ==  "Oklahoma West": CIRCDIST = 83
elif input_CIRCDIST ==  "Utah": CIRCDIST =  84
elif input_CIRCDIST ==  "Wyoming": CIRCDIST=  85 
elif input_CIRCDIST ==  "Alabama Mid": CIRCDIST = 86
elif input_CIRCDIST ==  "Alabama North": CIRCDIST = 87
elif input_CIRCDIST ==  "Alabama South": CIRCDIST = 88
elif input_CIRCDIST ==  "Florida Mid": CIRCDIST = 89
elif input_CIRCDIST ==  "Florida North": CIRCDIST = 90
elif input_CIRCDIST ==  "Florida South": CIRCDIST = 91
elif input_CIRCDIST ==  "Georgia Mid": CIRCDIST = 92
elif input_CIRCDIST ==  "Georgia North": CIRCDIST = 93
elif input_CIRCDIST == "Georgia South": CIRCDIST = 94
st.write("CIRCDIST set to ", CIRCDIST)
st.write("")
st.write("")

# VARIABLE: SENTIMP
input_SENTIMP = st.radio("**Set Sentence Type for ERIOD Model**", ["No Prison/Probation (Fine Only)", "Prison Only (No Alternatives)", "Prison + Confinement Conditions (Alternatives, Including Zone C Split Sentences)", "Probation + Confinement Conditions (Alternatives)", "Probation Only"])
if input_SENTIMP == "No Prison/Probation (Fine Only)": SENTIMP = 0
elif input_SENTIMP == "Prison Only (No Alternatives)": SENTIMP = 1
elif input_SENTIMP == "Prison + Confinement Conditions (Alternatives, Including Zone C Split Sentences)": SENTIMP = 2
elif input_SENTIMP == "Probation + Confinement Conditions (Alternatives)": SENTIMP = 3
elif input_SENTIMP == "Probation Only": SENTIMP = 4
else: SENTIMP = 0
st.write("SENTIMP set to ", SENTIMP)
st.write("")
st.write("")

# Input Features for Model 1
ERIOD_features = [ACCAP, AGE, GGDUM, BOOKER2, AROFFAP, 
            CIRCDIST, MITDUM, MONCIRC, ONSEX, NEWCIT, 
            NEWCNVTN, EWEDUC, NEWRACE, OFFTYPE2, 
            PRIMARY, QUARTER, A, SAFEVALVE, SENTIMP,
            OTCHPTS, WEAPON, XCRHISSR, LMIN, FY, 
            USSCIDN, ENSPLT0, GDL]

ERIOD_input = np.array(ERIOD_features).reshape(1, -1) 

# # Import Model 1
with open('./trained-models/eriod/eriod_rf', 'rb') as pickle_in:
    rf_ERIOD = pickle.load(pickle_in)

predict_ERIOD = st.button("Test ERIOD Model")
if predict_ERIOD:
    # Predict ERIOD
    prediction_ERIOD = rf_ERIOD.predict(ERIOD_input)
    if prediction_ERIOD[0] == 1: st.info("The predicted time period Koon Period (June 13, 1996 through April 30, 2003)")
    elif prediction_ERIOD[0] == 2: st.info("The predicted time period is PROTECT Act Period (May 1, 2003 through June 24, 2004)")
    elif prediction_ERIOD[0] == 3: st.info("The predicted time period is Booker Period (January 12, 2005 through December 10, 2007)")
    elif prediction_ERIOD[0] == 4: st.info("The predicted time period is Gall Period (December 11, 2007 through September 30, 2011)")
else:
    st.write("")



# MODEL 2
st.subheader("Sentence Type: Random Forest Model")
st.write("**Accuracy Score during Training**")
st.write("Train Score: 0.9528")
st.write("Test Score: 0.9447")

# VARIABLE: ERIOD
input_ERIOD = st.radio("**Set Time Period for SENTIMP Model**", ["Koon Period (June 13, 1996 through April 30, 2003)", "PROTECT Act Period (May 1, 2003 through June 24, 2004)",  "Booker Period (January 12, 2005 through December 10, 2007)", "Gall Period (December 11, 2007 through September 30, 2011)"])
if input_ERIOD == "Koon Period (June 13, 1996 through April 30, 2003)": ERIOD = 1
elif input_ERIOD == "PROTECT Act Period (May 1, 2003 through June 24, 2004)": ERIOD = 2
elif input_ERIOD == "Booker Period (January 12, 2005 through December 10, 2007)": ERIOD = 3
elif input_ERIOD == "Gall Period (December 11, 2007 through September 30, 2011)": ERIOD = 4
st.write("ERIOD set to ", ERIOD)
st.write("")
st.write("")

# VARIABLE: FY
input_FY = st.number_input("**Set Fiscal Year for SENTIMP Model**", 1996, 2011)
FY = input_FY 
st.write("FY set to ", FY)

# correlated feature
input_CIRCDIST = st.selectbox("**Select Location of District Circuit Court for SENTIMP Model**", ("Dist of Columbia", "Maine", "Massachusetts", "New Hampshire", "Puerto Rico", "Rhode Island", 
"Connecticut", "New York East", "New York North", "New York South", "New York West", "Vermont",
"Delaware", "New Jersey", "Penn. East", "Penn. Mid", "Penn. West", "Virgin Islands",
"Maryland", "N Carolina East", "N Carolina Mid", "N Carolina West", "South Carolina", "Virginia East",
"Virginia West", "W Virginia North", "W Virginia South", "Louisiana East", "Louisiana Middle",
"Louisiana West", "Miss. North", "Miss. South", "Texas East", "Texas North",
"Texas South", "Texas West", "Kentucky East", "Kentucky West", "Michigan East",
"Michigan West", "Ohio North", "Ohio South", "Tennessee East", "Iowa South",
"Minnesota", "Missouri East", "Missouri West", "Nebraska", "North Dakota",
"South Dakota", "Alaska", "Arizona ", "California Cent", "California East",
"California North", "California South", "Guam", "Hawaii", "Idaho",
"Montana", "Nevada", "N Mariana", "Oregon", "Washington East",
"Washington West", "Colorado", "Kansas", "New Mexico", "Oklahoma East",
"Oklahoma North", "Oklahoma West", "Utah", "Wyoming", "Alabama Mid",
"Alabama North", "Alabama South", "Florida Mid", "Florida North", "Florida South", "Georgia Mid", "Georgia North", "Georgia South"))
if input_CIRCDIST == "Dist of Columbia": CIRCDIST = 1
elif input_CIRCDIST == "Maine": CIRCDIST = 2
elif input_CIRCDIST == "Massachusetts": CIRCDIST = 3
elif input_CIRCDIST == "New Hampshire": CIRCDIST = 4
elif input_CIRCDIST == "Puerto Rico": CIRCDIST = 5
elif input_CIRCDIST == "Rhode Island": CIRCDIST = 6
elif input_CIRCDIST == "Connecticut": CIRCDIST = 7
elif input_CIRCDIST == "New York East": CIRCDIST = 8
elif input_CIRCDIST == "New York North": CIRCDIST = 9
elif input_CIRCDIST == "New York South": CIRCDIST = 10
elif input_CIRCDIST == "New York West": CIRCDIST = 11
elif input_CIRCDIST == "Vermont": CIRCDIST = 12
elif input_CIRCDIST == "Delaware": CIRCDIST = 13
elif input_CIRCDIST == "New Jersey": CIRCDIST = 14
elif input_CIRCDIST == "Penn. East": CIRCDIST = 15
elif input_CIRCDIST == "Penn. Mid": CIRCDIST = 16
elif input_CIRCDIST == "Penn. West": CIRCDIST = 17
elif input_CIRCDIST == "Virgin Islands": CIRCDIST = 18
elif input_CIRCDIST == "Maryland": CIRCDIST = 19
elif input_CIRCDIST == "N Carolina East": CIRCDIST = 20
elif input_CIRCDIST == "N Carolina Mid": CIRCDIST = 21
elif input_CIRCDIST == "N Carolina West": CIRCDIST = 22
elif input_CIRCDIST == "South Carolina": CIRCDIST = 23
elif input_CIRCDIST == "Virginia East": CIRCDIST = 24
elif input_CIRCDIST == "Virginia West": CIRCDIST = 25
elif input_CIRCDIST == "W Virginia North": CIRCDIST = 26
elif input_CIRCDIST == "W Virginia South": CIRCDIST = 27
elif input_CIRCDIST == "Louisiana East": CIRCDIST = 28
elif input_CIRCDIST == "Louisiana Middle": CIRCDIST = 29
elif input_CIRCDIST == "Louisiana West": CIRCDIST = 30
elif input_CIRCDIST == "Miss. North": CIRCDIST = 31
elif input_CIRCDIST == "Miss. South": CIRCDIST = 32
elif input_CIRCDIST == "Texas East": CIRCDIST = 33
elif input_CIRCDIST == "Texas North": CIRCDIST = 34
elif input_CIRCDIST == "Texas South": CIRCDIST = 35
elif input_CIRCDIST == "Texas West": CIRCDIST = 36
elif input_CIRCDIST == "Kentucky East": CIRCDIST = 37
elif input_CIRCDIST == "Kentucky West": CIRCDIST = 38
elif input_CIRCDIST == "Michigan East": CIRCDIST = 39
elif input_CIRCDIST == "Michigan West": CIRCDIST = 40
elif input_CIRCDIST == "Ohio North": CIRCDIST = 41
elif input_CIRCDIST == "Ohio South": CIRCDIST = 42
elif input_CIRCDIST == "Tennessee East": CIRCDIST = 43
elif input_CIRCDIST == "Tennessee Mid": CIRCDIST = 44
elif input_CIRCDIST == "Tennessee West": CIRCDIST = 45
elif input_CIRCDIST == "Illinois Cent": CIRCDIST = 46
elif input_CIRCDIST == "Illinois North": CIRCDIST = 47
elif input_CIRCDIST == "Illinois South": CIRCDIST = 48
elif input_CIRCDIST == "Indiana North": CIRCDIST = 49
elif input_CIRCDIST == "Indiana South": CIRCDIST = 50
elif input_CIRCDIST == "Wisconsin East": CIRCDIST = 51
elif input_CIRCDIST == "Wisconsin West": CIRCDIST = 52
elif input_CIRCDIST == "Arkansas East": CIRCDIST = 53
elif input_CIRCDIST == "Arkansas West": CIRCDIST = 54
elif input_CIRCDIST == "Iowa North": CIRCDIST = 55
elif input_CIRCDIST == "Iowa South": CIRCDIST = 56
elif input_CIRCDIST == "Minnesota": CIRCDIST = 57
elif input_CIRCDIST == "Missouri East": CIRCDIST = 58
elif input_CIRCDIST == "Missouri West": CIRCDIST = 59
elif input_CIRCDIST == "Nebraska": CIRCDIST = 60
elif input_CIRCDIST == "North Dakota": CIRCDIST = 61
elif input_CIRCDIST == "South Dakota": CIRCDIST = 62
elif input_CIRCDIST == "Alaska": CIRCDIST = 63
elif input_CIRCDIST == "Arizona": CIRCDIST = 64
elif input_CIRCDIST == "California Cent": CIRCDIST = 65
elif input_CIRCDIST == "California East": CIRCDIST = 66
elif input_CIRCDIST == "California North": CIRCDIST = 67
elif input_CIRCDIST == "California South": CIRCDIST = 68
elif input_CIRCDIST == "Guam": CIRCDIST = 69
elif input_CIRCDIST == "Hawaii": CIRCDIST = 70
elif input_CIRCDIST == "Idaho": CIRCDIST = 71
elif input_CIRCDIST == "Montana": CIRCDIST = 72
elif input_CIRCDIST == "Nevada": CIRCDIST = 73
elif input_CIRCDIST == "N Mariana Island": CIRCDIST = 74
elif input_CIRCDIST == "Oregon": CIRCDIST = 75
elif input_CIRCDIST == "Washington East": CIRCDIST = 76
elif input_CIRCDIST == "Washington West": CIRCDIST = 77
elif input_CIRCDIST == "Colorado": CIRCDIST = 78
elif input_CIRCDIST == "Kansas": CIRCDIST = 79
elif input_CIRCDIST == "New Mexico": CIRCDIST = 80
elif input_CIRCDIST ==  "Oklahoma East": CIRCDIST = 81
elif input_CIRCDIST ==  "Oklahoma North": CIRCDIST = 82
elif input_CIRCDIST ==  "Oklahoma West": CIRCDIST = 83
elif input_CIRCDIST ==  "Utah": CIRCDIST =  84
elif input_CIRCDIST ==  "Wyoming": CIRCDIST=  85 
elif input_CIRCDIST ==  "Alabama Mid": CIRCDIST = 86
elif input_CIRCDIST ==  "Alabama North": CIRCDIST = 87
elif input_CIRCDIST ==  "Alabama South": CIRCDIST = 88
elif input_CIRCDIST ==  "Florida Mid": CIRCDIST = 89
elif input_CIRCDIST ==  "Florida North": CIRCDIST = 90
elif input_CIRCDIST ==  "Florida South": CIRCDIST = 91
elif input_CIRCDIST ==  "Georgia Mid": CIRCDIST = 92
elif input_CIRCDIST ==  "Georgia North": CIRCDIST = 93
elif input_CIRCDIST == "Georgia South": CIRCDIST = 94
st.write("CIRCDIST set to ", CIRCDIST)
st.write("")
st.write("")

SENTIMP_features = [ACCAP, AGE, GGDUM, BOOKER2, AROFFAP, 
            CIRCDIST, MITDUM, MONCIRC, ONSEX, NEWCIT, 
            NEWCNVTN, EWEDUC, NEWRACE, OFFTYPE2, ERIOD,
            PRIMARY, QUARTER, A, SAFEVALVE,
            OTCHPTS, WEAPON, XCRHISSR, LMIN, FY, 
            USSCIDN, GDL]

SENTIMP_input = np.array(SENTIMP_features).reshape(1, -1) 
# Import SENTIMP Model
with open('./trained-models/sentimp/sentimp2_rf', 'rb') as pickle_in:
    rf_SENTIMP = pickle.load(pickle_in) 
# Performance Metrics
predict_SENTIMP = st.button("Test SENTIMP Model")
if predict_SENTIMP:
    # Predict SENTIMP
    prediction_SENTIMP = rf_SENTIMP.predict(SENTIMP_input)
    if prediction_SENTIMP[0] == 0: st.info("The predicted sentence type is No Prison/Probation (Fine Only)")
    elif prediction_SENTIMP[0] == 1: st.info("The predicted sentence type is Prison Only (No Alternatives)")
    elif prediction_SENTIMP[0] == 2: st.info("The predicted sentence type is Prison + Confinement Conditions (Alternatives, Including Zone C Split Sentences)")
    elif prediction_SENTIMP[0] == 3: st.info("The predicted sentence type is Probation + Confinement Conditions (Alternatives)")
    elif prediction_SENTIMP[0] == 4: st.info("The predicted sentence type is Probation Only")

else:
    st.write("")

# MODEL 3
# st.subheader("CIRCDIST Model: Random Forest Model")
# # Features
# CIRCDIST_features = [ACCAP, AGE, GGDUM, BOOKER2, AROFFAP, 
#             MITDUM, MONCIRC, ONSEX, NEWCIT, 
#             NEWCNVTN, EWEDUC, NEWRACE, OFFTYPE2, ERIOD,
#             PRIMARY, QUARTER, A, SAFEVALVE, SENTIMP,
#             OTCHPTS, WEAPON, XCRHISSR, LMIN, FY, 
#             USSCIDN, ENSPLT0, GDL]

# CIRCDIST_input = np.array(CIRCDIST_features).reshape(1, -1) 
# # Performance Metrics
# st.write("**Accuracy Score during Training**")
# st.write("Train Score: 0.4087")
# st.write("Test Score: 0.4071")
# # Import CIRCDIST Model
# with open('./trained-models/circdist/circdist_rf', 'rb') as pickle_in:
#     rf_CIRCDIST = pickle.load(pickle_in)



# # Predict user input
# predict_CIRCDIST = st.button("Test CIRCDIST Model")
# if predict_CIRCDIST:
#     st.write("Running Model...")
#     prediction_CIRCDIST = rf_CIRCDIST.predict(CIRCDIST_input)
#     if prediction_CIRCDIST[0] == 1: st.info("The predicted district is District of Columbia")
#     elif prediction_CIRCDIST[0] == 2: st.info("The predicted district is Maine")
#     elif prediction_CIRCDIST[0] == 3: st.info("The predicted district is in Massachusetts")
#     elif prediction_CIRCDIST[0] == 4: st.info("The predicted district is in New Hampshire")
#     elif prediction_CIRCDIST[0] == 5: st.info("The predicted district is in Puerto Rico")
#     elif prediction_CIRCDIST[0] == 6: st.info("The predicted district is in Rhode Island")
#     elif prediction_CIRCDIST[0] == 7: st.info("The predicted district is in Connecticut")
#     elif prediction_CIRCDIST[0] == 8: st.info("The predicted district is in New York East")
#     elif prediction_CIRCDIST[0] == 9: st.info("The predicted district is in New York North")
#     elif prediction_CIRCDIST[0] == 10: st.info("The predicted district is in New York South")
#     elif prediction_CIRCDIST[0] == 11: st.info("The predicted district is in New York West")
#     elif prediction_CIRCDIST[0] == 12: st.info("The predicted district is in Vermont")
#     elif prediction_CIRCDIST[0] == 13: st.info("The predicted district is in Delaware")
#     elif prediction_CIRCDIST[0] == 14: st.info("The predicted district is in New Jersey")
#     elif prediction_CIRCDIST[0] == 15: st.info("The predicted district is in Penn. East")
#     elif prediction_CIRCDIST[0] == 16: st.info("The predicted district is in Penn. Mid")
#     elif prediction_CIRCDIST[0] == 17: st.info("The predicted district is in Penn. West")
#     elif prediction_CIRCDIST[0] == 18: st.info("The predicted district is in Virgin Islands")
#     elif prediction_CIRCDIST[0] == 19: st.info("The predicted district is in Maryland")
#     elif prediction_CIRCDIST[0] == 20: st.info("The predicted district is in N Carolina East")
#     elif prediction_CIRCDIST[0] == 21: st.info("The predicted district is in N Carolina Mid")
#     elif prediction_CIRCDIST[0] == 22: st.info("The predicted district is in N Carolina West")
#     elif prediction_CIRCDIST[0] == 23: st.info("The predicted district is in South Carolina")
#     elif prediction_CIRCDIST[0] == 24: st.info("The predicted district is in Virginia East")
#     elif prediction_CIRCDIST[0] == 25: st.info("The predicted district is in Virginia West")
#     elif prediction_CIRCDIST[0] == 26: st.info("The predicted district is in W Virginia North")
#     elif prediction_CIRCDIST[0] == 27: st.info("The predicted district is in W Virginia South")
#     elif prediction_CIRCDIST[0] == 28: st.info("The predicted district is in Louisiana East")
#     elif prediction_CIRCDIST[0] == 29: st.info("The predicted district is in Louisiana Middle")
#     elif prediction_CIRCDIST[0] == 30: st.info("The predicted district is in Louisiana West")
#     elif prediction_CIRCDIST[0] == 31: st.info("The predicted district is in Miss. North")
#     elif prediction_CIRCDIST[0] == 32: st.info("The predicted district is in Miss. South")
#     elif prediction_CIRCDIST[0] == 33: st.info("The predicted district is in Texas East")
#     elif prediction_CIRCDIST[0] == 34: st.info("The predicted district is in Texas North")
#     elif prediction_CIRCDIST[0] == 35: st.info("The predicted district is in Texas South")
#     elif prediction_CIRCDIST[0] == 36: st.info("The predicted district is in Texas West")
#     elif prediction_CIRCDIST[0] == 37: st.info("The predicted district is in Kentucky East")
#     elif prediction_CIRCDIST[0] == 38: st.info("The predicted district is in Kentucky West")
#     elif prediction_CIRCDIST[0] == 39: st.info("The predicted district is in Michigan East")
#     elif prediction_CIRCDIST[0] == 40: st.info("The predicted district is in Michigan West")
#     elif prediction_CIRCDIST[0] == 41: st.info("The predicted district is in Ohio North")
#     elif prediction_CIRCDIST[0] == 42: st.info("The predicted district is in Ohio South")
#     elif prediction_CIRCDIST[0] == 43: st.info("The predicted district is in Tennessee East")
#     elif prediction_CIRCDIST[0] == 44: st.info("The predicted district is in Tennessee Mid")
#     elif prediction_CIRCDIST[0] == 45: st.info("The predicted district is in Tennessee West")
#     elif prediction_CIRCDIST[0] == 46: st.info("The predicted district is in Illinois Cent")
#     elif prediction_CIRCDIST[0] == 47: st.info("The predicted district is in Illinois North")
#     elif prediction_CIRCDIST[0] == 48: st.info("The predicted district is in Illinois South")
#     elif prediction_CIRCDIST[0] == 49: st.info("The predicted district is in Indiana North")
#     elif prediction_CIRCDIST[0] == 50: st.info("The predicted district is in Indiana South")
#     elif prediction_CIRCDIST[0] == 51: st.info("The predicted district is in Wisconsin East")
#     elif prediction_CIRCDIST[0] == 52: st.info("The predicted district is in Wisconsin West")
#     elif prediction_CIRCDIST[0] == 53: st.info("The predicted district is in Arkansas East")
#     elif prediction_CIRCDIST[0] == 54: st.info("The predicted district is in Arkansas West")
#     elif prediction_CIRCDIST[0] == 55: st.info("The predicted district is in Iowa North")
#     elif prediction_CIRCDIST[0] == 56: st.info("The predicted district is in Iowa South")
#     elif prediction_CIRCDIST[0] == 57: st.info("The predicted district is in Minnesota")
#     elif prediction_CIRCDIST[0] == 58: st.info("The predicted district is in Missouri East")
#     elif prediction_CIRCDIST[0] == 59: st.info("The predicted district is in Missouri West")
#     elif prediction_CIRCDIST[0] == 60: st.info("The predicted district is in Nebraska")
#     elif prediction_CIRCDIST[0] == 61: st.info("The predicted district is in North Dakota")
#     elif prediction_CIRCDIST[0] == 62: st.info("The predicted district is in South Dakota")
#     elif prediction_CIRCDIST[0] == 63: st.info("The predicted district is in Alaska")
#     elif prediction_CIRCDIST[0] == 64: st.info("The predicted district is in Arizona")
#     elif prediction_CIRCDIST[0] == 65: st.info("The predicted district is in California Cent")
#     elif prediction_CIRCDIST[0] == 66: st.info("The predicted district is in California East")
#     elif prediction_CIRCDIST[0] == 67: st.info("The predicted district is in California North")
#     elif prediction_CIRCDIST[0] == 68: st.info("The predicted district is in California South")
#     elif prediction_CIRCDIST[0] == 69: st.info("The predicted district is in Guam")
#     elif prediction_CIRCDIST[0] == 70: st.info("The predicted district is in Hawaii")
#     elif prediction_CIRCDIST[0] == 71: st.info("The predicted district is in Idaho")
#     elif prediction_CIRCDIST[0] == 72: st.info("The predicted district is in Montana")
#     elif prediction_CIRCDIST[0] == 73: st.info("The predicted district is in Nevada")
#     elif prediction_CIRCDIST[0] == 74: st.info("The predicted district is in N Mariana Island")
#     elif prediction_CIRCDIST[0] == 75: st.info("The predicted district is in Oregon")
#     elif prediction_CIRCDIST[0] == 76: st.info("The predicted district is in Washington East")
#     elif prediction_CIRCDIST[0] == 77: st.info("The predicted district is in Washington West")
#     elif prediction_CIRCDIST[0] == 78: st.info("The predicted district is in Colorado")
#     elif prediction_CIRCDIST[0] == 79: st.info("The predicted district is in Kansas")
#     elif prediction_CIRCDIST[0] == 80: st.info("The predicted district is in New Mexico")
#     elif prediction_CIRCDIST[0] == 81: st.info("The predicted district is in Oklahoma East")
#     elif prediction_CIRCDIST[0] == 82: st.info("The predicted district is in Oklahoma North")
#     elif prediction_CIRCDIST[0] == 83: st.info("The predicted district is in Oklahoma West")
#     elif prediction_CIRCDIST[0] == 84: st.info("The predicted district is in Utah")
#     elif prediction_CIRCDIST[0] == 85: st.info("The predicted district is in Wyoming")
#     elif prediction_CIRCDIST[0] == 86: st.info("The predicted district is in Alabama Mid")
#     elif prediction_CIRCDIST[0] == 87: st.info("The predicted district is in Alabama North")
#     elif prediction_CIRCDIST[0] == 88: st.info("The predicted district is in Alabama South")
#     elif prediction_CIRCDIST[0] == 89: st.info("The predicted district is in Florida Mid")
#     elif prediction_CIRCDIST[0] == 90: st.info("The predicted district is in Florida North")
#     elif prediction_CIRCDIST[0] == 91: st.info("The predicted district is in Florida South")
#     elif prediction_CIRCDIST[0] == 92: st.info("The predicted district is in Georgia Mid")
#     elif prediction_CIRCDIST[0] == 93: st.info("The predicted district is in Georgia North")
#     elif prediction_CIRCDIST[0] == 94: st.info("The predicted district is in Georgia South")
# else:
#     st.write("")