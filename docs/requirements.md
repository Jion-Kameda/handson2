# Functional Requirements

## Scope
This document defines functional requirements for an HTTP API built on Azure Functions.

## Requirements
1. The system shall provide two HTTP APIs.
2. The APIs shall be callable by entering a URL from a browser.
3. The system shall return the calculation result as a plain-text HTTP response.
4. The first API shall perform multiplication.
5. The second API shall perform division.
6. Both APIs shall accept input values using query string parameters named A and B.

## API Specification
### 1) Multiplication API
- Endpoint: /api/multiply
- Method: GET
- Query Parameters:
  - A: number (required)
  - B: number (required)
- Behavior:
  - Returns A * B
- Success Response:
  - Status: 200 OK
  - Body: calculation result in plain text (example: 12)

### 2) Division API
- Endpoint: /api/divide
- Method: GET
- Query Parameters:
  - A: number (required)
  - B: number (required)
- Behavior:
  - Returns A / B
- Success Response:
  - Status: 200 OK
  - Body: calculation result in plain text (example: 2)

## Input Validation and Error Handling
1. If A or B is missing, the API shall return:
   - Status: 400 Bad Request
   - Body: "A and B are required."
2. If A or B cannot be parsed as a number, the API shall return:
   - Status: 400 Bad Request
   - Body: "A and B must be numeric values."
3. If B is 0 in the division API, the API shall return:
   - Status: 400 Bad Request
   - Body: "B must not be zero."

## Notes
- Number input supports integer and decimal formats.
- This document covers only functional behavior.