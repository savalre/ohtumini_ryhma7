*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}
${ADD BOOK CITATION}  http://${SERVER}/book
${CITATIONS URL}  http://${SERVER}/citations

*** Keywords ***
Open And Configure Browser
    Clear DB
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
	Page Should Contain  Welcome

Add Book Page Should Be Open
    Page Should Contain  Add citation:

Go To Main Page
    Go To  ${HOME URL}

Go To Add Book Page
    Go To  ${ADD BOOK CITATION} 

Go To Citations Page
    Go To  ${CITATIONS URL}
