# Customer Churn Prediction using Azure Machine Learning Automl with Python SDK V2


This repo guides users to create an Automl job using Components and AML SDK V2. 
You can either the designer or notebooks to create a training and scoring job.


This notebook uses [Telco Customer Churn data from IBM Sample Datasets](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113).




### Pre-requisites
* Azure Machine Learning workspace provisioned.
* Compute Cluster provisioned in the workspace.
* Training Cluster created. Recommend to create training cluster with 3 nodes with each Node have 2 vCPUs. This can reduce the AutoML training time. This notebook takes about 12 minutes to complete the training on a 3 node CPU cluster with Standard_DS11_v2 (2 cores, 14 GB RAM, 28 GB disk). 
* Recommendation is to use AML compute instance to run the notebook.
* The notebook can be run locally but will the following dependencies installed locally:
 
    - python installed - python 3.8+
    - conda installed
    - Azure ML Python [SDK](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-ml-readme?view=azure-python) and [CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?view=azureml-api-2&tabs=public) v2 installed.
    - Install additional dependencies in the conda_env.yml
    
            conda env create -f conda_env.yml

* Clone repo from AML Compute Instance terminal or locally. 
        
        git clone https://github.com/anildwarepo/CustomerChurnPredictionWorkshop.git


* AML workspace can be configured with Private Endpoint with necessary DNS changes as documented [here](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-custom-dns?view=azureml-api-2&tabs=azure-cli). 

* Compute Cluster and Compute intances provisioned. 


There are two ways with which one can accomplish Automl training and scoring in AML. 
1. Automated ML UI
2. Jupyter Notebook or Cli using AML python SDK V2.

- For Automate ML using UI please see [this](Designer.md)

- For notebook based Automl, please see [this](Notebook.md)




