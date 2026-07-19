# AI Sustainability Agent - Simple Edition

Track and reduce your carbon footprint with **one click** - no Docker, no API keys, no complexity!

## 🚀 Quick Start

### For Anyone on Your Team:

1. **Double-click:** `START.bat`
2. **Wait:** Browser opens automatically
3. **Done!** Start uploading documents

That's literally it! 🎉

## ✨ What It Does

- 📤 **Upload** invoices, bills, receipts (PDF, Excel, CSV, Images)
- 🔍 **Classifies** automatically (Scope 1, 2, 3)
- 📊 **Calculates** carbon emissions (kg CO₂e)
- 📈 **Visualizes** on interactive dashboard
- 💡 **Recommends** reduction strategies
- 🎯 **Models** what-if scenarios
- 💬 **Answers** questions about your emissions

## 📋 What You Need

- ✅ Windows computer
- ✅ Python (install from python.org)
- ✅ 5 minutes

No technical knowledge required!

## 📁 What's Included

```
ESG/
├── START.bat                  ⭐ Double-click to start!
├── simple_app.py              Backend + Frontend in one file
├── simple_launcher.py         Auto-setup launcher
├── requirements_simple.txt    Minimal dependencies
├── .env.simple                Simple configuration
├── agents/
│   └── simple_agent.py        Rule-based agent (no API keys)
├── samples/                   Test data files
│   ├── electricity_bill.txt
│   ├── fuel_receipt.txt
│   ├── travel_expenses.csv
│   └── ... more samples
├── SIMPLE_GUIDE.md           📖 Easy step-by-step guide
└── README.md                  This file
```

## 🎯 Features

### Dashboard
- Total emissions by scope
- Visual charts and graphs
- Recent activities feed
- **Clear All Data** button to reset everything

### Upload Documents
- Drag & drop interface
- Automatic classification
- Instant results

### Analytics
- Ask questions naturally
- Get instant insights
- Understand trends

### Recommendations
- AI-powered suggestions
- Quick wins vs long-term strategies
- Impact estimates

### Scenarios
- "What if 50% of travel becomes virtual?"
- See projected savings
- Compare options

## 📖 Documentation

- **SIMPLE_GUIDE.md** - Complete user guide (start here!)
- **samples/README.md** - About test files
- **samples/test_script.md** - Testing workflow

## 💡 Key Advantages

### Simple
- ✅ One-click start (`START.bat`)
- ✅ No Docker required
- ✅ No API keys needed
- ✅ No complex setup

### Fast
- ✅ Works offline (after setup)
- ✅ Local processing
- ✅ Instant results

### Secure
- ✅ All data stays on your computer
- ✅ No cloud services
- ✅ Complete privacy

### Portable
- ✅ Copy folder to share
- ✅ Runs anywhere
- ✅ Self-contained

## 🧪 Test It Now

1. Double-click `START.bat`
2. When browser opens, go to "Upload" tab
3. Upload a sample file from `samples/` folder
4. See it classify and calculate emissions!

Try:
- `samples/electricity_bill.txt` → Scope 2, ~140 kg CO₂e
- `samples/fuel_receipt.txt` → Scope 1, ~92 kg CO₂e
- `samples/travel_expenses.csv` → Scope 3, ~600 kg CO₂e

## 🔧 How It Works

### No API Keys Required!

Uses **rule-based classification**:
- Keyword matching ("electricity" → Scope 2)
- Regular expressions (extract amounts)
- Statistical analysis (trends)
- Template recommendations

### SQLite Database

- Simple file-based database
- No server required
- Located in `data/db/`

### All-in-One Interface

- Backend + Frontend in one file
- Single HTML page with tabs
- No separate React app needed

## 🤝 Share with Your Team

### Option 1: Copy Folder
```
1. Zip the ESG folder
2. Email to colleagues
3. They unzip and run START.bat
```

### Option 2: Network Drive
```
Put on shared drive → Everyone runs START.bat
```

### Option 3: Email Instructions
```
Subject: Carbon Tracking Tool

To use:
1. Go to: \\shared\ESG\
2. Double-click: START.bat
3. Upload your invoices!
```

## ❓ Troubleshooting

### "Python not found"
Install from: https://www.python.org/downloads/
Make sure to check "Add Python to PATH"

### "Port 8000 in use"
Close the application and try again

### Browser doesn't open
Manually go to: http://localhost:8000

## 📊 Supported Documents

| Type | Examples | Scope |
|------|----------|-------|
| Electricity bills | Utility invoices | Scope 2 |
| Fuel receipts | Gas stations | Scope 1 |
| Travel expenses | Flights, hotels, taxis | Scope 3 |
| Cloud bills | AWS, Azure, GCP | Scope 3 |
| Office supplies | Purchases | Scope 3 |

## 🌱 Make an Impact

Track emissions monthly → Identify hot spots → Implement recommendations → Reduce your carbon footprint!

## 📞 Support

Questions? Check `SIMPLE_GUIDE.md` for detailed instructions.

---

**Ready to make a difference?**

Just double-click `START.bat` and start tracking! 🚀

---

Built with simplicity in mind. No Docker, no complexity, just results.
