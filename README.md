az configure --defaults group=aml-rg workspace=aml-testws location=westus

az ml data create --path ./data --name wa_telco_churn_data --version 0.1 --type mltable


az ml data create --path ./bankmarketing_train.csv --name wa_telco_churn_data --version 0.1 --type mltable

conda env create -n automlscoring --file .\conda_env_v_1_0_0.yml