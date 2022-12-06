*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Open Add Citation Page
    Go To Add Citation Page
    Add Citation Page Should Be Open

Invalid Form Does Not Submit
    Go To Add Citation Page
    Click Button  Submit
    Add Citation Page Should Be Open

Valid Entry_type From Form Opens Correct Page
    Go To Add Citation Page
    Select From List By Value  name:entry_type  misc
    Click Button  Submit
    Page Should Contain  Add a new misc citation

Valid Form Adds A New Citation
    Go To Add Citation Page
    Select From List By Value  name:entry_type  book
    Click Button  Submit
    Set Cite  moti2022
    Set Author  Moti Motivaatio
    Set Title  Motivaation Puute
    Set Year  2022
    Set Publisher  Motivaatio OY
    Click Button  Submit
    Add Citation Page Should Be Open
    Go To Citations Page
    Page Should Contain  @book
    Page Should Contain  moti2022
    Page Should Contain  author: { Moti Motivaatio }
    Page Should Contain  publisher: { Motivaatio OY }
    Page Should Contain  title: { Motivaation Puute }
    Page Should Contain  year: { 2022 }

Invalid Form Does Not Add A New Citation
    Go To Add Citation Page
    Select From List By Value  name:entry_type  misc
    Click Button  Submit
    Set Author  Ricotrap
    Set Title  God why
    Set Year  2022
    Click Button  Submit
    Page Should Contain  Add a new misc citation
    Go To Citations Page
    Page Should Not Contain  @misc
    Page Should Not Contain  author: { Ricotrap }
    Page Should Not Contain  title: { God why }

*** Keywords ***
Set Cite
    [Arguments]  ${cite_as}
    Input Text  cite_as  ${cite_as}

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
