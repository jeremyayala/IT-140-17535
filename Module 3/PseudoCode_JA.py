#Problem: A company wants a program that will calculate the weekly paycheck for an employee based on how many hours they worked.
# For this company, an employee earns $20 an hour for the first 40 hours that they work.
# The employee earns overtime, $30 an hour, for each hour they work above 40 hours.

Example: If an employee works 60 hours in a week, they would earn $20/hr for
the first 40 hours. Then they would earn $30/hr for the 20 hours they worked overtime.
Therefore, they earned: ($20/hr * 40hrs) + ($30/hr * 20 hrs) = $800 + $600 = $1400 total.

# getting hours worked and assign to input
INPUT "Hours Worked"  // input from user

#variables for hourly pay rates

Normal Rate variable = $20

Overtime Rate  = $30

#logic to calculate total overtime and regular hours worked

IF Hours Worked are less than or equal to 40
    Then assign Hours worked to Total Regular Hours
    and assign 0 to Total Overtime Hours
ELSE Hours Worked are greater than 40 :
        Then Assign 40 hours to Regular Hours
        And  Assign (CALCULATE Total Hours Worked - Regular Hours) to Total Overtime Hours

#printing to the console how many hours worked

Print ( Employee worked Total Regular Hours hours and Total Overtime Hours hours!)

#getting the pay

Total_Regular_Pay = Total Regular Hours Worked and Multiply by Normal Rate

Total_Overtime_Pay = Total_Overtime_Hours_Worked and Multiply by Overtime Rate

Total Pay = CALCULATE  Total Regular Pay + Total Overtime Pay

#printing the total pay

Print "You were paid Total Pay for the week!"

variables: Overtime Rate, Normal (Rate, Total_Regular_Hours,
           Total_Overtime_Hours, Total_Regular_Pay, Total_Overtime_Pay, Total_Pay)
