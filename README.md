Planday Data Analyst Task
This readme file will add some context to my thoughts and the decisions taken when completing this task. I have divided my thoughts and ideas into each task for an easily readable overview:

Task 1:
For the first task concerning exploring and cleaning the dataset with Python, I have chosen to perform this in a Jupyter Notebook. I have pulled this into this git repository, and you can find this file under: Plandaytask.py
While Tableau excels at visual analytics, it has limited capabilities when it comes to detailed data cleaning and preprocessing. 
Therefore, Python was the preferred choice for this step, as it allowed for:
1. Initial exploration of the dataset (data types, missing values, duplicates)
2. Cleaning and standardizing column formats
3. Deriving new columns such as WEEK_FROM_START and Converted (Numeric) for later use in Tableau
4. Performing simple sanity checks before exporting a cleaned dataset

This workflow ensured that the dataset was well-prepared before moving into Tableau for visual analysis.

Task 2:
For task 2 of running a descriptive analysis and creating visualizations for the "Activation product team", I have chosen to import the cleaned dataset into Tableau. 
The dataset was imported to explore trends, behaviors, and insights that could help the team understand how trialists engage with the product and what may drive conversions.
I have uploaded this workbook to my git repository, and this can easily be inserted into Tableau to view each individual worksheet, the grouping, the filters and a combined dashboard that presents all key insights in one simple view. You can find this file under: Plandaytask.twbx

The key findings from this task include:
- The overall conversion rate among trialists is ~21%.
- Trialists who used “Absence Management” or “Scheduling & Shifts” features had the highest conversion rates, so future feature improvements and onboarding should focus heavily on this. 
- The highest conversion rate is in the first week of started Trial, so getting the Trialists up and running in this week, and making sure that they make use of the abovementioned features, will most likely increase the conversion rate further. 

Task 3:
To make this type of analysis more precise and predictive, gaining access to the following data would be highly valuable:

- User-level activity logs: The current dataset is aggregated at the organization level. User-level data would allow for group level analysis and identification of team-wide engagement patterns.
- Organization metadata: Knowing the industry, size, and location of each organization would enable segmentation analysis and reveal patterns across customer types.
- Onboarding touchpoints: Data on emails sent, calls made, or help center usage would help evaluate which onboarding interventions correlate with successful conversions.
- Feedback or satisfaction metrics: Post-trial feedback or NPS could be used to explain edge cases with no conversion and enrich behavioral interpretation.

