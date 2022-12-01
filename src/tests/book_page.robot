*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Open Add Book Page
    Go To Add Book Page
    Add Book Page Should Be Open

Invalid Form Does Not Submit
    Go To Add Book Page
    Click Button  Submit
    Add Book Page Should Be Open

Valid Form Sumbits
    Go To Add Book Page
    Set Cite  BkMM
    Set Author  Moti Motivaatio
    Set Title  Motivaation Puute
    Set Year  2022
    Set Publisher  Motivaatio OY
    Click Button  Submit
    Add Book Page Should Be Open
    Go To Citations Page
    Page Should Contain  @Book
    Page Should Contain  BkMM
    Page Should Contain  author: { Moti Motivaatio }
    Page Should Contain  publisher: { Motivaatio OY }
    Page Should Contain  title: { Motivaation Puute }
    Page Should Contain  year: { 2022 }

*** Keywords ***
Set Cite
    [Arguments]  ${cite}
    Input Text  cite  ${cite}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}
