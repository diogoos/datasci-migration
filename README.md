# Analysis of Interstate Migration Patterns In The U.S.
Migration Project for Pathways in Data Science course @ UChicago

## Project Files

| **Notebook**              | **Description**                                                                     |
|---------------------------|-------------------------------------------------------------------------------------|
| [create_dataframe.ipynb](create_dataframe.ipynb)    | Combines all the datasets we used into a single DataFrame; creates [full_df_testing.csv](full_df_testing.csv) |
| [state-testing.ipynb](state-testing.ipynb)       | Graphs the inflow and outflow migration patterns for each state                     |
| [predictive_modeling.ipynb](predictive_modeling.ipynb) | Produces and tests the quadratic and multilinear regression models                  |
| [polynomial_regression.py](polynomial_regression.py)  | Auxiliary function to fit and graph a polynomial curve for the given data                               |



## Dataset files
| **Dataset**                           | **Description**                                                     |
|---------------------------------------|---------------------------------------------------------------------|
| HPI_PO_state.xls                      | Housing price indices by state and year, from FHFA                  |
| Migration_Flows_from_2010_to_2019.csv | Migration inflow and outflow patterns from US Census                |
| SAGDP2N__ALL_AREAS_1997_2020.csv      | GDP information by state and year, from Bureau Of Economic Analysis |
| states_all.csv                        | Education data for each state, from NCES                            |
