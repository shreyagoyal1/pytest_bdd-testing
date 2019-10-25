Feature: Authentication to demo
  As a user or attacker,
  I want to log into the system with invalid credentials,
  So I can view the demo data.
  
  Background:
    Given the OpenMRS home page is displayed

  Scenario: incorrect userpas attempts
    When the attacker tries to login with invalid "user" and invalid "pas" 
    Then check after 10 incorrect attempts, the systems allows to login with correct credentials or not

 

