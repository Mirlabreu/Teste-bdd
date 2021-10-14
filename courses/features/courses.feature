Feature: Courses

  Scenario: Access the enrolled courses (3a)
    Given a user accesses the platform homepage
    When the user clicks My Courses
    Then the system displays the ongoing courses of Application Development Fundamentals with Visual C# and Entrepreneurship and Ethics


  Scenario: Join course (3b)
    Given a user accesses the enrollment courses page
    When the user clicks Go to course
    And the system displays the course name and course didactic contract
    And the user accepts the didactic contract
    Then the system redirects to the class page


  Scenario: Join class (3c)
    Given a user accesses the Visual C# Application Development Fundamentals course
    When the user clicks join the class
    Then the system redirects to the webaula paddle