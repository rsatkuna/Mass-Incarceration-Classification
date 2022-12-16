## Binary Classifiers: Focus on feature importance
ACCAP: Armed Career Criminal status 
 0 = Not Applied
 1 = Applied
 · = Missing, Indeterminable, or Inapplicable
CAREER: Career Offender status applied under §4B1.1
 1 = Career Offender Impacted FOL
 · = No impact, Missing or Indeterminable
 
MONSEX: Indicates the offender's gender.

NEWCIT: Citizenship of the defendant.
0 = U.S.
1 = Non-U.S. (Includes Legal and
Illegal Aliens)
· = Missing, Indeterminable, or Inapplicable

NEWCIT: Citizenship of the defendant.
0 = Plea
1 = Trial
· = Missing, Indeterminable, or Inapplicable

SAFEVALVE: Indicator of whether or not the “Safety Valve” provision (§5C1.2 or 2D1.1) 
0 = Safety Valve Not Applied
1 = Safety Valve Applied
. = Missing, Indeterminable, or Inapplicable

WEAPON: Indicates if there is an SOC weapon enhancement or an 18§924(c) conviction. 
0 = No SOC Weapon Enhancement Nor 18§924(c) Charge Present
1 = SOC Weapon Enhancement or 18§924(c) Charge Present
· = Missing, Indetermined, or Inapplicable

## Multiple Classifiers: Focus on feature importance
OFFTYPE2: Offense Type
1 = Murder
 2 = Manslaughter
 3 = Kidnapping/Hostage Taking
 4 = Sexual Abuse
 5 = Assault
 6 = Robbery (includes MONOFFTP= 7, other Robbery)
 9 = Arson
10 = Drugs - Trafficking, Manufacturing, and Importing
11 = Drugs - Communication Facilities
12 = Drugs: - Simple Possession
13 = Firearms (Includes Firearms Use, Possession, and Trafficking) (includes MONOFFTP= 14, Firearms possession and
Trafficking)
15 = Burglary/Breaking and Entering
16 = Auto Theft
17 = Larceny
18 = Fraud
19 = Embezzlement
20 = Forgery/Counterfeiting
21 = Bribery
22 = Tax Offenses
23 = Money Laundering
24 = Racketeering /Extortion (includes MONOFFTP= 8, Extortion)
25 = Gambling/Lottery
26 = Civil Rights Offenses
27 = Immigration
28 = Pornography/Prostitution (Value not available after FY2009)
29 = Prison Offenses
30 = Administration of Justice (Includes accessory after the fact, misprision of felony, and witness tampering)
31 = Environmental, Game, Fish, and Wildlife Offenses
32 = National Defense Offenses
33 = Antitrust Violations
34 = Food and Drug Offenses
35 = Traffic Violations and Other Offenses (Includes Other Drug, Environmental, Firearms, Miscellaneous Property
Crimes, Violent, and Traffic offenses) (includes MONOFFTP= 35, 36, 37, 38, 39, 40, 41)
42 = Child Pornography (Value not available prior FY2010)
43 = Obscenity (Value not available prior FY2010)
44 = Prostitution (Value not available prior FY2010)
. = Missing

GDL: Chapter Two Guideline applied in a case
2BNew = Fraud Offenses
2D1.1 = Drug Trafficking Offenses
 (includes 2D1.2)
2G2.1 = Child Pornography Production
 Offenses
2G2.2 = Child Pornography Possession
 Offenses (includes 2G2.4)
2L1.1 = Alien Smuggling Offenses
2L1.2 = Illegal Entry Offenses
2K2.1 = Firearms Offenses
2_#.# = Chapter 2 Guideline Applied of
All Other Offenses
· = Missing, Indeterminable, or Inapplicable

NEWEDUC: Indicates whether the case was settled by plea agreement or trial.
1 = Less Than H.S. Graduate
3 = H.S. Graduate
5 = Some College
6 = College Graduate
· = Missing, Indeterminable, or Inapplicable

NEWRACE: Race of defendant.
1 = White
2 = Black
3 = Hispanic
6 = Other
· = Missing, Indeterm

XCRHISSR: Defendant's final criminal history category (I-VI), as determined by the court.
Range: 1 thru 6
· = Missing, Indeterminable, or Inapplicable

**PERIOD: Time Period in which the case was sentenced.
Range: 1-4
1 = Koon Period (June 13, 1996 through April 30, 2003)
2 = PROTECT Act Period (May 1, 2003 through June 24, 2004)
3 = Booker Period (January 12, 2005 through December 10, 2007)
4 = Gall Period (December 11, 2007 through September 30, 2011)
. = Missing.**

PRIMARY: Primary drug type involved in the offense standardized across all fiscal years.
 1 = Cocaine
 2 = Crack
 3 = Heroin
 4 = Marijuana
 6 = Methamphetamine
77 = Other
 · = Missing, Indeterminable, or Inapplicable

PRIMARY: Primary drug type involved in the offense standardized across all fiscal years. 
Range: 1-4
1 = Oct 1 thru Dec 31
2 = Jan 1 thru March 31
3 = April 1 thru June 30
4 = July 1 thru Sept 30

SA: This variable is an expanded version of BOOKER2, with the different government sponsored categories broken out. 
0 = Within Range
1 = Above Range
2 = 5K1.1/Substantial Assistance
3 = Early Disposition/5K3.1
4 = Government Sponsored - Below Range
5 = Non-Govt Sponsored Below Range
· = Missing, Indeterminable, or Inapplicable

SENTIMP: Indicates what type of sentence was given (prison, probation, probation plus alternatives, or prison/split sentence).
0 = No Prison/Probation (Fine Only)
1 = Prison Only (No Alternatives)
2 = Prison + Confinement Conditions (Alternatives, Including Zone C Split Sentences)
3 = Probation + Confinement Conditions (Alternatives)
4 = Probation Only
 · = Missing, Indetermined or Inapplicable

## Quantitiative Variables: Flask/Streamlit input and play
AGE: Age at the time of sentencing
16 through 98
LOSS_2B: The dollar amount of loss for which the offender is held responsible
Range: 0-3,400,406,949
0 = No loss
· =Missing, Indeterminable, or
Inapplicable (Includes cases with
some loss, but amount not specified)

SENSPLT0: The trumped total prison sentence, in months (sentence of 470 months or more, including life, are reported as 470 months)
Range: 0 thru 470
0 = Probation
· = Missing, Indeterminable, or Inapplicable

TOTCHPTS: The total number of criminal history points applied.
Range: 0 thru 99
0 = None
· = Missing, Indeterminable, or Inapplicable

## Locations: Display common information/[External Data](https://www.prisonpolicy.org/data/) 
CIRCDIST: Circuit District
Range: 1 thru 94
