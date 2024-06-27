import pandas as pd
import numpy as np

dataFrame = pd.read_excel("C:/Users/Alperen Arda/OneDrive/Desktop/GitHub/Python-Boot-Camp-All-Codes-and-Projects/Lectures/PythonBootCamp/27-SalarySheet (1).xlsx")
print("Total number of lines: " + str(dataFrame["Employee Name"].count()))
print("\nAverage salary of the company: " + str(dataFrame["Salary"].mean()) + "€")

departmentFrame = dataFrame.groupby("Department")
sortedDepartmentFrame = departmentFrame["Salary"].mean().sort_values(ascending=False)
print("\nAverage salary comparing according to departments:\n" + str(sortedDepartmentFrame))

print("\nAverage salary comparing according to title:\n" + str(dataFrame.groupby("Title")["Salary"].mean().sort_values(ascending=False)))

seniorSalary = dataFrame[dataFrame["Title"] == "Senior"]["Salary"].mean()
juniorSalary = dataFrame[dataFrame["Title"] == "Junior"]["Salary"].mean()
print(f"\nAverage senior salary is {round((seniorSalary * 100 / juniorSalary), 2) - 100}% more than average junior "
      f"salary ")

softwareSeniorSalary = dataFrame[(dataFrame["Department"] == "Software Development") & (dataFrame["Title"] == "Senior")]["Salary"].mean()
softwareJuniorSalary = dataFrame[(dataFrame["Department"] == "Software Development") & (dataFrame["Title"] == "Junior")]["Salary"].mean()
print(f"\nAverage senior salary in software development is {round((softwareSeniorSalary * 100 / softwareJuniorSalary)) - 100}% more than average junior "
      f"salary in software development department.")

financeCLevelSalary = dataFrame[(dataFrame["Department"] == "Finance") & (dataFrame["Title"] == "C-level")]["Salary"].mean()
financeMidSeniorSalary = dataFrame[(dataFrame["Department"] == "Finance") & (dataFrame["Title"] == "Mid-Senior")]["Salary"].mean()
print(f"\nAverage c-level salary in finance department is {round((financeCLevelSalary * 100 / financeMidSeniorSalary)) - 100}% more than average mid-senior "
      f"salary in finance department.")

numberOfSoftwareClevel = dataFrame[(dataFrame["Department"] == "Software Development") & (dataFrame["Title"] == "C-level")]["Employee Name"].count()
numberOfMarketing = dataFrame[(dataFrame["Department"] == "Marketing") & (dataFrame["Title"] == "C-level")]["Employee Name"].count()
print(f"\nNumber of C-level person in software development department is {round((numberOfSoftwareClevel / numberOfMarketing))} times more than number of C-level person in marketing department "
      f"salary in finance department.")
