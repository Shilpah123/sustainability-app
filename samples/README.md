# Sample Data for Testing

This folder contains sample documents and data to test the AI Sustainability Agent system.

## Sample Files

### 1. Invoice Samples
- `electricity_bill.txt` - Utility electricity bill
- `fuel_receipt.txt` - Gas station fuel receipt
- `hotel_invoice.txt` - Hotel accommodation invoice

### 2. Travel Expenses
- `travel_expenses.csv` - Business travel expense report
- `flight_bookings.csv` - Flight ticket data

### 3. Cloud Infrastructure
- `aws_bill.txt` - AWS cloud computing invoice
- `azure_bill.txt` - Azure cloud services bill

### 4. Test Queries
- `chatbot_queries.txt` - Sample questions to test the AI chatbot

## How to Test

### Testing Document Upload

1. **Start the application:**
   ```bash
   docker-compose up -d
   ```

2. **Access the Upload page:** http://localhost:3000/upload

3. **Upload sample files:**
   - Try uploading `electricity_bill.txt` (will be classified as Scope 2)
   - Upload `fuel_receipt.txt` (will be classified as Scope 1)
   - Upload `travel_expenses.csv` (will be classified as Scope 3)

### Testing Analytics

1. **Go to Analytics page:** http://localhost:3000/analytics

2. **Try these queries:**
   - "Why did emissions increase?"
   - "Which category has the highest emissions?"
   - "Show me trends over time"

### Testing Recommendations

1. **Go to Recommendations page:** http://localhost:3000/recommendations

2. **Click "Generate Recommendations"**

3. **Filter by:**
   - Quick Wins
   - Long-term Strategies

### Testing Scenarios

1. **Go to Scenarios page:** http://localhost:3000/scenarios

2. **Try these scenarios:**
   - "What if 50% of travel becomes virtual?"
   - "What if we switch to renewable energy?"
   - "What if we reduce cloud usage by 30%?"

### Testing Chatbot

1. **Click the chat button** (bottom right)

2. **Ask questions from `chatbot_queries.txt`**

## Expected Results

### Electricity Bill
- **Classification:** Scope 2
- **Category:** Electricity
- **Estimated Emissions:** ~140 kg CO₂e (based on 300 kWh)

### Fuel Receipt
- **Classification:** Scope 1
- **Category:** Fuel
- **Estimated Emissions:** ~92 kg CO₂e (based on 40 liters)

### Travel Expenses
- **Classification:** Scope 3
- **Category:** Business Travel
- **Estimated Emissions:** Varies by distance and mode

### Cloud Bills
- **Classification:** Scope 3
- **Category:** Cloud Computing
- **Estimated Emissions:** Based on compute hours and storage

## Creating Your Own Test Data

### CSV Format
Create a CSV file with these columns:
```csv
Date,Description,Category,Amount,Currency,Quantity,Unit
2024-06-15,Flight to Boston,Travel,450.00,USD,1200,km
```

### Text Format (for OCR testing)
Create a plain text file mimicking an invoice:
```
COMPANY NAME
Invoice #12345
Date: June 15, 2024

Item: Electricity Usage
Quantity: 300 kWh
Amount: $45.00
```

## Notes

- The system uses AI to extract data, so exact formatting isn't critical
- Text files simulate OCR output from PDF documents
- CSV files demonstrate structured data import
- All sample data is fictional for testing purposes
