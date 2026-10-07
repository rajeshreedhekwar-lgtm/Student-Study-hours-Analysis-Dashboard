import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 1. LOAD EXCEL FILE
file_path = r"C:\Users\Rajeshree\OneDrive\Desktop\studyhours.xlsx"

df = pd.read_excel(file_path)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()


total_students = len(df)

avg_study_hours = df["Study hours per day"].mean()

avg_attendance = df["Attendance %"].mean()

avg_final_marks = df["Final Marks"].mean()

pass_percentage = (df["Result"].str.strip().str.lower() == "pass").mean() * 100



fig = plt.figure(figsize=(18, 10))
fig.suptitle(
    "STUDENT STUDY HOUR ANALYSIS DASHBOARD",
    fontsize=22,
    fontweight="bold",
    y=0.97
)


kpi_data = [
    ("TOTAL STUDENTS", f"{total_students}"),
    ("AVG STUDY HOURS", f"{avg_study_hours:.2f} hrs"),
    ("AVG ATTENDANCE", f"{avg_attendance:.1f}%"),
    ("AVG FINAL MARKS", f"{avg_final_marks:.1f}"),
    ("PASS PERCENTAGE", f"{pass_percentage:.1f}%")
]

x_positions = [0.05, 0.24, 0.43, 0.62, 0.81]

for i, (title, value) in enumerate(kpi_data):

    ax = fig.add_axes([x_positions[i], 0.82, 0.15, 0.10])

    ax.set_xticks([])
    ax.set_yticks([])

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1.5)

    ax.text(
        0.5, 0.68,
        title,
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

    ax.text(
        0.5, 0.30,
        value,
        ha="center",
        va="center",
        fontsize=18,
        fontweight="bold"
    )


ax1 = fig.add_axes([0.06, 0.48, 0.42, 0.27])

ax1.scatter(
    df["Study hours per day"],
    df["Final Marks"],
    s=70
)

ax1.set_title(
    "Study Hours vs Final Marks",
    fontsize=13,
    fontweight="bold"
)

ax1.set_xlabel("Study Hours per Day")
ax1.set_ylabel("Final Marks")
ax1.grid(alpha=0.3)

# Add student labels
for _, row in df.iterrows():

    ax1.annotate(
        str(int(row["Student"])),
        (row["Study hours per day"], row["Final Marks"]),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=8
    )



ax2 = fig.add_axes([0.53, 0.48, 0.42, 0.27])

department_hours = (
    df.groupby("Department")["Study hours per day"]
    .mean()
    .sort_values()
)

ax2.bar(
    department_hours.index,
    department_hours.values
)

ax2.set_title(
    "Average Study Hours by Department",
    fontsize=13,
    fontweight="bold"
)

ax2.set_xlabel("Department")
ax2.set_ylabel("Average Study Hours")

ax2.grid(axis="y", alpha=0.3)



ax3 = fig.add_axes([0.06, 0.14, 0.42, 0.27])

study_marks = (
    df.groupby("Study hours per day")["Final Marks"]
    .mean()
    .sort_index()
)

ax3.plot(
    study_marks.index,
    study_marks.values,
    marker="o",
    linewidth=2
)

ax3.set_title(
    "Average Final Marks by Study Hours",
    fontsize=13,
    fontweight="bold"
)

ax3.set_xlabel("Study Hours per Day")
ax3.set_ylabel("Average Final Marks")

ax3.grid(alpha=0.3)


ax4 = fig.add_axes([0.53, 0.14, 0.20, 0.27])

grade_counts = df["Grades"].value_counts()

ax4.pie(
    grade_counts.values,
    labels=grade_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

ax4.set_title(
    "Grade Distribution",
    fontsize=13,
    fontweight="bold"
)

ax5 = fig.add_axes([0.76, 0.14, 0.20, 0.27])

result_counts = df["Result"].str.strip().value_counts()

ax5.bar(
    result_counts.index,
    result_counts.values
)

ax5.set_title(
    "Pass / Fail Distribution",
    fontsize=13,
    fontweight="bold"
)

ax5.set_xlabel("Result")
ax5.set_ylabel("Number of Students")

ax5.grid(axis="y", alpha=0.3)


fig.text(
    0.5,
    0.04,
    "Student Study Hour Analysis | Excel Dataset | Python Dashboard",
    ha="center",
    fontsize=10
)


plt.show()
