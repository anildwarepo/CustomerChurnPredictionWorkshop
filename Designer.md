### Automl and Scoring with UI

In this section, we will use Automl UI to create a training job and AML Visual Designer to score using the best performaning model created by Automl. 

#### Create a Automl Training Job

Make sure a compute cluster is provisioned. 

##### Please follow the steps to configure and submit an Automl Training Job.
- Navigate to https://ml.azure.com and login with you credentials. 
- Select the workspace and navigate to Automated ML tab. 
![Automl Tab](./assets/automlimage1.png)
- Select New Automated ML job
![Automl1](./assets/automlimage2.png)
- Provide a unique job name For e.g my_unique_name_automl_job
- Select "Create New" under experiment name and provide a unique experiment name and click next. For e.g my_unique_name_experiment.
![Alt text](./assets/automlimage3.png)
- Select Classification as Task type.
![Alt text](./assets/automlimage4.png)
- In the Select dataset, select Create
![Alt text](./assets/automlimage5.png)
- Provide unique name for the Data asset. For e.g my_unique_data_asset_for_automl and select Type as Table(mltable) and click Next
![Alt text](./assets/automlimage6.png)
- Select From local files and click next. 
- Select Datastore Type as Azure Blob Storage and select workspaceblobstore and click next. 
- Click Upload Folder and point to the AutomlTrainingData folder under this repo. 
![Alt text](./assets/automlimage7.png)
- Click Next and Click Create. This should a new Data set in the AML workspace. 

- In the Automl page, select the newly created dataset and click Next.
![Alt text](./assets/automlimage8.png)

- Under Task settings, select Target Column Churn
- Click additional configuration settings and provide details as shown below and click Save.
 ![Alt text](./assets/automlimage9.png)
- Enable early termination. This is to reduce training time if the scores do not improve. 
Click Next. 
![Alt text](./assets/automlimage10.png)
- Under Compute, select compute type as Compute Cluster and select the AML compute cluster that has been provisioned and click Next.
![Alt text](./assets/automlimage11.png)

- Click Submit Training job. The job can around 12 minutes on a 2-core training cluster. Please wait for the job to complete successfully. 
![Alt text](./assets/automlimage12.png)
- Navigate to Job panel in AML workspace to see the status of the training job. 
![Alt text](./assets/automlimage13.png)
- Click on Models tab to view the best performing model and view explainations and other metrics. 
![Alt text](./assets/automlimage14.png)
![Alt text](./assets/automlimage15.png)
- Click on Register Model Tab 
![Alt text](./assets/automlimage16.png)

- Click Next
![Alt text](./assets/automlimage17.png)
- Provide unique model name and version and Click Next. For e.g my_unique_best_performing_model. 
![Alt text](./assets/automlimage18.png)
- Click Register.
![Alt text](./assets/automlimage19.png)

- Once the model is registered, you can find it in the Models Pane in AML. 
![Alt text](./assets/automlimage20.png)


#### Using Visual Designer to Score using the best performing model. 

##### Prerequisites
- Navigate to Components pane in AML. 
![Alt text](./assets/automlimage21.png)
- Click on New Component and select Folder in the Upload Component page. 
![Alt text](./assets/automlimage22.png)
- Click Browse and point to score-component from this repo and upload the contents of the score-component. This folder has code to score the the test data using the best performing model. 
![Alt text](./assets/automlimage23.png)
- Click Next to create the component
![Alt text](./assets/automlimage24.png)

##### Create scoring job using Visual Designer. 

- Navigate to Designer pane in AML and select Custom tab.
![Alt text](./assets/automlimage25.png)
- Create new pipeline using Custom components button
- On the Authoring page, select Data tab and click on the + button to add a new test dataset. 
![Alt text](./assets/automlimage26.png)
- In the Create data assest page, provide a unique Data asset name. For e.g. my_unique_test_dataset.
Select Type as File and click Next.
![Alt text](./assets/automlimage27.png)
- Select From local files, click Next, Select Azure Blob Storage and workspaceblobstore. 
![Alt text](./assets/automlimage28.png)
- Click Upload File and point to the WA_Fn-UseC_-Telco-Customer-Churn_Test.csv file in the telcocustomerchurn folder in the repo. Click Next once the file is uploaded.
- Click Create to create the data set. 
![Alt text](./assets/automlimage29.png)

- Drag and Drop the new created my_unique_test_dataset on the Authoring canvas. 
![Alt text](./assets/automlimage30.png)

- Click on Model Tab and Drag and Drop the my_unique_best_performing_model on to the Authoring Canvas. 
![Alt text](./assets/automlimage31.png)

- Click on the Component Tab and Drag and drop the Score component that was just uploaded. 
![Alt text](./assets/automlimage32.png)

- Connect the Dataset to the input_data port of the Score component and Model to the input_model port of the component. 
![Alt text](./assets/automlimage33.png)

- Click on the Properties icon on the top right corner in the Authoring canvas. 
![Alt text](./assets/automlimage34.png)
![Alt text](./assets/automlimage35.png)
- Expand Output section and provide unique name in the Path Field. For e.g azureml/my_unique_folder_name/
![Alt text](./assets/automlimage36.png)

- Click on Configure & Submit on the top right corner. 
![Alt text](./assets/automlimage37.png)

- Provide new experiment name and job display name and click Next and Next. For e.g. my_unique_designer_experiment.
![Alt text](./assets/automlimage38.png)

- On the Runtime Settings page, select compute cluster and select the provisioned compute cluster. Click Next.
![Alt text](./assets/automlimage39.png)
- Click Submit to create the experiment. Please wait for the Job to complete, by Navigating to the Jobs Page in AML. 
![Alt text](./assets/automlimage40.png)

- Once the Job complete, to view the Scoring results, naviate to the Azure Portal from the AML workspace top right corner. 
![Alt text](./assets/automlimage41.png)
Click on "View all properties in Azure Portal".  This will open the Azure Poral in a new browser tab. 
- In the Azure portal, click on the Storage link in the AML workspace overview panel. 
![Alt text](./assets/automlimage42.png)
![Alt text](./assets/automlimage43.png)

- Navigate to Containers tab.

![Alt text](./assets/automlimage44.png)

- Navigate to the azureml-blobstore-{{some-guid}} folder. Type the folder path in the search box. For e.g azureml/my_unique_folder_name/. This is the name of the folder path provided in the Designer page. 

![Alt text](./assets/automlimage45.png)

- Download the file to review the Churn Prediction Results. 

![Alt text](./assets/automlimage46.png)