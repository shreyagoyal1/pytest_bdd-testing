Feature: Authentication to demo
  As a attacker,
  I want to log into the system with invalid credentials,
  So I can view the demo data.
  
  Background:
    Given the OpenMRS home page is displayed

  Scenario: incorrect username attempts
    When the  attacker tries to login with invalid "user" and valid password
    Then check after 10 incorrect attempts, the systems allows to login with correct credentials or not
