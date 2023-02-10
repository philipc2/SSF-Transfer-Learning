import numpy as np

################### Configuration for Data Loading ################################
path = '/glade/scratch/philipc/senior-thesis-data/SSF/data/'
path_save = '/glade/scratch/philipc/SSF/data/'  # need to change to the absolute path to save data_files
absolute_path = '/glade/scratch/philipc/SSF/'  # need to change to the absolute path of the code files
rootpath_cv = '/glade/scratch/philipc/SSF/data/random_cv/'
forecast_rootpath = '/glade/scratch/philipc/SSF/data/forecast/'
param_path = '/glade/scratch/philipc/SSF/data/random_cv/cv_results_test/best_parameter/'

# target variable: 'tmp2m' or 'precip'
target = 'tas_2m'
# target resolution
target_res = 2
# lat range of the target region
target_lat = [25.1, 48.9]
# lon range of the target region
target_lon = [235.7, 292.8]
target_us_all = True
# days to shift for target variable - 14 days ahead of prediction
shift_days = 14
# forecast range - 14 days average or summation
forecast_range = 14
# compute the summation or average over the forecast range
# "mean" for temperature and "sum" for precipitation
operation = 'mean'
# flag to indicate weather to save shifted target
save_target = True

# Set the start date for training
train_start_date = '1990-01-01'
# Set the end date for training set
train_end_date = '2016-12-31'
# Set the start date for testing
test_start_date = '2017-01-01'
# Set the end date for whole dataset
end_date = '2018-12-31'

# spatial temporal covariate variables
covariates_us = ['tas_2m']
# spatial-temporal covariates on land
covariates_global = ['zg_10', 'zg_500', 'psl']
# spatial-temporal covariate over ocean
covariates_sea = ['ts']
pacific_atlantic = True

# lat/lon range for covariates
lat_range_global = [0, 50.0]
lon_range_global = [120, 340]

lat_range_us = [25.1, 48.9]
lon_range_us = [235.7, 292.8]

lat_range_sea = [0, 50]
lon_range_sea = [120, 340]


# spatial variable
# add_spatial = True  # flag to indicate adding spatial features: may not need this flag
spatial_set = ['elevation']  # spatial variables

# temporal variable
# flag to indicate adding temporal features: may not need
add_temporal = False
temporal_set = ['mei', 'nao', 'mjo_phase', 'mjo_amplitude', 'nino3', 'nino4', 'nino3.4', 'nino1+2']  # temporal variable(s)

save_cov = True    # flag to indicate weather to save covariance


# target_lat = 37.75 # 'latitude range for target variable'
# target_lon = 237.75 #'longitude range for target variable'

################### Configuration for Dataset ################################

# preprocessing
rootpath_data = '/glade/scratch/philipc/SSF/data/'
savepath_data ='/glade/scratch/philipc/SSF/data/'

vars = ['ts', 'ts', 'tas_2m', 'zg_10', 'zg_500', 'psl']
locations = ['pacific', 'atlantic', 'us', 'global', 'global', 'global']

num_pcs = 10

# train-validation split
data_target_file = '/glade/scratch/philipc/SSF/data/target_tmp2m_multitask_zscore.h5'
data_cov_file = '/glade/scratch/philipc/SSF/data/covariates_all_pc10.h5'
target_var = 'tmp2m'

# years to create validation sets
val_years = [2016, 2015, 2014, 2013, 2012]

# number of years in the training set (train-val split)
val_train_range = 5

# number of days to include in the validation set
val_range = 28
# frequency to generate validation date
val_freq = '7D'

# train-test split
test_years = [2017, 2018]

# number of years in the training set (train-test split)
test_train_range = 5

# number of days to aggregate in the past: t-n,...,t-1'
past_ndays = 28

# number of years in the past to aggaregate: t-k,...,t year'
past_kyears = 2

# future_mdays = 0

################ Configuration for hyper parameter tuning  ######################
# param_grid for encoder decoder model
param_grid_en_de = {'hidden_dim': [10, 20, 40, 60, 150, 200],
                    'num_layers': [2, 3, 4, 5, 6],
                    'learning_rate': [0.005, 0.001],
                    'threshold': [0.5, 0.6],
                    'num_epochs': [100, 200, 300],
                    'decoder_len': [4, 11, 18],
                    'last_layer': [True, False],
                    'seq_len': [4, 11, 18],
                    'linear_dim': [50, 100, 200],
                    'drop_out': [0.1, 0.2],
                    'ci_dim': 8}
num_random = 30

month_range = list(range(1, 13))
#model_names = ['Lasso', 'FNN', 'XGBoost', 'CNN_FNN', 'CNN_LSTM', 'EncoderFNN_AllSeq_AR_CI',
#               'EncoderFNN_AllSeq_AR', 'EncoderFNN_AllSeq', 'EncoderDecoder', 'EncoderFNN']
model_names = ['EncoderDecoder']
# ['EncoderFNN_AllSeq', 'EncoderDecoder', 'EncoderFNN']
cv_metric = 'cos'
one_day = True
num_rep = 10
