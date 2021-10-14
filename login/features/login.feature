Feature: Platform login

  Scenario: login (1a)
    Given a user accesses the login page (1a)
    When the user submits his signup with user and password
    Then the system redirects the user to the logged area


  Scenario:  Login failed without filling a user (1b)
    Given a user accesses the login page (1b)
    When the user submits his signup without the user
    Then the system displays Invalid user and/or password. Check the user and password and try again


  Scenario: Login failed without filling the password (1c)
    Given a user accesses the login page (1c)
    When the user submits his signup without the password
    Then the login button is disabled
