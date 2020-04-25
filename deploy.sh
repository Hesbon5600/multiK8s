#!/bin/bash
echo ">>>>>>>>>>>>>>>>>>>>> login to Docker hub & GCP <<<<<<<<<<<<<<<<"

openssl aes-256-cbc -K $encrypted_9f3b5599b056_key -iv $encrypted_9f3b5599b056_iv -in service-account.json.enc -out service-account.json -d
curl https://sdk.cloud.google.com | bash >/dev/null
source $HOME/google-cloud-sdk/path.bash.inc
gcloud components update kubectl
gcloud auth activate-service-account --key-file service-account.json
gcloud config set project mukti-k8s
gcloud config set compute/zone us-central1-c
gcloud container clusters get-credentials multi-cluster
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_ID" --password-stdin

echo ">>>>>>>>>>>>>>>>>>>>> Build Docker App image <<<<<<<<<<<<<<<<"
# build with the latest tag as well as witthe current commit tag
docker build -t hesbon5600/multi-docker-app-image:latest -t hesbon5600/multi-docker-app-image:$SHA -f ./docker/Dockerfile .

echo " "
echo ">>>>>>>>>>>>>>>>>>>>> Push Docker image <<<<<<<<<<<<<<<<"

docker push hesbon5600/multi-docker-app-image:latest
docker push hesbon5600/multi-docker-app-image:$SHA

echo " "
echo ">>>>>>>>>>>>>>>>>>>>> Apply K8s config <<<<<<<<<<<<<<<<"

# Apply the configurations in the k8s folder
kubectl apply -f k8s

echo " "
echo ">>>>>>>>>>>>>>>>>>>>> Apply Updated K8s config <<<<<<<<<<<<<<<<"
# Apply the latest changes of the image based on the sha
kubectl set image deployments/app-deployment app=hesbon5600/multi-docker-app-image:$SHA
