# receipt-processor


Receipt Processor API

This project implements a receipt processing API using Flask. The API calculates points based on specific rules for receipts submitted by users.

Requirements

Local Setup
	•	Python 3.9 or higher
	•	Flask

Docker Setup
	•	Docker installed on your system.

Installation and Running the Application

Run Using Docker
	1.	Build the Docker image:

docker build -t receipt-processor .


	2.	Run the Docker container:

docker run -p 5000:5000 receipt-processor


	3.	Access the API at:

http://localhost:5000

API Endpoints

1. Process Receipt

Endpoint: /receipts/process
Method: POST
Description: Submits a receipt for processing and returns an ID.

Example Request

POST http://localhost:5000/receipts/process
Content-Type: application/json
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    }
  ],
  "total": "6.49"
}

Example Response

{
  "id": "123e4567-e89b-12d3-a456-426614174000"
}

2. Get Receipt Points

Endpoint: /receipts/{id}/points
Method: GET
Description: Retrieves the points awarded to a receipt by its ID.

Example Request

GET http://localhost:5000/receipts/123e4567-e89b-12d3-a456-426614174000/points

Example Response

{
  "points": 28
}

Postman Collection

A Postman collection is included in this repository to help you test the API.
	1.	Import the Collection:
	•	Open Postman.
	•	Click Import and select the file postman_collection.json.
	2.	Environment Variables:
	•	Use {{use id here}} for the inserting ID generated.

Files Included
	•	receipt.py: The main Flask application.
	•	Dockerfile: Docker setup file for containerizing the application.
	•	api.yml: OpenAPI 3.0 specification.
	•	postman_collection.json: Postman collection for testing the API.

Running Tests
	1.	Import postman_collection.json into Postman.
	2.	Set the environment variable base_url to your API URL (e.g., http://localhost:5000).
	3.	Test the endpoints:
	•	POST /receipts/process: Submit a receipt.
	•	GET /receipts/{id}/points: Retrieve points for a receipt.
