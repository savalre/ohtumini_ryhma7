*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Open Citation Page
    Go To Citations Page
    Citations Page Should Be Open

Search Should Not Be Successful
    Go To Add Citation Page
    Select From List By Value  name:entry_type  book
    Click Button  Submit
    Set Cite  moti2022
    Set Author  Moti Motivaatio
    Set Title  Motivaation Puute
    Set Year  2022
    Set Publisher  Motivaatio OY
    Click Button  Submit

    Go To Citations Page
    Set Keyword  Seiti
    Click Button  Search
    Page Should Not Contain  Moti Motivaatio

Search Should Be Successful
    Go To Add Citation Page
    Select From List By Value  name:entry_type  book
    Click Button  Submit
    Set Cite  moti2022
    Set Author  Moti Motivaatio
    Set Title  Motivaation Puute
    Set Year  2022
    Set Publisher  Motivaatio OY
    Click Button  Submit

    Go To Citations Page
    Set Keyword  Moti
    Click Button  Search
    Page Should Contain  Moti Motivaatio

Delete One Citation
    Go To Add Citation Page
    Select From List By Value  name:entry_type  book
    Click Button  Submit

    Set Cite  moti2022
    Set Author  Moti Motivaatio
    Set Title  Motivaation Puute
    Set Year  2022
    Set Publisher  Motivaatio OY
    Click Button  Submit

    Go To Citations Page
    Click Button  moti2022

    Go To Citations Page
    Page Should Contain  moti2022
    Click Button  deselect_all
    Click Button  moti2022
    Click Button  Delete citation(s)
    Handle Alert
    Go To Citations Page
    Page Should Not Contain  moti2022

Delete One Of Two Citations
    Go To Add Citation Page
    Select From List By Value  name:entry_type  book
    Click Button  Submit
    Set Cite  moti2022
    Set Author  Moti Motivaatio
    Set Title  Motivaation Puute
    Set Year  2022
    Set Publisher  Motivaatio OY
    Click Button  Submit

    Go To Add Citation Page
    Select From List By Value  name:entry_type  booklet
    Click Button  Submit
    Set Cite  inspi2021
    Set Title  Inspiraation Puute
    Set Year  2021
    Click Button  Submit

    Go To Citations Page
    Click Button  deselect_all
    Page Should Contain  moti2022
    Page Should Contain  inspi2021
    Click Button  moti2022
    Click Button  Delete citation(s)
    Handle Alert
    Go To Citations Page
    Page Should Contain  inspi2021
    Page Should Not Contain  moti2022

Delete Two Citations
    Clear DB
    Go To Add Citation Page
    Select From List By Value  name:entry_type  book
    Click Button  Submit
    Set Cite  moti2022
    Set Author  Moti Motivaatio
    Set Title  Motivaation Puute
    Set Year  2022
    Set Publisher  Motivaatio OY
    Click Button  Submit
    Go To Citations Page

    Go To Add Citation Page
    Select From List By Value  name:entry_type  booklet
    Click Button  Submit
    Set Cite  inspi2021
    Set Title  Inspiraation Puute
    Set Year  2021
    Click Button  Submit

    Go To Citations Page
    Click Button  deselect_all
    Page Should Contain  moti2022
    Page Should Contain  inspi2021
    Click Button  select_all
    Click Button  Delete citation(s)
    Handle Alert
    Go To Citations Page
    Page Should Not Contain  inspi2021
    Page Should Not Contain  moti2022

*** Keywords ***
Citations Page Should Be Open
    Page Should Contain  List of citations

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

Set Keyword
    [Arguments]  ${keyword}
    Input Text  keyword  ${keyword}