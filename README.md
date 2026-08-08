<p align="center">
  <img src="https://github.com/user-attachments/assets/d063779c-ff50-4792-a41a-4ffaa559dca5" alt="Project banner" style="max-width:100%;height:auto;border-radius:8px;box-shadow:0 2px 12px rgba(0,0,0,0.12);" />
</p>

# 📊 Data Jobs Market Analysis & Salary Dashboard

An end-to-end **Excel Data Analytics project** analyzing the 2023 data science job market. This project combines **data cleaning, exploratory data analysis, data modeling, salary analysis, skill analysis, and interactive dashboard development** using Microsoft Excel.

Using advanced Excel tools such as **Power Query, Power Pivot, PivotTables, DAX, Pivot Charts, advanced formulas, and data validation**, the project transforms raw job-market data into meaningful insights about salaries, technical skills, job titles, employment types, and geographic differences.

The project consists of two complementary parts:

* 📈 **Data Jobs Market Analysis** — Exploratory analysis of salaries, skills, regions, and job-market trends.
* 📊 **Interactive Salary Dashboard** — A dynamic dashboard for exploring median salaries by job title, country, and employment type.

---

## 🎯 Objective

The main goal of this project was to develop practical **Excel data analytics skills** while answering important questions about the data science job market.

### Key Objectives

* Analyze salary trends across data-related roles.
* Understand how technical skills influence salary levels.
* Identify the most in-demand technical skills.
* Compare salaries across different geographic regions.
* Explore the relationship between the number of skills and compensation.
* Build an interactive salary dashboard.
* Transform raw job-market data into actionable insights.

---

## 📁 Project Files

| File                      | Description                                     |
| ------------------------- | ----------------------------------------------- |
| `1_Salary_Dashboard.xlsx` | Interactive Excel salary dashboard              |
| `2_Project_Analysis.xlsx` | Detailed data analysis and exploratory workbook |

---

## 📊 Dataset Description

The project uses real-world **2023 Data Science job-market data** containing information about job postings, salaries, locations, skills, and employment types.

| Feature            | Description                            |
| ------------------ | -------------------------------------- |
| 👨‍💼 Job Title    | Data-related job role                  |
| 💰 Annual Salary   | Estimated annual salary                |
| 📍 Job Country     | Country where the job is located       |
| 🛠️ Skills         | Technical skills required for the role |
| 💼 Employment Type | Type/schedule of employment            |
| 🆔 Job ID          | Unique identifier for each job posting |

---

## 🛠️ Technologies & Excel Skills

* 🔍 **Power Query** — Data cleaning and ETL
* 💪 **Power Pivot** — Data modeling
* 📊 **PivotTables** — Data aggregation and analysis
* 📈 **Pivot Charts** — Data visualization
* 🧮 **DAX** — Advanced calculations and measures
* 🧮 **Advanced Excel Formulas** — Dynamic calculations
* ❎ **Data Validation** — Interactive dashboard filters
* 📋 **Data Modeling** — Relationships between tables
* 📉 **Data Visualization** — Charts, maps, and dashboard design
* 🔎 **Exploratory Data Analysis** — Identifying trends and patterns

---

# 🧑‍💻 Project Workflow

## 1️⃣ Data Preparation & ETL

Raw job-market data was imported and prepared using **Power Query**.

### Process

* Imported raw datasets into Excel.
* Cleaned and transformed the data.
* Created separate queries for job information and job skills.
* Prepared the datasets for analysis.
* Loaded the cleaned data into the Excel data model.

This ETL process provided a structured foundation for the analysis.

---

## 2️⃣ Data Modeling

A relational data model was created using **Power Pivot**.

The jobs and skills datasets were connected using the:

```text
job_id
```

This relationship allowed the analysis to combine job-level information with individual technical skills.

---

## 3️⃣ Exploratory Data Analysis

The cleaned dataset was analyzed using:

* PivotTables
* DAX measures
* Pivot Charts
* Excel formulas
* Data visualization

The analysis focused on salaries, skills, job titles, regions, and employment characteristics.

---

# 🔍 Business Questions & Key Insights

## 1️⃣ Do More Skills Lead to Higher Salaries?

### 🔧 Tools Used

* Power Query
* Data Cleaning
* ETL
* PivotTables

The dataset was analyzed to understand the relationship between the number of technical skills required by a role and its median salary.

### 📈 Key Findings

* Roles requiring a broader technical skill set generally offered higher median salaries.
* Senior Data Engineers and Data Scientists showed a strong relationship between skill count and compensation.
* Entry-level and analyst roles generally required fewer technical skills and had lower median salaries.

### 💡 Takeaway

Developing a broader and more relevant technical skill set can improve earning potential in data-related careers.

---

## 2️⃣ How Do Salaries Vary Across Regions?

### 🔧 Tools Used

* Power Pivot
* PivotTables
* DAX
* Data Visualization

A DAX measure was created to calculate median salary:

```DAX
Median Salary :=
MEDIAN(data_jobs_all[salary_year_avg])
```

### 📈 Key Findings

* US-based data professionals consistently showed higher median salaries than many international markets.
* Senior technical positions remained among the highest-paying roles.
* Geographic location has a significant impact on compensation.

### 💡 Takeaway

Location is an important factor when evaluating data-career opportunities and salary expectations.

---

## 3️⃣ Which Technical Skills Are Most In Demand?

### 🔧 Tools Used

* Power Pivot
* Data Modeling
* Relationships
* PivotTables

The analysis identified frequently requested technical skills across data-related job postings.

### 🔥 Most In-Demand Skills

* Python
* SQL
* AWS
* Azure
* Excel

These technologies appeared frequently across a wide range of data-related positions.

### 💡 Takeaway

Developing skills in programming, databases, cloud platforms, and analytical tools can improve employability in the data industry.

---

## 4️⃣ Which Skills Are Associated With Higher Salaries?

### 🔧 Tools Used

* PivotTables
* Pivot Charts
* Data Visualization

A combination chart was created to compare:

* 💰 Median Salary
* 📊 Skill Demand (%)

### 📈 Key Findings

* Python, SQL, and Oracle were among the technical skills associated with higher median salaries.
* General productivity tools such as Word and PowerPoint were associated with comparatively lower salaries.
* Specialized technical skills generally provide stronger earning potential.

### 💡 Takeaway

Investing in programming languages, databases, cloud technologies, and specialized technical skills can create opportunities for higher-paying data careers.

---

# 📊 Interactive Salary Dashboard

The second part of the project transforms the analysis into an **interactive Excel dashboard**.

The dashboard allows users to explore salary information dynamically based on:

* 👨‍💼 Job Title
* 🌍 Country
* 💼 Employment Type

---

## 📌 Salary Comparison by Job Title

An interactive horizontal bar chart displays median salaries across different data-related roles.

### Key Insight

Senior-level and engineering positions generally offer higher median salaries than analyst-oriented positions.

---

## 🌍 Salary Comparison by Country

An interactive world map visualizes median salaries across countries.

### Key Insight

Salary levels vary significantly between countries, highlighting the impact of geographic location on compensation.

---

## 🎛️ Interactive Dashboard Filters

The dashboard uses **Excel Data Validation** to create interactive dropdown filters.

Users can select:

* Job Title
* Country
* Employment Type

The dashboard then dynamically updates the salary analysis based on the selected criteria.

---

## 🧮 Advanced Excel Formulas

Dynamic Excel formulas were used to calculate median salaries based on multiple criteria.

Example:

```excel
=MEDIAN(
IF(
(jobs[job_title_short]=A2)*
(jobs[job_country]=country)*
(ISNUMBER(SEARCH(type,jobs[job_schedule_type])))*
(jobs[salary_year_avg]<>0),
jobs[salary_year_avg]
)
)
```

Additional functions such as `FILTER()` were used to generate dynamic lists and improve dashboard interactivity.

---

# 📈 Dashboard Visualizations

The project includes visualizations designed to communicate salary and job-market insights effectively.

### 📊 Salary by Job Title

Compares median salary across different data-related roles.

### 🌍 Salary by Country

Highlights geographic differences in compensation.

### 📈 Skill Demand vs Salary

Compares the popularity of technical skills with their associated salary levels.

### 📊 Skill Count vs Salary

Explores whether a broader technical skill set is associated with higher compensation.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a0466a2e-25d9-482b-9353-f2a33dda4725" alt="Skill demand vs salary" style="width:90%;max-width:1100px;height:auto;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.08);" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/1d855594-2a23-41f9-aa17-eba2c63017eb" alt="Salary by job title" style="width:90%;max-width:1100px;height:auto;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.08);" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/078a43a6-242c-4339-8930-e1c4d0106ceb" alt="Salary by country map" style="width:90%;max-width:1100px;height:auto;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.08);" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/a86c3cc4-b6b1-41a8-88ad-785956c73439" alt="Skill count vs salary" style="width:90%;max-width:1100px;height:auto;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.08);" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/75cc4cf9-17a1-4377-91a5-f2a9b81a350a" alt="Dashboard overview" style="width:90%;max-width:1400px;height:auto;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.08);" />
</p>

---

# 🧠 Key Learnings

Through this project, I gained practical experience in:

* 🔍 Cleaning and transforming raw datasets using **Power Query**
* 💪 Building relational data models using **Power Pivot**
* 🧮 Creating **DAX measures**
* 📊 Performing exploratory data analysis with **PivotTables**
* 📈 Creating professional **Pivot Charts**
* 🧮 Using advanced Excel formulas
* ❎ Creating interactive filters using **Data Validation**
* 🌍 Building geographic salary visualizations
* 📋 Designing interactive Excel dashboards
* 🔎 Extracting actionable insights from real-world datasets
* 📊 Communicating analytical findings through visualization

---

# 🎯 Conclusion

This project demonstrates that **Microsoft Excel can be used as a powerful end-to-end data analytics platform**, far beyond basic spreadsheet calculations.

By combining **Power Query, Power Pivot, DAX, PivotTables, Pivot Charts, advanced formulas, and interactive dashboard techniques**, I analyzed the 2023 data science job market from multiple perspectives.

The analysis provided insights into:

* 💰 Salary differences
* 🌍 Geographic compensation
* 🛠️ Technical skill demand
* 📈 Skill-to-salary relationships
* 👨‍💼 Job-title salary trends

Building both the analytical workbook and interactive dashboard strengthened my skills in **data preparation, data modeling, exploratory analysis, visualization, and business storytelling**.

---

# 🔌 Example Use Cases

This analysis can be useful for:

* 🎯 Career planning and job selection
* 💰 Understanding salary expectations
* 🛠️ Identifying valuable technical skills
* 🌍 Comparing international job markets
* 📚 Prioritizing skills to learn
* 📊 Supporting salary negotiations
* 👨‍💼 Understanding data-industry hiring trends

---

# 📁 Repository Structure

```text
Data-Jobs-Market-Analysis/
│
├── data/
│   └── data_jobs.csv
│
├── workbooks/
│   ├── 1_Salary_Dashboard.xlsx
│   └── 2_Project_Analysis.xlsx
│
├── visuals/
│   └── dashboard.png
│
├── README.md
│
└── ...
```

---

# 🚀 Getting Started

1. Download or clone this repository.
2. Open `2_Project_Analysis.xlsx` to explore the detailed analysis.
3. Open `1_Salary_Dashboard.xlsx` to interact with the salary dashboard.
4. Use the available filters to explore different job titles, countries, and employment types.
5. Review the PivotTables, charts, and calculations to understand how the insights were generated.

> **Note:** Some Excel features such as Power Query, Power Pivot, DAX, and certain visualizations may work best with the desktop version of Microsoft Excel.

---

# 🧠 Future Improvements

* 🤖 Add machine learning-based salary predictions.
* 📊 Build additional interactive dashboard pages.
* 🌍 Add more detailed geographic analysis.
* 📅 Analyze salary trends across multiple years.
* 💼 Add industry and company-level comparisons.
* 📈 Include salary forecasting.
* 🔄 Automate data refresh using Power Query.
* 🎯 Build a personalized salary benchmark tool based on role, location, and skills.

---

# 🙏 Acknowledgement

This project was completed as part of the **Excel for Data Analytics** course by **Luke Barousse**.

The work, analysis, implementation, and insights presented in this repository represent my own learning and application of the concepts taught throughout the course.

---

## 👩‍💻 Author

Made with ❤️ by **Rakhi Yadav**

### Turning job-market data into career insights 📊💼✨
