# Deploy


cd scoring-pipeline
az ml online-endpoint create --file endpoint.yml -g aml-rg --workspace-name aml-testws
az ml online-deployment create --file deployment.yml -g aml-rg --workspace-name aml-testws