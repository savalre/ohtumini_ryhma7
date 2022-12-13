*** Settings ***
Resource  resource.robot
Resource  form_input_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Bib With No Citations
    Go To Bib Page
    Page Should Contain  Add a new citation

Bib Select One Citation
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

    Go To Bib Page
    Page Should Contain  @book
    Page Should Contain  moti2022
    Page Should Contain  author = {Moti Motivaatio}
    Page Should Contain  publisher = {Motivaatio OY}
    Page Should Contain  title = {Motivaation Puute}
    Page Should Contain  year = {2022}

Bib Select All Citations
    Go To Add Citation Page
    Select From List By Value  name:entry_type  booklet
    Click Button  Submit

    Set Cite  inspi2021
    Set Title  Inspiraation Puute
    Set Year  2021
    Click Button  Submit

    Go To Citations Page
    Click Button  select_all

    Go To Bib Page
    Page Should Contain  @book
    Page Should Contain  moti2022
    Page Should Contain  author = {Moti Motivaatio}
    Page Should Contain  publisher = {Motivaatio OY}
    Page Should Contain  title = {Motivaation Puute}
    Page Should Contain  year = {2022}

    Page Should Contain  @booklet
    Page Should Contain  inspi2021
    Page Should Contain  title = {Inspiraation Puute}
    Page Should Contain  year = {2021}
    
Bib Deselect All Citations
    Go To Citations Page
    Click Button  select_all
    Click Button  deselect_all
    Go To Bib Page
    Page Should Contain  Add a new citation

Bib Deselect All Citations And Select One
    Go To Citations Page
    Click Button  select_all
    Click Button  deselect_all
    Click Button  inspi2021
    Go To Bib Page
    Page Should Contain  inspi2021
    Page Should Not Contain  moti2022
