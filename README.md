# Key-Value Store Demo
This is a simple demo I made to learn Docker. The Flask application can
retrieve values if a GET request is made to `http://localhost:5000` with the
`key` query paramter. It can update the value if a POST request is made with
the query parameters `key` and `value`.

## Demo
1. Try getting the value with the key `something` with `curl "http://localhost:5000/?key=something"`
2. Then update the key `something` with `curl -XPOST "http://localhost:5000/?key=something&value=helloWorld"`
3. Try getting the value again with `curl "http://localhost:5000/?key=something"`
4. The value should be updated now

## Installation
1. Build the Docker image with `docker build stevenhvtran/kv-app:v0.1`
  - View `docker-compose.yml` for image name
2. Run the development server with `docker-compose up -d`
3. View logs with `docker logs <container name>`
4. To spin down the container do `docker-compose down`

## Kubernetes
1. Install `minikube` and `kubectl` on the local environment
2. Reboot the system (helps avoid weird bugs that I encountered)
3. Start the development cluster `minikube start`
4. Enter the `minikube` context `eval $(minikube docker-env)`
  - This allows you to create images that the deployment will be able to see
5. Build the image that the deployment will use
   `docker build -t <image name> .`
6. Deploy according to the config `kubectl apply -f deployment.yaml`
  - This deployment should expose a port with a service, LoadBalancer is a
    possible choice here
7. Check that they pods are running with `kubectl get pods`
8. Navigate to the IP of service that exposes the port with
   `minikube service <service name> --url`
