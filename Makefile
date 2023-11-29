# Deploys a kind cluster, the config is passed in to override default cluster
# Added in this project explicitly to faciliate macOS port mapping issue while using nodeports
# Other OS would work without extra host Mapping except Macos
# https://github.com/kubernetes-sigs/kind/issues/808#issuecomment-525046566
deploy-cluster:
	kind create cluster --name dev --config kind-cluster-config.yaml

delete-cluster:
	kind delete cluster --name dev

# deletes all the services and k8s cluster
delete-all:
	helm delete $(shell helm list -aq)
	kind delete cluster --name dev 

build-image:
	docker build server/. -t todo-server
	docker build client/. -t todo-client

# Load images to local kind registry
upload-image:
	kind load --name dev docker-image todo-server:latest
	kind load --name dev docker-image todo-client:latest

# loads the image and installs the service with overrides
deploy:
	make upload-image
	@helm install todo-app ./chart

undeploy:
	helm delete todo-app

status:
	@kubectl get pods