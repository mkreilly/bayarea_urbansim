---
layout: page
title: Models
---

*Work in Progress*

# Models

---
CONTENTS
 
1. [Introdution](#introduction)
2. [Approach](#approach)
3. [Application Types](#application)
4. [Model System](#model-system)
5. [More Information](#more-information)
6. [Model Schematic](#model-schematic)

---

slr_inundate floods parcels impacted by sea level rise
slr_remove_dev removes buildings on parcels impacted by sea level rise
eq_code_buildings 
earthquake_demolish removes buildings
neighborhood_vars    # street network accessibility
regional_vars        # road network accessibility
nrh_simulate         # non-residential rent hedonic
household_relocation
households_transition
reconcile_unplaced_households update building/unit/hh correspondence
jobs_relocation
jobs_transition
balance_rental_and_ownership_hedonics
price_vars
scheduled_development_events brings in a list
preserve_affordable
lump_sum_accounts
subsidized_residential_developer_lump_sum_accts # run the subsidized residential acct system
office_lump_sum_accounts # run the subsidized office acct system
subsidized_office_developer_lump_sum_accts
alt_feasibility
residential_developer
developer_reprocess
retail_developer
office_developer
accessory_units
calculate_vmt_fees
remove_old_units # (for buildings that were removed)      
initialize_new_units # set up units for new residential buildings
reconcile_unplaced_households # update building/unit/hh correspondence
rsh_simulate simulates the residential sales hedonic for units
rrh_simulate simulates the residential rental hedonic for units
assign_tenure_to_new_units based on higher of predicted price or rent
hlcm_owner_lowincome_simulate household location choice model that allocates low income households to owner-occupied units
hlcm_renter_lowincome_simulate household location choice model that allocates low income households to renter-occupied units
hlcm_owner_simulate household location choice model that allocates remaining households to owner-occupied units
hlcm_renter_simulate household location choice model that allocates remaining households to renter-occupied units
hlcm_owner_simulate_no_unplaced
hlcm_owner_lowincome_simulate_no_unplaced
hlcm_renter_simulate_no_unplaced
hlcm_renter_lowincome_simulate_no_unplaced
reconcile_placed_households
proportional_elcm        # start with a proportional jobs model
elcm_simulate  # displaced by new dev
OFF save_intermediate_tables # saves output for visualization
topsheet write out table related to x
simulation_validation
parcel_summary write out tables related to x
building_summary write out tables related to x
diagnostic_output write out tables related to x
geographic_summary write out tables related to x
travel_model_output write out tables for inputs to Travel Model 1.5
OFF travel_model_2_output write out tables for inputs to Travel Model 2
hazards_slr_summary write out tables related to sea level rise impacts
hazards_eq_summary writes out tables related to earthquake impacts
slack_report sends out information on model completion to Slack
