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
- Checkout into the `kubernetes` branch to see a more stripped down version of
  the app that uses it
- View the `README.md` file in the branch to see specific instructions
