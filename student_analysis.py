import pandas as pd

#Dataset
data = {
    "name":["Aman", "Riya", "Rahul", "Sneha", "Karan"],
    "city":["Delhi", "Noida", "Delhi", "Noida", "Delhi"],
    "marks":[85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

print("Full Data: \n", df)

#Topper
print("\n Topper:")
print(df.sort_values("marks", ascending = False).head(1))

#marks of Delhi students
print("\n Delhi Students Marks:")
print(df[df["city"] == "Delhi"]["marks"])

#Average mrks per city
print("\n Average Marks Per City:")
print(df.groupby("city")["marks"].mean())

#Student with marks > 80
print("\n Students With Marks > 80:")
print(df[df["marks"] > 80])

#Student of Noida with above 85 marks
print("\n Noida Students with Marks > 85:")
print(df[(df["city"] == "Noida") & (df["marks"] > 85)])

#Lowest marks student
print("\n Lowest Marks Student:")
print(df.sort_values("marks").head(1))

#Total students per city
print("\n Total Students Per City:")
print(df["city"].value_counts())

#Total Delhi students
print("\n Total Delhi Students:")
print(df[df["city"] == "Delhi"]["name"].count())

#Top 3 students
print("\n Top 3 Students:")
print(df.sort_values("marks", ascending = False).head(3))