*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}
${ADD CITATION URL}  http://${SERVER}/new
${CITATIONS URL}  http://${SERVER}/citations
${BIB URL}  http://${SERVER}/citations.bib

*** Keywords ***
Open And Configure Browser
    Clear DB
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
	Page Should Contain  Welcome

Add Citation Page Should Be Open
    Page Should Contain  Add a new citation

Go To Main Page
    Go To  ${HOME URL}

Go To Add Citation Page
    Go To  ${ADD CITATION URL} 

Go To Citations Page
    Go To  ${CITATIONS URL}

Go To Bib Page
    Go To  ${BIB URL}
