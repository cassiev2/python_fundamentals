## REPOSITORY: python_fundamentals
This project is two differente python programs created as an exploration of python code fundamentals such as input, validation, if/then/else statements, text transformation, and mathematical formulas as part of the Interoperability (INFO-U762-01W) course curriculum. Humor and engagement was used in the design to stimulate creativity, exploration, and play - both in the coding and in the testing/running of the programs.

### 💡 A Note on Going 'Beyond'
I have worked in data analysis and report design for 14+ years using a number of different applications and languages including Crystal Reports, Business Objects, Power BI, Power Automate, HTML, and SAS. My employer is currently in the process of migrating from SAS to Python, which is new to me. I took this opportunity to try different functions, to "play" with Python to become more familiar, and to develop something that was fun to do. As my statistical team and I transition to Python, currently in early stages, we are not only learning a new language but re-navigating the interoperability between systems and processes. Current project estimates are 12-18 *months*, which is still expected to be a stretch to achieve. This has been a fun assignment. Hopefully you enjoy evaluating these programs as much as I enjoyed creating them.

### 🎯 Requirements
- Python 3.6+ 
- uses built in time and math modules from the standard Python library. 
- No requirements outside of the standard Python library, and no external dependencies.

##### ------------------------------------------------------------------------------------------------------------ #####

## PROGRAM: age_validator.py
An age validation and evalation program which demonstrates prompting for user input, validating, looping for retry, and case based response.

### 🚀 Run Instructions
Open a terminal in the python_fundamentals folder
Run: age_validator.py
The interactive program will open in the terminal and prompt for responses

### ⚠️ Assumptions 
That users are very unlikely to be under 10 years of age or over 110. 

### 🔬 Testing

## 1. Input Type validation (is it a number?)
| ID | Test scenario | Input | Expected | Result|
|---|---|---|---|---|---|
| T1.1 | integer | 10 | Accepted with no response, continues program | ✅ Pass |
| T1.2 | float | 55.3 | Accepted with no response, continues program | ✅ Pass |
| T1.3 | string | aaa | text response "oops", re-prompts to enter age | ✅ Pass |
| T1.4 | null value | NULL | text response "oops", re-prompts to enter age | ✅ Pass |

## 2. Input evaluation - is it in range (>=10 and <=110>)
| T2.1 | in range | 25 | Accepted with no response, continues program | ✅ Pass |
| T2.2 | below |  | 8 | text response "try again", re-prompts to enter age | ✅ Pass |
| T2.3 | above | 125 | text response "try again", re-prompts to enter age | ✅ Pass |
| T2.4 | as a float = above | 110.2 | text response "try again", re-prompts to enter age | ✅ Pass |

## 3. Text response based on input
| T3.1 | age < 27 | 25 | text response: not 1900s | ✅ Pass |
| T3. | age >= 27 | 60 | text response: Oregon trail | ✅ Pass |
| T3. | age is a float and < 27 | 25.4 | coverted to integer, text response: let's go with + not 1900s | ✅ Pass |
| T3. | age is a float and >= 27 | 27.3 | coverted to integer, text response: let's go with + Oregon Trail | ✅ Pass |

##### ------------------------------------------------------------------------------------------------------------ #####

## PROGRAM: LostHollow_Adventure.py
A nostalgic re-visit of text based adventure games which demonstrates INPUT & STRIP, UPPERCASE, TRANSFORM - REVERSE, EXCEPTION HANDLING, CALCULATE AREA FROM RADIUS, ANALYSIS/STRING SPLIT

### 🚀 Run Instructions

Open a terminal in the python_fundamentals folder
Run: LostHollow_Adventure.py
The interactive program will open in the terminal and prompt for responses

### ⚠️ Assumptions

### 🔬 Testing

## 1. Bread choice - expected: take, leave, transformations = strip, lower
| T1.1 | valid response | take | text response: you grab the bread and stuff it into your pack | ✅ Pass |
| T1.1 | valid response | leave | text response: you leave the bread on the counter | ✅ Pass |
| T1.1 | valid with lower | TAKE | text response: you grab the bread and stuff it into your pack. | ✅ Pass |
| T1.1 | valid with strip | TAKE+space | text response: you grab the bread and stuff it into your pack. | ✅ Pass |
| T1.1 | invalid choice | pick up | text response: drop bread, lose health | ✅ Pass |
| T1.1 | empty choice | NULL | text response: drop bread, lose health | ✅ Pass |

<more tests here>