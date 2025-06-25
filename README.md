# Employee Turnover Case Study – Salifort Motors

## Project Overview
This project analyzes HR data from Salifort Motors to identify the key drivers of employee attrition and support data-informed retention strategies. Using Python for EDA and modeling, and Tableau for visualization, the analysis highlights satisfaction, workload, salary, and department-level risk.

## Folder Structure
```
employee_turnover_case_study/
├── data/
│   └── employee_turnover_cleaned.csv
│   └── employee_turnover_raw.csv
│   └── notebook.ipynb
├── scripts/
│   └── employee_turnover_model.ipynb
├── visuals/
├── dashboard/
│   └── employee_attrition_dashboard_link.txt
├── employee_turnover_case_study.pdf
├── README.md
```

## Tools & Technologies
- Python (pandas, seaborn, scikit-learn, XGBoost)
- Tableau (dashboard visualization)
- Microsoft Word (case study write-up)

## Business Questions Answered
- What percentage of employees are leaving the company?
- Which departments experience the highest turnover?
- How does satisfaction differ between stayers and leavers?
- Does workload correlate with attrition?
- How does salary level impact turnover?
- Are promoted employees less likely to leave?

## Key Findings
- Overall attrition rate is 24 percent across 14,999 employees.
- Sales and Technical departments account for over 50 percent of turnover.
- Median satisfaction for leavers is 0.44 vs 0.66 for stayers.
- Employees working >250 monthly hours have nearly double the attrition rate.
- Low-salary employees leave at 39 percent; high-salary at just 9 percent.
- Promotions are highly protective: only 2 percent of promoted employees leave.

## Predictive Model
An XGBoost model achieved an AUC of 0.90, identifying satisfaction level, number of projects, average monthly hours, and salary tier as top predictors of attrition risk.

## Recommendations
- Target Sales and Technical departments with engagement programs.
- Cap average monthly hours at 220 to reduce burnout.
- Expand internal promotion pathways.
- Review compensation strategy for low-paid employees.
- Deploy quarterly satisfaction surveys linked to predictive risk scoring.

## Interactive Dashboard
View the live dashboard here:  ![HR_Dashboard](https://github.com/user-attachments/assets/6f6047ed-61c4-4f5b-ab4a-49169c931f96)

(https://public.tableau.com/views/EmployeeAttrition_17508261962710/SalifortMotors-EmployeeAttrition?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Author
Bryce Smith
