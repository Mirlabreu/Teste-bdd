Feature: Notes

  Scenario: View notes (5a)
    Given a user accesses the platform homepage (5a)
    When the user clicks My Notes
    Then the system displays the partial mean
    And the grade of each class


  Scenario: View the grade of only one lesson (5b)
    Given a user accesses My Notes (5b)
    When the user clicks on the desired lesson
    Then the system displays Evaluation and Workshop