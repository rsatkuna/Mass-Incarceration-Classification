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

# RangeIndex: 800000 entries, 0 to 799999
# Data columns (total 28 columns): Index matches dictionary
st.subheader("All Input Variables")
# Index: 0
# https://nce.fd.org/sites/nce.fd.org/files/publications/ACCA%20and%20CO%20presentation%2C%20FINAL.pdf
input_ACCAP = st.selectbox("**Armed Career Status**", ("Not applied", "Applied", "Inapplicable"))
if input_ACCAP == "Applied": ACCAP = 1 
elif input_ACCAP == "Not applied": ACCAP = 0
else: input_ACCAP = ACCAP = -999
st.write("ACCAP set to ", ACCAP)
st.write("")
st.write("")

# Index: 1
input_AGE = st.slider("**Defendant's Age** ( >= 16 years )", 0, 98)
if input_AGE <= 16: AGE = -999
else: AGE = input_AGE
st.write("AGE set to ", AGE)
st.write("")
st.write("")


# Index: 2
# https://content.next.westlaw.com/Document/NE79C68F0B8AD11D8983DF34406B5929B/View/FullText.html?transitionType=Default&contextData=(sc.Default)&firstPage=true
input_GGDUM = st.selectbox("**Defendant's Aggravating Role**", ("No Adjustment Applied", "Valid Value (1-4) Applied", "Indeterminable, invalid value applied, or Inapplicable"))
if input_GGDUM == "No Adjustment Applied": GGDUM = 0
elif input_GGDUM == "Valid Value (1-4) Applied": GGDUM = 1
elif input_GGDUM == "Indeterminable, invalid value applied, or Inapplicable": GGDUM = 99
else: GGDUM = -999
st.write("GGDUM set to ", GGDUM)
st.write("")
st.write("")

# Index: 3 
input_BOOKER2 = st.selectbox("**Sentence Relativity to Guidleline Range**", ("Within Range", "Above Departure", "Government Sponsored", "Below Range"))
# https://en.wikipedia.org/wiki/United_States_Federal_Sentencing_Guidelines
if input_BOOKER2 == "Within Range": BOOKER2 = 0
elif input_BOOKER2 == "Above Departure": BOOKER2 = 1
elif input_BOOKER2 == "Government Sponsored": BOOKER2 = 2
elif input_BOOKER2 == "Below Range": BOOKER2 = 4
else: BOOKER2 = 0 
st.write("BOOKER2 set to", BOOKER2)
st.write("")
st.write("")

# Index: 4
input_AROFFAP = st.selectbox("**Career Offender Status**", ("Not Applied", "Applied"))
if input_AROFFAP == "Applied": AROFFAP = 1 
elif input_AROFFAP == "Not Applied": AROFFAP = 0
else: AROFFAP = 0
st.write("AROFFAP set to ", AROFFAP)
st.write("")
st.write("")


# Index: 5
input_CIRCDIST = st.selectbox("**District of the Circuit Court**", ("Dist of Columbia", "Maine", "Massachusetts", "New Hampshire", "Puerto Rico", "Rhode Island", 
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


# Index: 6
input_MITDUM = st.selectbox("**Mitigating Role Adjustment**", ("Inapplicable", "No Adjustment Applied", "Valid Value (1-4) Applied"))
if input_MITDUM == "No Adjustment Applied": MITDUM = 1 
elif input_MITDUM == "Valid Value (1-4) Applied": MITDUM = 0
else: MITDUM = 0
st.write("MITDUM set to ", MITDUM)
st.write("")
st.write("")

# Input: 7
input_MONCIRC = st.number_input("**Judicial Circuit**", 0, 11)
MONCIRC = input_MONCIRC
st.write("MONCIRC set to ", MONCIRC)
st.write("")
st.write("")

# Index: 8
input_ONSEX = st.selectbox("**Offender's Sex**", ("Unspecified", "Male", "Female"))
if input_ONSEX == "Male": ONSEX = 1 
elif input_ONSEX == "Female": ONSEX = 0
else: ONSEX = 0
st.write("ONSEX set to ", ONSEX) 
st.write("")
st.write("")

# Index: 9
input_NEWCIT = st.radio("**Citizenship Status**", ["U.S.", "Non-U.S."])
if input_NEWCIT == "U.S.": NEWCIT = 1 
elif input_NEWCIT == "Non-U.S.": NEWCIT = 0
else: NEWCIT = 0
st.write("NEWCIT set to ", NEWCIT)
st.write("The US Sentencing Commission does not differentiate between Legal and Illegal Immigrants for their data collection nor analysis of sentencing data.")
st.write("")
st.write("")

# Index: 10
input_NEWCNVTN = st.radio("Citizenship Status", ["Plea", "Trial"])
if input_NEWCNVTN == "Plea": NEWCNVTN = 1 
elif input_NEWCNVTN == "Trial": NEWCNVTN = 0
else: NEWCNVTN = -999
st.write("NEWCNVTN set to ", NEWCNVTN)
st.write("")
st.write("")


# Index: 11
input_EWEDUC = st.selectbox("**Education Level**", ("Less Than H.S. Graduate", "H.S. Graduate", "Some College", "College Graduate"))
if input_EWEDUC == "Less Than H.S. Graduate": EWEDUC = 1
elif input_EWEDUC == "H.S. Graduate": EWEDUC = 3
elif input_EWEDUC == "Some College": EWEDUC = 5
elif input_EWEDUC == "College Graduate": EWEDUC = 6
else: NEWCNVTN = 7
st.write("EWEDUC set to ", EWEDUC)
st.write("")
st.write("")


# Index: 12
input_NEWRACE = st.selectbox("**Defendant's Race**", ("Other", "White", "Black", "Hispanic"))
if input_NEWRACE == "White": NEWRACE = 1
elif input_NEWRACE == "Black": NEWRACE = 2
elif input_NEWRACE == "Hispanic": NEWRACE = 3
elif input_NEWRACE == "Other": NEWRACE = 6
elif input_NEWRACE == "option": NEWRACE = 0
else: NEWRACE = -999
st.write("NEWRACE set to ", NEWRACE)
st.write("")
st.write("")

# OFFTYPE2
# Index: 
input_OFFTYPE2 = st.selectbox("**Primary Offense**", ("Murder", "Manslaughter", "Kidnapping/Hostage Taking", "Sexual Abuse", "Assault", "Robbery", "Arson",
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
else: OFFTYPE2 = -999
st.write("OFFTYPE2 set to ", OFFTYPE2)
st.write("")
st.write("")

# ERIOD
# Index: 
input_ERIOD = st.radio("**Time Period by Act**", ["Koon Period (June 13, 1996 through April 30, 2003)",
"PROTECT Act Period (May 1, 2003 through June 24, 2004)", 
"Booker Period (January 12, 2005 through December 10, 2007)",
"Gall Period (December 11, 2007 through September 30, 2011)"])
if input_ERIOD == "Koon Period (June 13, 1996 through April 30, 2003)": ERIOD = 1
elif input_ERIOD == "PROTECT Act Period (May 1, 2003 through June 24, 2004)": ERIOD = 2
elif input_ERIOD == "Booker Period (January 12, 2005 through December 10, 2007)": ERIOD = 3
elif input_ERIOD == "Gall Period (December 11, 2007 through September 30, 2011)": ERIOD = 4
st.write("ERIOD set to ", ERIOD)
st.write("")
st.write("")

# Index: 15
input_PRIMARY = st.selectbox("**Primary drug type involved**", ("None", "Cocaine", "Crack", "Heroin", "Marijuana", "Methamphetamine", "Other"))
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

# Index: 16
# input_QUARTER = st.("**Fiscal Year quarter**")
# if 0 = No Prison/Probation (Fine Only)
# 1 = Prison Only (No Alternatives)
# 2 = Prison + Confinement Conditions (Alternatives, Including Zone C Split Sentences)
# 3 = Probation + Confinement Conditions (Alternatives)
# 4 = Probation Only
# else: QUARTER = -999
# st.write("QUARTER set to ", QUARTER)
# st.write("")
# st.write("")

# Index: 17
# input_A = st.("**Government Sponsored Categories**")
# if 0 = Within Range
# 0 = Safety Valve Not Applied
# 1 = Safety Valve Applied
# 2 = Missing, Indeterminable, or Inapplicable
# st.write("A set to ", A)
# st.write("")
# st.write("")

# Index: 18
# input_SAFEVALVE = st.("**o**")
# if input_SAFEVALVE == "": SAFEVALVE = 1 
# elif input_SAFEVALVE == "": SAFEVALVE = 0
# elif input_SAFEVALVE == "Inapplicable": 2
# else: SAFEVALVE = -999
# st.write("SAFEVALVE set to ", SAFEVALVE)
# st.write("")
# st.write("")

# Index: 19
# input_SENTIMP = st.("**Criminal History Points Applied**")
# if input_SENTIMP == "Plea": SENTIMP = 1 
# else: SENTIMP = -999
# st.write("SENTIMP set to ", SENTIMP)
# st.write("")
# st.write("")

# Index: 20
# input_OTCHPTS = st.("**type of sentence**")
# 0 = No Prison/Probation (Fine Only)
# 1 = Prison Only (No Alternatives)
# 2 = Prison + Confinement Conditions (Alternatives, Including Zone C Split Sentences)
# 3 = Probation + Confinement Conditions (Alternatives)
# 4 = Probation Only
# else: OTCHPTS = -999
# st.write("OTCHPTS set to ", OTCHPTS)
# st.write("")
# st.write("")

# Index: 21
# input_WEAPON = st.("**SOC weapon enhancement**")
# 0 = No SOC Weapon Enhancement Nor 18§924(c) Charge Present
# 1 = SOC Weapon Enhancement or 18§924(c) Charge Present
# -999 = Missing, Indeterminable, or Inapplicable
# st.write("WEAPON set to ", WEAPON)
# st.write("")
# st.write("")

# Index: 22
# input_XCRHISSR = st.("**o**")
# if input_XCRHISSR < 6: XCRHISSR = input_XCRHISSR 
# else: XCRHISSR = -999
# st.write("XCRHISSR set to ", XCRHISSR)
# st.write("")
# st.write("")

# Index: 23
# input_LMIN = st.("**Defendant's final criminal history category (I-VI), as determined by the court.**")
# if input_LMIN == "Plea": LMIN = 1 
# elif input_LMIN == "Trial": LMIN = 0
# else: LMIN = -999
# st.write("LMIN set to ", LMIN)
# st.write("")
# st.write("")

# Index: 24
# input_FY = st.("**o**", 1996, 2011)
# if input_FY <= 2011: FY = input_FY 
# st.write("FY set to ", FY)
# st.write("")
# st.write("")

# Index: 25
# input_USSCIDN = st.("**o**")
# if input_USSCIDN == "Plea": USSCIDN = 1 
# elif input_USSCIDN == "Trial": USSCIDN = 0
# else: USSCIDN = -999
# st.write("This identification number might have need")
# st.write("")
# st.write("")

# Index: 26
# input_ENSPLT0 = st.("**o**")
# if input_ENSPLT0 == "Plea": ENSPLT0 = 1 
# elif input_ENSPLT0 == "Trial": ENSPLT0 = 0
# else: ENSPLT0 = -999
# st.write("ENSPLT0 set to ", ENSPLT0)
# st.write("")
# st.write("")


# Index: 27
# input_GDL = st.("**o**")
# if input_GDL == "Plea": GDL = 1 
# elif input_GDL == "Trial": GDL = 0
# else: GDL = -999
# st.write("GDL set to ", GDL)
# st.write("")
# st.write("")

# TODO: do conditionals for each variable
# TODO: give each variable a label
# TODO: git each variable data + add to dictionary

# features = [ACCAP, AGE, GGDUM, BOOKER2, AROFFAP, 
#             CIRCDIST, MITDUM, MONCIRC, ONSEX, NEWCIT, 
#             NEWCNVTN, EWEDUC, NEWRACE, OFFTYPE2, ERIOD, 
#             PRIMARY, QUARTER, A, SAFEVALVE, SENTIMP,
#             OTCHPTS, WEAPON, XCRHISSR, LMIN, FY, 
#             USSCIDN, ENSPLT0, GDL]


st.title("Modeling Process")
# user_input = np.array(features).reshape(1, -1)

# TARGET 3
st.subheader("Target Class: ERIOD")
st.write("Modeling Federal Act Time Periods")
# insert cleaning and preprocessing content

# TARGET 2
st.subheader("Target Class: SENTIMP")
st.write("Modeling Sentence Types based on Sentencing Trends")
# insert cleaning and preprocessing content

# TARGET 3
st.header("Target Class: CIRCDIST")
st.subheader("Modeling Circuit Court District's Sentencing Trends")
# insert cleaning and preprocessing content

# TEST USER INPUT AS AN EXAMPLE
st.title("Test Production Model with Inputs")

# # MODEL 1
st.subheader("ERIOD Model: Random Forest Classifier")
# # Import ERIOD Model
# with open('./trained-models/eriod/eriod_rf', 'rb') as pickle_in:
#     rf_ERIOD = pickle.load(pickle_in)
# # Performance Metrics
st.write("**Accuracy Score during Training**")
st.write("Train Score: 0.9929")
st.write("Test Score: 0.9899")
# # # Predict user input
# prediction_ERIOD = rf_ERIOD.predict(user_input)
# st.write(f"The predicted sentence type is {prediction_ERIOD[0]}") 

# # MODEL 2
st.subheader("SENTIMP Model: Random Forest Model")
# # # Import SENTIMP Model
# with open('./trained-models/sentimp/sentimp2_rf', 'rb') as pickle_in:
#     rf_SENTIMP = pickle.load(pickle_in) 
# # Performance Metrics
st.write("**Accuracy Score during Training**")
st.write("Train Score: 0.9528")
st.write("Test Score: 0.9447")
# # Predict user input
# prediction_SENTIMP = rf_SENTIMP.predict(user_input)
# st.write(f"The predicted sentence type is {prediction_SENTIMP[0]}") 

# # MODEL 3
st.subheader("CIRCDIST Model: Random Forest Model")
# # Performance Metrics
st.write("**Accuracy Score during Training**")
st.write("Train Score: 0.4087")
st.write("Test Score: 0.4071")
# # Import CIRCDIST Model
# with open('./trained-models/circdist/circdist_rf', 'rb') as pickle_in:
#     rf_CIRCDIST = pickle.load(pickle_in)
# # Predict user input
# prediction_CIRCDIST = rf_CIRCDIST.predict(user_input)
# st.write(f"The predicted sentence type is {prediction_CIRCDIST[0]}") 