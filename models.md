---
layout: page
title: Models
---

*Work in Progress*

# Models

---
CONTENTS
 
1. [Hazards](#hazards)
2. [Accessibility](#accessibility)
3. [Non-Residential Prices](#nonresidential-prices)
4. [New and Moving Households and Jobs](#new-and-moving-households-and-jobs)
5. [Prices](#prices)
6. [Develop Buildings](#develop-buildings)
7. [Place Households](#place-households)
8. [Place Jobs](place-jobs)
9. [Summaries Validation and Reports](#summaries-validation-and-Reports)

---

## Hazards
### slr_inundate
### slr_remove_dev
### eq_code_buildings 
### earthquake_demolish

## Accessibility
### [neighborhood_vars](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L1098)
### [regional_vars](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L1109)

## Nonresidential Prices
### nrh_simulate

## New and Moving Households and Jobs
### [household_relocation](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L338)
### [households_transition](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L33)
### reconcile_unplaced_households 
update building/unit/hh correspondence
### [jobs_relocation](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L307)
### jobs_transition
### balance_rental_and_ownership_hedonics

## Prices 
### [price_vars](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L1148)

## Develop Buildings
### [scheduled_development_events](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L373)
brings in a list
### preserve_affordable
### lump_sum_accounts
### subsidized_residential_developer_lump_sum_accts
run the subsidized residential acct system
### office_lump_sum_accounts
run the subsidized office acct system
### subsidized_office_developer_lump_sum_accts
### [alt_feasibility](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L555)
### [residential_developer](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L581)
### [developer_reprocess](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L893)
### [retail_developer](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L711)
### [office_developer](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L789)
### [accessory_units](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L169)
### calculate_vmt_fees
### remove_old_units
(for buildings that were removed)      
### initialize_new_units
set up units for new residential buildings
### reconcile_unplaced_households
update building/unit/hh correspondence
### rsh_simulate
simulates the residential sales hedonic for units
### rrh_simulate
simulates the residential rental hedonic for units
### assign_tenure_to_new_units
based on higher of predicted price or rent

## Place Households
### hlcm_owner_lowincome_simulate
household location choice model that allocates low income households to owner-occupied units
### hlcm_renter_lowincome_simulate
household location choice model that allocates low income households to renter-occupied units
### hlcm_owner_simulate
household location choice model that allocates remaining households to owner-occupied units
### hlcm_renter_simulate
household location choice model that allocates remaining households to renter-occupied units
### hlcm_owner_simulate_no_unplaced
### hlcm_owner_lowincome_simulate_no_unplaced
### hlcm_renter_simulate_no_unplaced
### hlcm_renter_lowincome_simulate_no_unplaced
### reconcile_placed_households

## Place Jobs
### [proportional_elcm](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L185)
start with a proportional jobs model
### [elcm_simulate][https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/models.py#L24)
displaced by new dev

## Summaries Validation and Reports
### OFF save_intermediate_tables
saves output for visualization
### topsheet 
write out table related to x
### simulation_validation
### parcel_summary 
write out tables related to x
### building_summary 
write out tables related to x
### diagnostic_output 
write out tables related to x
### geographic_summary 
write out tables related to x
### [travel_model_output](https://github.com/BayAreaMetro/bayarea_urbansim/blob/820554cbabee51725c445b9fd211542db8876c9f/baus/summaries.py#L1467) 
write out tables for inputs to Travel Model 1.5
### OFF travel_model_2_output 
write out tables for inputs to Travel Model 2
### hazards_slr_summary 
write out tables related to sea level rise impacts
### hazards_eq_summary
writes out tables related to earthquake impacts
### slack_report 
sends out information on model completion to Slack
