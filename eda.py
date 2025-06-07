import pandas as pd
import numpy as np
df = pd.read_csv("data/sac_intake_outcome_data_2019-2024.csv")

#print(df[df["us_county_name"].isin(["Fresno County", "Los Angeles County"])])


df_grouped = df.groupby("us_county_name", as_index=False)["stray_at_large_total"].sum()
df_sorted = df_grouped.sort_values(by="stray_at_large_total", ascending=False)
idxx = df_sorted.reset_index(drop=True)
df_sorted["rank"] = idxx.index + 1
print(df_sorted[:15])

county_name = "Fresno County"
result = df_sorted[df_sorted["us_county_name"] == county_name]
print(result)
#print(df.columns)
#result:
# Index(['organization_id', 'location_id', 'org_type', 'location_state_us',
#        'us_county_name', 'us_fips_code', 'completion_status_split',
#        'year_of_record', 'month_of_record', 'species_name', 'gross_intakes',
#        'net_intakes', 'gross_outcomes', 'other_outcomes', 'live_outcomes',
#        'youth_stray_at_large_count', 'adult_stray_at_large_count',
#        'age_unknown_stray_at_large_count', 'stray_at_large_total',
#        'youth_relinquished_by_owner_count',
#        'adult_relinquished_by_owner_count',
#        'age_unknown_relinquished_by_owner_count',
#        'relinquished_by_owner_total', 'youth_other_intakes_count',
#        'adult_other_intakes_count', 'age_unknown_other_intakes_count',
#        'other_intakes_total', 'youth_seized_count', 'adult_seized_count',
#        'age_unknown_seized_count', 'seized_total',
#        'adult_transferred_in_instate', 'youth_transferred_in_instate',
#        'age_unknown_transferred_in_instate', 'transferred_in_instate_total',
#        'youth_transferred_in_outstate', 'adult_transferred_in_outstate',
#        'age_unknown_transferred_in_outstate', 'transferred_in_outstate_total',
#        'youth_transferred_in_international',
#        'adult_transferred_in_international',
#        'age_unknown_transferred_in_international',
#        'transferred_in_international_total',
#        'youth_transferred_in_undesignated',
#        'adult_transferred_in_undesignated',
#        'age_unknown_transferred_in_undesignated',
#        'transferred_in_undesignated_total', 'adult_transferred_in_total_count',
#        'youth_transferred_in_total_count',
#        'age_unknown_transferred_in_total_count', 'transferred_in_total',
#        'youth_adoption_count', 'adult_adoption_count',
#        'age_unknown_adoption_count', 'adoption_total',
#        'youth_returned_to_owner_count', 'adult_returned_to_owner_count',
#        'age_unknown_returned_to_owner_count', 'returned_to_owner_total',
#        'youth_transferred_out_instate', 'adult_transferred_out_instate',
#        'age_unknown_transferred_out_instate', 'transferred_out_instate_total',
#        'youth_transferred_out_outstate', 'adult_transferred_out_outstate',
#        'age_unknown_transferred_out_outstate',
#        'transferred_out_outstate_total', 'youth_transferred_out_international',
#        'adult_transferred_out_international',
#        'age_unknown_transferred_out_international',
#        'transferred_out_international_total',
#        'youth_transferred_out_undesignated',
#        'adult_transferred_out_undesignated',
#        'age_unknown_transferred_out_undesignated',
#        'transferred_out_undesignated_total',
#        'adult_transferred_out_total_count',
#        'youth_transferred_out_total_count',
#        'age_unknown_transferred_out_total_count', 'transferred_out_total',
#        'youth_returned_to_field_count', 'adult_returned_to_field_count',
#        'age_unknown_returned_to_field_count', 'returned_to_field_total',
#        'youth_other_live_outcome_count', 'adult_other_live_outcome_count',
#        'age_unknown_other_live_outcome_count', 'other_live_outcome_total',
#        'youth_died_in_care_count', 'adult_died_in_care_count',
#        'age_unknown_died_in_care_count', 'died_in_care_total',
#        'youth_lost_in_care_count', 'adult_lost_in_care_count',
#        'age_unknown_lost_in_care_count', 'lost_in_care_total',
#        'youth_shelter_euthanasia_count', 'adult_shelter_euthanasia_count',
#        'age_unknown_shelter_euthanasia_count', 'shelter_euthanasia_total'],
#       dtype='object')