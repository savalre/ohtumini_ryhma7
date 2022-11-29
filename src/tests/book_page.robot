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
    Set Cite  cite
    Set Author  author
    Set Title  title
    Set Year  2022
    Set Publisher  publisher
    Click Button  Submit
    Add Book Page Should Be Open

*** Keywords ***
Add Book Page Should Be Open
    Page Should Contain  Add citation:

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
