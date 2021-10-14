Feature: Help

  Scenario: help (2a)
    Given a user accesses the login page (2a)
    When the user clicks I need help
    Then the system redirects to the home page of the platform https://leadfortaleza.com.br/portal
