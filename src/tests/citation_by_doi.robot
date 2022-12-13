*** Settings ***
Resource  resource.robot
Resource  form_input_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Add Citation By Valid Doi
    Go To Add Citation Page
    Set Cite As  moti_22
    Set Doi  10.1145/1151954.1067596
    Click Button  submit_doi
    Add Citation Page Should Be Open
    Go To Citations Page
    Page Should Contain  article
    Page Should Contain  moti_22
    Page Should Contain  Ilana Bass and Dvir Lanzberg
    Page Should Contain  ACM SIGCSE Bulletin
    Page Should Contain  Iterative implementation of DFS
    Page Should Contain  37
    Page Should Contain  2005

Faulty Doi Is Not Added
    Go To Add Citation Page
    Set Cite As  moti_2022
    Set Doi  123455
    Click Button  submit_doi
    Add Citation Page Should Be Open
    Go To Citations Page
    Page Should Not Contain  moti_2022

Entry Without Cite As Is Not Added
    Go To Add Citation Page
    Set Doi  10.1145/1067445.1067596
    Click Button  submit_doi
    Add Citation Page Should Be Open
    Go To Citations Page
    Page Should Not Contain  @inproceedings
