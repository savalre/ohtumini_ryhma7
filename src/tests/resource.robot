*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${HOME URL}  http://${SERVER}
${ADD BOOK CITATION}  http://${SERVER}/book

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

//Placeholder test
Main Page Should Be Open
	Page Should Contain  Flask

Go To Main Page
    Go To  ${HOME URL}

Go To Add Book Page
    Go To  ${ADD BOOK CITATION} 
