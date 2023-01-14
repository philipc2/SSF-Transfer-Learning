## Sub-Seasonal Climate Forecasting via Machine Learning and Transfer Learning

Code is adapted from He et al. [Sub-Seasonal Climate Forecasting via Machine Learning: Challenges, Analysis, and Advances](https://arxiv.org/abs/2006.07972). Modified to support the CESM2 Forecast and Reforecast dataset and Transfer Learning

## Requirements
The code is compatible with Python 3.6 and the following packages:
- numpy: 1.19.0
- pandas: 0.24.2
- joblib: 0.15.1
- pickle: 4.0
- scipy: 1.5.0
- pytorch: 1.2.0
- sklearn: 0.23.1
- xgboost: 1.0.2
- pytables: 3.5.2

## Getting started
1. Clone the repo
2. Create virtual environments and install the necessary python packages listed above
3. Set up raw datasets
    1. **SSF:** Load raw data from the google drive folder (https://drive.google.com/drive/folders/1qeDOWDULW-F8HnLYPEzWe8tCdtF4xQYT?usp=sharing) and save it to the folder named "data/SSF"
    2. **CESM:** Copy data from {} and save it to the folder name "data/CESM"
4. Revise configutation files to adapt to the required settings
    1. cfg_target.py
    2. cfg_SSF.py
    3. cfg_CESM.py
5. Data loading and preprocessing:
    1. Execute load_data.py to load the subset of data needed in generating forecasts
    2. Execute run_preprocess.py to preprocess covariates and target variable separately
        1. Alternatively, one can execute run_preprocess_map.py to zscore covariates and convert them to squared maps
    3. Execute create_covariates_pca.py to concatenate data
    4. Execute create_datasets.py to create training-validation sets and training-test sets
6. Hyperparameter tuning: execute run_random_search.py to find the best parameter by random search
7. Generate forecasts: execute main_experiments.py to train all the models and generate forecasts on test sets
8. Evaluate forecasts: execute run_evaluation.py to evaluate the forecasting performance on both training and test sets


## Project Structure

### Scripts for generating forecasts
- cfg_target.py: configure file with all parameters from users
- load_data: script for a subset of data required by configure file (cfg_target.py)
- run_preprocess.py: script for data preprocessing
- run_preprocess_map.py: script for preprocessing covariates and converting them to squared maps
- create_covariates_pca.py: script for concatenating PCs from all climate variables (covariates)
- create_datasets.py: script for creating training-validation sets and training-test sets
- run_random_search.py: script for hyperparameter tuning via random search
- main_experiments: script for running experiments for all models on training and test sets
- run_evaluation.py: script for evaluate the performance of forecasting models on training and test sets


### Functions
- data_load: folder contains functions for data loading
- preprocess: folder contains functions for data preprocessing
- hyperparameter_tuning: folder contains functions for random search
- forecasting: folder contains scripts for training forecasting models and evaluating on test sets
- evaluation: folder contains functions for evaluation
- model: collection of models implemented in experiments
- utils:utility functions
