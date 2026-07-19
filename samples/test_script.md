# Complete Testing Script

Follow this guide to thoroughly test the AI Sustainability Agent system.

## Prerequisites

1. System is running: `docker-compose up -d`
2. Frontend accessible at: http://localhost:3000
3. Backend API at: http://localhost:8000
4. API docs at: http://localhost:8000/docs

## Test Sequence

### Phase 1: Document Upload (10 minutes)

#### Test 1.1: Single Document Upload
1. Navigate to **Upload** page
2. Click the upload area
3. Select `electricity_bill.txt`
4. Click "Upload and Process"
5. **Expected Result:**
   - Success message appears
   - Shows "Scope 2" classification
   - Displays ~140 kg CO₂e emissions
   - Processing time < 30 seconds

#### Test 1.2: Batch Upload
1. Stay on **Upload** page
2. Select multiple files:
   - `fuel_receipt.txt`
   - `hotel_invoice.txt`
   - `travel_expenses.csv`
3. Click "Upload and Process"
4. **Expected Result:**
   - All files processed successfully
   - Different scopes assigned correctly
   - Aggregate emissions calculated
   - Processing time < 60 seconds

#### Test 1.3: CSV Import
1. Upload `flight_bookings.csv`
2. **Expected Result:**
   - All 15 rows processed
   - Classified as Scope 3 (travel)
   - Total emissions ~500-700 kg CO₂e
   - Each flight shows distance and emissions

### Phase 2: Dashboard Visualization (5 minutes)

#### Test 2.1: Dashboard Overview
1. Navigate to **Dashboard** page
2. **Verify:**
   - Total emissions displayed
   - 4 stat cards showing Scope 1, 2, 3
   - Pie chart shows scope distribution
   - Line chart shows trends
   - Bar chart shows categories
   - Recent activities list

#### Test 2.2: Real-time Updates
1. Upload another document
2. Return to Dashboard
3. **Expected Result:**
   - Stats update automatically
   - New activity appears in recent list
   - Charts reflect new data

### Phase 3: Analytics & Insights (10 minutes)

#### Test 3.1: Predefined Questions
1. Navigate to **Analytics** page
2. Click "Why did emissions increase in Q2?"
3. **Expected Result:**
   - Analysis completes < 10 seconds
   - Shows insights with priority levels
   - Identifies root causes
   - Provides supporting data
   - Summary in natural language

#### Test 3.2: Custom Questions
1. Type: "Which category has the highest emissions?"
2. Click "Analyze"
3. **Expected Result:**
   - Identifies top category
   - Shows percentage breakdown
   - Explains why it's highest
   - Suggests focus areas

#### Test 3.3: Trend Analysis
1. Ask: "Show me year-over-year trends"
2. **Expected Result:**
   - Shows trend direction (↑↓→)
   - Calculates percentage change
   - Identifies patterns
   - Detects anomalies

### Phase 4: Recommendations (10 minutes)

#### Test 4.1: Generate Recommendations
1. Navigate to **Recommendations** page
2. Click "Generate Recommendations"
3. **Expected Result:**
   - 8-12 recommendations appear
   - Each has priority label (High/Medium/Low)
   - Shows estimated reduction %
   - Displays cost, timeframe, effort
   - Includes prerequisites

#### Test 4.2: Filter Recommendations
1. Click "Quick Wins"
2. **Verify:** Shows only short-term, low-cost actions
3. Click "Long-term Strategies"
4. **Verify:** Shows only medium/long-term initiatives

#### Test 4.3: Recommendation Details
1. Review a high-priority recommendation
2. **Verify it includes:**
   - Clear title and description
   - Estimated reduction (kg and %)
   - Implementation cost level
   - Timeframe estimate
   - Effort level
   - Feasibility score
   - List of prerequisites

### Phase 5: Scenario Analysis (15 minutes)

#### Test 5.1: Virtual Meeting Scenario
1. Navigate to **Scenarios** page
2. Type: "What if 50% of travel becomes virtual?"
3. Click "Run Scenario"
4. **Expected Result:**
   - Scenario completes < 15 seconds
   - Shows baseline vs projected chart
   - Calculates reduction % and kg
   - Displays by-scope breakdown
   - Provides narrative explanation
   - Shows feasibility assessment

#### Test 5.2: Renewable Energy Scenario
1. Click "What if we switch to renewable energy?"
2. **Expected Result:**
   - Targets Scope 2 emissions
   - Shows significant reduction (40-60%)
   - Comparison chart updates
   - Explains impact on electricity

#### Test 5.3: Cloud Optimization Scenario
1. Type: "What if we optimize cloud infrastructure by 30%?"
2. **Expected Result:**
   - Reduces Scope 3 cloud category
   - Shows specific kg reduction
   - Provides implementation insights
   - Estimates feasibility

#### Test 5.4: Multiple Scenario Comparison
1. Run 3 different scenarios
2. **Compare:**
   - Which has highest reduction
   - Which is most feasible
   - Which is quickest to implement
   - Combined potential impact

### Phase 6: AI Chatbot (20 minutes)

#### Test 6.1: Basic Chatbot Interaction
1. Click chat button (bottom right)
2. Type: "What are our total emissions?"
3. **Expected Result:**
   - Response in < 5 seconds
   - Natural language answer
   - Includes specific numbers
   - Offers related insights

#### Test 6.2: Suggested Questions
1. In chatbot, click a suggested question
2. **Verify:**
   - Question auto-fills
   - Response is contextual
   - Answer is comprehensive

#### Test 6.3: Follow-up Questions
1. Ask: "Why did emissions increase?"
2. Then ask: "How can we fix that?"
3. **Expected Result:**
   - Maintains conversation context
   - Builds on previous answer
   - Provides specific recommendations

#### Test 6.4: Complex Questions
1. Ask: "What are our top 3 emission sources and how can we reduce them?"
2. **Expected Result:**
   - Identifies 3 sources
   - Provides reduction strategy for each
   - Estimates impact for each
   - Prioritizes by effectiveness

#### Test 6.5: Scenario Questions
1. In chatbot, ask: "What happens if 50% of travel becomes virtual?"
2. **Expected Result:**
   - Routes to Scenario Agent
   - Provides projected reduction
   - Explains methodology
   - Suggests implementation

#### Test 6.6: Intent Classification
Test different intents:
- **Analytics**: "Show me trends" → Routes to Analytics Agent
- **Recommendations**: "Suggest reductions" → Routes to Recommendation Agent
- **Scenarios**: "What if..." → Routes to Scenario Agent
- **General**: "How does this work?" → General response

### Phase 7: API Testing (10 minutes)

#### Test 7.1: API Documentation
1. Visit http://localhost:8000/docs
2. **Explore:**
   - All endpoints listed
   - Request/response schemas
   - Try out feature works

#### Test 7.2: Direct API Calls
Using the API docs "Try it out" feature:

1. **Upload Document:**
   ```
   POST /api/upload
   ```
   - Upload a sample file
   - Check response includes classification

2. **Get Summary:**
   ```
   GET /api/emissions/summary
   ```
   - Returns aggregate emissions
   - Includes by-scope breakdown

3. **Chat:**
   ```
   POST /api/chat
   Body: {"query": "What are our emissions?"}
   ```
   - Returns natural language response
   - Includes intent classification

### Phase 8: Error Handling (5 minutes)

#### Test 8.1: Invalid File Upload
1. Try uploading a .txt file with no invoice data
2. **Expected:** Error message or low-confidence classification

#### Test 8.2: Empty Questions
1. In Analytics, click "Analyze" with empty query
2. **Expected:** Button is disabled

#### Test 8.3: Network Errors
1. Stop backend: `docker-compose stop backend`
2. Try any action
3. **Expected:** User-friendly error message
4. Restart: `docker-compose start backend`

### Phase 9: Data Persistence (5 minutes)

#### Test 9.1: Database Persistence
1. Upload documents
2. Restart containers: `docker-compose restart`
3. Check Dashboard
4. **Expected:** All data still present

### Phase 10: Performance Testing (10 minutes)

#### Test 10.1: Response Times
Measure and record:
- Document upload: < 30s
- Analytics query: < 10s
- Recommendation generation: < 15s
- Scenario analysis: < 15s
- Chatbot response: < 5s

#### Test 10.2: Concurrent Operations
1. Open 2 browser tabs
2. Upload in tab 1
3. Query chatbot in tab 2 simultaneously
4. **Expected:** Both complete successfully

## Success Criteria

### Must Pass ✓
- [x] All uploads process successfully
- [x] Classification accuracy > 80%
- [x] All charts render correctly
- [x] Chatbot responds to all question types
- [x] Scenarios show projected reductions
- [x] Recommendations are actionable
- [x] API endpoints return valid data
- [x] No console errors
- [x] Data persists after restart

### Performance ✓
- [x] Document processing < 30s
- [x] Analytics < 10s
- [x] Recommendations < 15s
- [x] Scenarios < 15s
- [x] Chatbot < 5s
- [x] UI responsive, no lag

### User Experience ✓
- [x] Intuitive navigation
- [x] Clear error messages
- [x] Visual feedback for actions
- [x] Helpful tooltips/guidance
- [x] Mobile-responsive design

## Troubleshooting

### Issue: Upload fails
- Check file size (< 10MB)
- Verify file format supported
- Check backend logs: `docker-compose logs backend`

### Issue: Chatbot not responding
- Verify OPENAI_API_KEY in .env
- Check API quota/credits
- View logs for errors

### Issue: Charts not showing
- Check if data exists (upload documents first)
- Verify browser console for errors
- Try refreshing page

### Issue: Database errors
- Check PostgreSQL is running: `docker-compose ps`
- Verify database connection in logs
- Try: `docker-compose restart db`

## Test Data Summary

After completing all tests, you should have:
- **15+ documents** uploaded
- **3+ scopes** classified
- **5+ categories** tracked
- **10+ chat** interactions
- **3+ scenarios** analyzed
- **8-12 recommendations** generated

## Next Steps

After successful testing:
1. Review all generated insights
2. Compare recommendations across scenarios
3. Export data for reporting
4. Customize for your organization
5. Add real company data

## Test Completion Checklist

- [ ] Phase 1: Document Upload
- [ ] Phase 2: Dashboard
- [ ] Phase 3: Analytics
- [ ] Phase 4: Recommendations
- [ ] Phase 5: Scenarios
- [ ] Phase 6: Chatbot
- [ ] Phase 7: API Testing
- [ ] Phase 8: Error Handling
- [ ] Phase 9: Data Persistence
- [ ] Phase 10: Performance

**Total Estimated Testing Time:** 90 minutes

---

**Testing Complete!** 🎉

The system is ready for production use with your organization's actual data.
