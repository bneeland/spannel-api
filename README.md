Spannel is structured in Docker containers. One service for the API and one service for the web app interface.

Steps to run spannel-api locally:
1. Clone this repository
2. Navigate to `spannel-api` directory (where `Dockerfile` is located)
3. Run `docker compose up`
4. Go to `http://localhost:8000` in a browser

The web app runs on port `8000` and the API runs on port `80001`.
