---
layout: page
title: Output
---

*Work in Progress*

# Output Files

---
CONTENTS

1. [Core Files](#core-files)
2. [Travel Model Inputs](#travel-model-inputs)
3. [Additional Files](#additional-files) 

---

Each Bay Area UrbanSim run (r#) produces output files. Some are only output at the start and/or finish of the run, but most are produced every in each 5th year of the run (yr). 

## Core Files
* run[r#].log shows livetime run progress which includes info on scenario numbers, inputs, model execution, and performance
* run[r#]\_configuration.log
* run[r#]\_topsheet\_[yr].csv provides basic info to understand the overall nature of a run. For each year it lists the number of householdd, whether or not all agents are placed in buildings, basic stats on the locations of growth and current totals, and jobs-housing balance.
* run[r#]\_superdistrict_summaries\_[yr].csv contain a summary of select variables at the Super District level (n=33)
* run[r#]\_juris_summaries\_[yr].csv contain a summary of select variables at the juridictional level (n=108)
* run[r#]\_taz_summaries\_[yr].csv contain a summary of select variables at the Travel Analysis Zone level (n=1454)
* run[r#]\_baseyear\_pda_summaries\_2010.csv contain a summary at the PDA level for the START of 2010 (the other 2020 summary occurs at the end of the year 2010 and so contains one year of model forecast)
* run[r#]\_county_growth_summaries.csv
* run[r#]\_county_summaries\_[yr].csv
* run[r#]\_parcel_data\_[yr].csv
* run[r#]\_parcel_data_diff\_[yr].csv
* run[r#]\_parcel_output\_[yr].csv
* run[r#]\_regional_marginals\_[yr].csv
* run[r#]\_simulation_output.csv
* run[r#]\_taz_logsums\_[yr].csv

## Travel Model Inputs

## Additional Files
* run[r#]\_acctlog\_[policy_name]\_[final_yr].csv
* run[r#]\_building_data\_[yr].csv
* run[r#]\_DIS_growth_summaries.csv provides total growth of households, employment, etc in each displacement zone/jurisdiction category
* run[r#]\_dropped_buildings.csv ????
* run[r#]\_GG_growth_saummaries.csv provides total growth of households, employment, etc in each GG/jurisdiction category
* run[r#]\_HRA_growth_summaries.csv provides total growth of households, employment, etc in each HRA/jurisdiction category
* run[r#]\_traDIS_growth_sumaries.csv provides total growth of households, employment, etc in each TRA/HRA/jurisdiction category
* run[r#]\_tra_growth_summaries.csv provides total growth of households, employment, etc in each TRA/jurisdiction category
* run[r#]\_juris_growth_summaries\_[yr].csv
* run[r#]\_superdistrict_growth_summaries.csv
* run[r#]\_taz_growth_summaries.csv
* run[r#]\_hazards_slr\_[yr].csv
* run[r#]\_hazards_slr_buildings\_[yr].csv
* run[r#]\_parcel_logsums\_[yr].csv
* run[r#]\_urban_footprint_summary\_[yr].csv provides the total number of units and nonres sqft that is in various greenfield-related zones in that year

