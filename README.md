## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/receipt-processor-challenge.git
   cd receipt-processor-challenge
   ```

2.create and activate a venv
```bash
    python3 -m venv venv
    source venv/bin/activate
```

3. install dependencies:
   ```bash
    pip install -r requirements.txt
   ```
5. run flask app:
```bash
  python app.py
```

Docker Setup
Build the Docker image:
```bash
docker build -t receipt-service .
```

Run the Docker container:
docker run -p 5000:5000 receipt-service
Access the application at http://localhost:5000.
