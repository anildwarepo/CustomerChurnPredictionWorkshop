## Create and run machine learning pipelines using components with the Azure Machine Learning SDK v2

### Prerequisites

* Recommendation is to use AML compute instance to run the notebook.
* The notebook can be run locally but will the following dependencies installed locally:
 
    - python installed - python 3.8+
    - conda installed
    - Azure ML Python [SDK](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-ml-readme?view=azure-python) and [CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?view=azureml-api-2&tabs=public) v2 installed.
    - Install additional dependencies in the conda_env.yml
    
            conda env create -f conda_env.yml

* Clone repo from AML Compute Instance terminal or locally. 
        
        git clone https://github.com/anildwarepo/CustomerChurnPredictionWorkshop.git


### Training using AutoML

Use the automl_amlsdkv2_training.ipynb to kickoff an AutoML training job on AML.


### Scoring using local compute

use the automl_amlsdkv2_score_bestmodel_local.ipynb to run a scoring job on local.



### Scoring using remote compute

use the automl_amlsdkv2_score_bestmodel_compute_cluster.ipynb to run a scoring job on compute cluster.