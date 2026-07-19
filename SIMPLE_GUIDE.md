# Super Simple Guide - Anyone Can Use!

## What You Need

✅ Windows computer
✅ Internet connection (just for initial download)
✅ 5 minutes

That's it! No technical knowledge needed.

## Step 1: Install Python (One Time Only)

**Only if you don't have Python:**

1. Go to: https://www.python.org/downloads/
2. Click the big yellow "Download Python" button
3. Run the installer
4. **IMPORTANT:** Check the box "Add Python to PATH"
5. Click "Install Now"

**How to check if you have Python:**
- Press Windows Key + R
- Type: `cmd`
- Type: `python --version`
- If you see a number like "Python 3.11.x", you're good!

## Step 2: Start the Application

1. **Navigate to the folder:**
   ```
   C:\data\02-cyberdome\tmsecdom\ESG
   ```

2. **Double-click:** `START.bat`

3. **Wait a moment...** The first time takes a few minutes to set up.

4. **Your browser opens automatically!** 🎉

That's it! The application is running.

## How to Use

### Upload Your First Document

1. Click **"Upload"** tab
2. Drag and drop a file (or click to browse)
   - Try: `samples/electricity_bill.txt`
3. Wait a few seconds
4. See the results!

### View Your Dashboard

1. Click **"Dashboard"** tab
2. See your total emissions
3. View breakdown by Scope 1, 2, 3
4. Check recent uploads

**Need to start fresh?** Click the red **"Clear All Data"** button to delete everything and reset to zero.

### Ask Questions

1. Click **"Analytics"** tab
2. Type: "What are my total emissions?"
3. Press Enter
4. Get instant answer

### Get Recommendations

1. Click **"Recommendations"** tab
2. Click **"Generate Recommendations"**
3. See actionable strategies
4. Review impact estimates

### Try What-If Scenarios

1. Click **"Scenarios"** tab
2. Type: "What if 50% of travel becomes virtual?"
3. Click **"Run Scenario"**
4. See projected savings

## What Files Can You Upload?

✅ **Electricity bills** (PDF or text)
✅ **Fuel receipts** (PDF, text, or images)
✅ **Travel expenses** (Excel or CSV)
✅ **Hotel invoices** (PDF or text)
✅ **Cloud bills** (AWS, Azure - PDF or text)
✅ **Office supply receipts**
✅ **Any invoice or receipt**

The system automatically:
- Reads the document (OCR for images/PDFs)
- Finds the important information
- Classifies it (Scope 1, 2, or 3)
- Calculates CO₂ emissions
- Stores it in your database

## Example Workflow

### Week 1: Get Started
1. Start the application (`START.bat`)
2. Upload 5-10 sample files from `samples` folder
3. Check the Dashboard
4. Understand your baseline

### Week 2: Analyze
1. Upload your real invoices and bills
2. Ask questions in Analytics
3. Generate recommendations
4. Identify quick wins

### Week 3: Plan
1. Run different scenarios
2. Compare options
3. Pick best strategies
4. Create action plan

### Week 4: Track
1. Upload new monthly data
2. Monitor progress
3. Adjust strategies
4. Celebrate reductions!

## Troubleshooting

### Problem: "Python is not installed"
**Solution:** Install Python from python.org (see Step 1)

### Problem: "Port 8000 already in use"
**Solution:** 
1. Close the application (Ctrl+C in the black window)
2. Wait 10 seconds
3. Try again

### Problem: Browser doesn't open automatically
**Solution:** Manually open browser and go to: http://localhost:8000

### Problem: "Error installing dependencies"
**Solution:**
1. Close the application
2. Delete the `venv` folder
3. Run `START.bat` again

### Problem: Can't find `START.bat`
**Solution:** Make sure you're in the right folder:
```
C:\data\02-cyberdome\tmsecdom\ESG
```

## How to Stop the Application

1. Click on the black window (console)
2. Press `Ctrl + C`
3. Close the window

Or simply close the console window.

## Data Storage

All your data is stored locally on your computer in:
```
C:\data\02-cyberdome\tmsecdom\ESG\data\
```

- `data/uploads/` - Your uploaded files
- `data/db/sustainability.db` - Your emissions database

**No data leaves your computer!** Everything is private and secure.

## Tips for Best Results

### 📄 Document Quality
- Clear, readable text works best
- Scanned documents should be high quality
- Excel/CSV files are fastest to process

### 📊 Accurate Tracking
- Upload all invoices monthly
- Include dates on documents
- Keep files organized

### 🎯 Emission Reduction
- Focus on high-impact areas first
- Implement quick wins immediately
- Track progress monthly
- Celebrate improvements!

## Sample Files to Try

In the `samples` folder, you'll find:

| File | What It Shows | Expected Result |
|------|---------------|-----------------|
| `electricity_bill.txt` | Utility bill | Scope 2, ~140 kg CO₂e |
| `fuel_receipt.txt` | Gas station | Scope 1, ~92 kg CO₂e |
| `travel_expenses.csv` | Business travel | Scope 3, ~600 kg CO₂e |
| `aws_bill.txt` | Cloud services | Scope 3, ~23 kg CO₂e |

Try uploading these to see how the system works!

## Understanding Results

### Emission Scopes

**Scope 1 (Direct)** 🚗
- Company vehicles
- Fuel consumption
- On-site generators

**Scope 2 (Energy)** ⚡
- Electricity bills
- Heating and cooling
- Purchased energy

**Scope 3 (Indirect)** ✈️
- Business travel
- Cloud computing
- Supply chain
- Employee commuting

### CO₂e Explained

**CO₂e = Carbon Dioxide Equivalent**

This is a standard way to measure all greenhouse gases.

Example:
- 1,000 kg CO₂e = 1 tonne
- Average car: ~4.6 tonnes/year
- Average person: ~16 tonnes/year (USA)

## Sharing with Your Team

### For Team Members:
1. Copy the `ESG` folder to their computer
2. They run `START.bat`
3. Everyone tracks their own department

### For Managers:
1. Team members upload their data
2. Export summaries monthly
3. Track organization-wide progress
4. Share recommendations

## Getting Help

### Check the Documentation
- `README.md` - Overview
- `GETTING_STARTED.md` - Detailed guide
- `NO_API_KEYS_MODE.md` - Technical details

### Common Questions

**Q: Is this free?**
A: Yes! No subscriptions, no API costs.

**Q: Do I need internet?**
A: Only for initial setup. After that, works offline.

**Q: Is my data safe?**
A: Yes! Everything stays on your computer.

**Q: Can I customize it?**
A: Yes! The code is open and editable.

**Q: What if I close the browser?**
A: Just go to http://localhost:8000 to reopen it.

**Q: How do I share data with colleagues?**
A: Copy the `data` folder or export CSV from the interface.

## You're Ready! 🎉

Just double-click `START.bat` and you're off!

The application will:
✅ Set itself up automatically
✅ Open in your browser
✅ Guide you through everything
✅ Track your carbon footprint
✅ Help you reduce emissions

**No technical knowledge required!**

---

Need help? Check the other guides in this folder or ask your IT team for assistance.

Start making a difference today! 🌱
