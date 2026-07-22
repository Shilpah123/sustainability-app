"""
Simple All-in-One Application
Backend + Frontend in one file - no complex setup
"""
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, List
import shutil
from pathlib import Path
from datetime import datetime
import sqlite3
import json

# Import simple agent
import sys
sys.path.append(str(Path(__file__).parent / "agents"))
from simple_agent import SimpleAgent

# Initialize FastAPI
app = FastAPI(title="AI Sustainability Agent")

# Initialize simple agent
agent = SimpleAgent()

# Ensure directories exist
Path("data/uploads").mkdir(parents=True, exist_ok=True)
Path("data/db").mkdir(parents=True, exist_ok=True)

# Initialize SQLite database
DB_PATH = "data/db/sustainability.db"

def init_db():
    """Initialize simple SQLite database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create emissions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            upload_date TEXT,
            scope TEXT,
            category TEXT,
            emissions_kg REAL,
            confidence REAL,
            data TEXT
        )
    """)
    
    conn.commit()
    conn.close()

init_db()

# Pydantic models
class ChatRequest(BaseModel):
    query: str

class ScenarioRequest(BaseModel):
    scenario_query: str

# HTML Template (embedded frontend)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Sustainability Agent</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: #f5f7fa;
            padding: 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 12px;
            margin-bottom: 30px;
            text-align: center;
        }
        .header h1 { font-size: 2em; margin-bottom: 10px; }
        .header p { opacity: 0.9; }
        
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            background: white;
            padding: 10px;
            border-radius: 12px;
        }
        .tab {
            padding: 12px 24px;
            border: none;
            background: transparent;
            cursor: pointer;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s;
        }
        .tab:hover { background: #f0f0f0; }
        .tab.active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        
        .card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .card h2 { margin-bottom: 16px; color: #333; }
        
        .upload-area {
            border: 2px dashed #667eea;
            border-radius: 12px;
            padding: 40px;
            text-align: center;
            background: #f8f9ff;
            cursor: pointer;
            transition: all 0.3s;
        }
        .upload-area:hover { background: #f0f2ff; }
        .upload-area input { display: none; }
        
        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .btn-primary:hover { transform: translateY(-2px); }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .stat-value {
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin: 10px 0;
        }
        .stat-label {
            color: #666;
            font-size: 0.9em;
            text-transform: uppercase;
        }
        
        .results {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
        }
        
        .success {
            background: #d4edda;
            color: #155724;
            padding: 12px;
            border-radius: 8px;
            margin: 10px 0;
        }
        
        .error {
            background: #f8d7da;
            color: #721c24;
            padding: 12px;
            border-radius: 8px;
            margin: 10px 0;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
        
        input[type="text"], textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 1em;
            margin: 10px 0;
        }
        
        .recommendation {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin: 10px 0;
            border-left: 4px solid #667eea;
        }
        .recommendation h3 { color: #667eea; margin-bottom: 10px; }
        .recommendation .impact {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
            margin: 5px 5px 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌱 AI Sustainability Agent</h1>
            <p>Track and reduce your carbon footprint - Simple, Fast, No Setup Required</p>
        </div>
        
        <div class="tabs">
            <button class="tab active" onclick="showTab('dashboard')">Dashboard</button>
            <button class="tab" onclick="showTab('upload')">Upload</button>
            <button class="tab" onclick="showTab('analytics')">Analytics</button>
            <button class="tab" onclick="showTab('recommendations')">Recommendations</button>
            <button class="tab" onclick="showTab('scenarios')">Scenarios</button>
        </div>
        
        <!-- Dashboard Tab -->
        <div id="dashboard" class="tab-content active">
            <div class="card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                    <h2>Emissions Overview</h2>
                    <button class="btn btn-secondary" onclick="clearAllData()" style="background: #dc3545; color: white;">
                        🗑️ Clear All Data
                    </button>
                </div>
                <div class="stats-grid" id="stats-grid">
                    <div class="stat-card">
                        <div class="stat-label">Total Emissions</div>
                        <div class="stat-value" id="total-emissions">-</div>
                        <div class="stat-label">kg CO₂e</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Scope 1</div>
                        <div class="stat-value" id="scope1">-</div>
                        <div class="stat-label">kg CO₂e</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Scope 2</div>
                        <div class="stat-value" id="scope2">-</div>
                        <div class="stat-label">kg CO₂e</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Scope 3</div>
                        <div class="stat-value" id="scope3">-</div>
                        <div class="stat-label">kg CO₂e</div>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2>Recent Uploads</h2>
                <div id="recent-uploads">Loading...</div>
            </div>
        </div>
        
        <!-- Upload Tab -->
        <div id="upload" class="tab-content">
            <div class="card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h2>Upload Documents</h2>
                    <button class="btn btn-secondary" onclick="document.getElementById('upload-results').innerHTML=''" style="font-size: 0.9em;">
                        Clear Results
                    </button>
                </div>
                <p style="color: #666; margin-bottom: 20px;">
                    Upload invoices, bills, receipts, or expense reports (PDF, Excel, CSV, Images)
                </p>
                <div class="upload-area" onclick="document.getElementById('file-input').click()">
                    <input type="file" id="file-input" multiple onchange="handleUpload(event)">
                    <div style="font-size: 3em; margin-bottom: 10px;">📤</div>
                    <div style="font-size: 1.2em; margin-bottom: 10px;">Click to select files</div>
                    <div style="color: #666;">Supports: PDF, Excel, CSV, JPG, PNG</div>
                </div>
                <div id="upload-results"></div>
            </div>
        </div>
        
        <!-- Analytics Tab -->
        <div id="analytics" class="tab-content">
            <div class="card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h2>Ask Questions</h2>
                    <button class="btn btn-secondary" onclick="document.getElementById('analytics-results').innerHTML=''; document.getElementById('analytics-query').value=''" style="font-size: 0.9em;">
                        Clear
                    </button>
                </div>
                <input type="text" id="analytics-query" placeholder="e.g., Why did emissions increase?" onkeypress="if(event.key==='Enter') analyzeQuery()">
                <button class="btn btn-primary" onclick="analyzeQuery()">Analyze</button>
                <div id="analytics-results"></div>
            </div>
        </div>
        
        <!-- Recommendations Tab -->
        <div id="recommendations" class="tab-content">
            <div class="card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h2>Get Recommendations</h2>
                    <button class="btn btn-secondary" onclick="document.getElementById('recommendations-results').innerHTML=''" style="font-size: 0.9em;">
                        Clear
                    </button>
                </div>
                <button class="btn btn-primary" onclick="getRecommendations()">Generate Recommendations</button>
                <div id="recommendations-results"></div>
            </div>
        </div>
        
        <!-- Scenarios Tab -->
        <div id="scenarios" class="tab-content">
            <div class="card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h2>What-If Scenarios</h2>
                    <button class="btn btn-secondary" onclick="document.getElementById('scenario-results').innerHTML=''; document.getElementById('scenario-query').value=''" style="font-size: 0.9em;">
                        Clear
                    </button>
                </div>
                <input type="text" id="scenario-query" placeholder="e.g., What if 50% of travel becomes virtual?" onkeypress="if(event.key==='Enter') runScenario()">
                <button class="btn btn-primary" onclick="runScenario()">Run Scenario</button>
                <div id="scenario-results"></div>
            </div>
        </div>
    </div>

    <script>
        // Tab switching
        function showTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab').forEach(el => el.classList.remove('active'));
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
            
            if (tabName === 'dashboard') loadDashboard();
        }
        
        // Load dashboard data
        async function loadDashboard() {
            try {
                const response = await fetch('/api/summary');
                const data = await response.json();
                
                document.getElementById('total-emissions').textContent = data.total.toFixed(1);
                document.getElementById('scope1').textContent = data.scope1.toFixed(1);
                document.getElementById('scope2').textContent = data.scope2.toFixed(1);
                document.getElementById('scope3').textContent = data.scope3.toFixed(1);
                
                // Load recent uploads
                const recentResponse = await fetch('/api/recent');
                const recent = await recentResponse.json();
                const recentDiv = document.getElementById('recent-uploads');
                
                if (recent.length === 0) {
                    recentDiv.innerHTML = '<p>No uploads yet. Go to the Upload tab to get started!</p>';
                } else {
                    recentDiv.innerHTML = recent.map(r => `
                        <div style="padding: 12px; background: #f8f9fa; border-radius: 8px; margin: 10px 0;">
                            <strong>${r.filename}</strong> - ${r.scope.toUpperCase()} - ${r.emissions_kg.toFixed(1)} kg CO₂e
                            <br><small style="color: #666;">${r.upload_date}</small>
                        </div>
                    `).join('');
                }
            } catch (error) {
                console.error('Error loading dashboard:', error);
            }
        }
        
        // Handle file upload
        async function handleUpload(event) {
            const files = event.target.files;
            if (files.length === 0) return;
            
            const resultsDiv = document.getElementById('upload-results');
            resultsDiv.innerHTML = '<div class="loading">Processing files...</div>';
            
            const formData = new FormData();
            for (let file of files) {
                formData.append('files', file);
            }
            
            try {
                const response = await fetch('/api/upload', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    resultsDiv.innerHTML = `
                        <div class="success">
                            <strong>✓ Success!</strong> Processed ${data.processed} file(s)
                            <br>Total emissions: ${data.total_emissions.toFixed(1)} kg CO₂e
                        </div>
                        ${data.results.map(r => `
                            <div class="results">
                                <strong>${r.filename}</strong><br>
                                Classification: ${r.scope.toUpperCase()}<br>
                                Emissions: ${r.emissions.toFixed(1)} kg CO₂e<br>
                                Confidence: ${(r.confidence * 100).toFixed(0)}%
                            </div>
                        `).join('')}
                    `;
                    loadDashboard();
                } else {
                    resultsDiv.innerHTML = `<div class="error">Error: ${data.detail}</div>`;
                }
            } catch (error) {
                resultsDiv.innerHTML = `<div class="error">Error uploading files: ${error}</div>`;
            }
        }
        
        // Analytics
        async function analyzeQuery() {
            const query = document.getElementById('analytics-query').value;
            if (!query) return;
            
            const resultsDiv = document.getElementById('analytics-results');
            resultsDiv.innerHTML = '<div class="loading">Analyzing...</div>';
            
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query })
                });
                
                const data = await response.json();
                resultsDiv.innerHTML = `
                    <div class="results">
                        <h3>Analysis Results</h3>
                        <p>${data.response}</p>
                    </div>
                `;
            } catch (error) {
                resultsDiv.innerHTML = `<div class="error">Error: ${error}</div>`;
            }
        }
        
        // Recommendations
        async function getRecommendations() {
            const resultsDiv = document.getElementById('recommendations-results');
            resultsDiv.innerHTML = '<div class="loading">Generating recommendations...</div>';
            
            try {
                const response = await fetch('/api/recommendations');
                const data = await response.json();
                
                resultsDiv.innerHTML = data.recommendations.map(r => `
                    <div class="recommendation">
                        <h3>${r.title}</h3>
                        <p>${r.description}</p>
                        <div>
                            <span class="impact">Impact: ${r.estimated_reduction_percentage}% reduction</span>
                            <span class="impact">Cost: ${r.implementation_cost}</span>
                            <span class="impact">Timeframe: ${r.timeframe}</span>
                        </div>
                    </div>
                `).join('');
            } catch (error) {
                resultsDiv.innerHTML = `<div class="error">Error: ${error}</div>`;
            }
        }
        
        // Scenarios
        async function runScenario() {
            const query = document.getElementById('scenario-query').value;
            if (!query) return;
            
            const resultsDiv = document.getElementById('scenario-results');
            resultsDiv.innerHTML = '<div class="loading">Running scenario...</div>';
            
            try {
                const response = await fetch('/api/scenario', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ scenario_query: query })
                });
                
                const data = await response.json();
                resultsDiv.innerHTML = `
                    <div class="results">
                        <h3>Scenario Results</h3>
                        <div class="stats-grid">
                            <div class="stat-card">
                                <div class="stat-label">Baseline</div>
                                <div class="stat-value">${data.baseline.toFixed(1)}</div>
                                <div class="stat-label">kg CO₂e</div>
                            </div>
                            <div class="stat-card">
                                <div class="stat-label">Projected</div>
                                <div class="stat-value" style="color: #28a745;">${data.projected.toFixed(1)}</div>
                                <div class="stat-label">kg CO₂e</div>
                            </div>
                            <div class="stat-card">
                                <div class="stat-label">Reduction</div>
                                <div class="stat-value" style="color: #667eea;">${data.reduction_pct.toFixed(1)}%</div>
                                <div class="stat-label">${data.reduction_kg.toFixed(1)} kg</div>
                            </div>
                        </div>
                    </div>
                `;
            } catch (error) {
                resultsDiv.innerHTML = `<div class="error">Error: ${error}</div>`;
            }
        }
        
        // Clear all data
        async function clearAllData() {
            if (!confirm('⚠️ This will delete ALL uploaded data and reset emissions to zero. Are you sure?')) {
                return;
            }
            
            try {
                const response = await fetch('/api/clear', { method: 'POST' });
                const data = await response.json();
                
                if (response.ok) {
                    alert('✓ All data cleared successfully!');
                    loadDashboard(); // Reload dashboard
                    document.getElementById('upload-results').innerHTML = '';
                    document.getElementById('analytics-results').innerHTML = '';
                    document.getElementById('recommendations-results').innerHTML = '';
                    document.getElementById('scenario-results').innerHTML = '';
                } else {
                    alert('Error clearing data: ' + data.detail);
                }
            } catch (error) {
                alert('Error: ' + error);
            }
        }
        
        // Load dashboard on page load
        loadDashboard();
    </script>
</body>
</html>
"""

# Routes
@app.get("/", response_class=HTMLResponse)
async def home():
    """Serve the single-page application"""
    return HTML_TEMPLATE

@app.get("/api/summary")
async def get_summary():
    """Get emissions summary"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT scope, SUM(emissions_kg) FROM emissions GROUP BY scope")
    results = cursor.fetchall()
    
    summary = {"scope1": 0, "scope2": 0, "scope3": 0}
    for scope, total in results:
        summary[scope] = total or 0
    
    summary["total"] = sum(summary.values())
    
    conn.close()
    return summary

@app.get("/api/recent")
async def get_recent():
    """Get recent uploads"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT filename, upload_date, scope, emissions_kg
        FROM emissions
        ORDER BY upload_date DESC
        LIMIT 10
    """)
    
    results = cursor.fetchall()
    conn.close()
    
    return [
        {
            "filename": r[0],
            "upload_date": r[1],
            "scope": r[2],
            "emissions_kg": r[3]
        }
        for r in results
    ]

@app.post("/api/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    """Upload and process documents"""
    results = []
    total_emissions = 0
    
    for file in files:
        try:
            # Save file
            file_path = Path("data/uploads") / f"{datetime.now().timestamp()}_{file.filename}"
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            # Read content
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            # Classify
            classification = agent.classify_document(content)
            
            # Extract amounts
            amounts = agent.extract_amounts(content)
            
            # Calculate emissions (simple: $1 = 0.5 kg CO₂e for now)
            emissions = sum(a["value"] * 0.5 for a in amounts if a["type"] == "currency")
            if emissions == 0:
                emissions = 50  # Default estimate
            
            # Store in database
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO emissions (filename, upload_date, scope, category, emissions_kg, confidence, data)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                file.filename,
                datetime.now().isoformat(),
                classification["scope"],
                "general",
                emissions,
                classification["confidence"],
                content[:500]
            ))
            conn.commit()
            conn.close()
            
            total_emissions += emissions
            
            results.append({
                "filename": file.filename,
                "scope": classification["scope"],
                "emissions": emissions,
                "confidence": classification["confidence"]
            })
            
        except Exception as e:
            results.append({
                "filename": file.filename,
                "error": str(e)
            })
    
    return {
        "processed": len([r for r in results if "error" not in r]),
        "total_emissions": total_emissions,
        "results": results
    }

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """Simple chatbot"""
    query = request.query.lower()
    
    # Get summary
    summary = await get_summary()
    
    if "total" in query or "how much" in query:
        return {"response": f"Your total emissions are {summary['total']:.1f} kg CO₂e ({summary['total']/1000:.2f} tonnes)."}
    
    elif "highest" in query or "most" in query:
        highest = max(summary, key=lambda k: summary[k] if k != 'total' else 0)
        return {"response": f"{highest.upper()} has the highest emissions at {summary[highest]:.1f} kg CO₂e."}
    
    elif "suggest" in query or "reduce" in query:
        return {"response": "Top suggestions: 1) Replace 50% of travel with virtual meetings (20% reduction), 2) Switch to renewable energy (50% reduction in Scope 2), 3) Optimize cloud infrastructure (15% reduction)."}
    
    else:
        return {"response": f"Your emissions breakdown: Scope 1: {summary['scope1']:.1f}, Scope 2: {summary['scope2']:.1f}, Scope 3: {summary['scope3']:.1f} kg CO₂e."}

@app.get("/api/recommendations")
async def get_recommendations_api():
    """Get recommendations"""
    summary = await get_summary()
    recs = agent.generate_recommendations({"total_emissions_kg_co2e": summary["total"], "by_scope": summary})
    return {"recommendations": recs}

@app.post("/api/scenario")
async def run_scenario_api(request: ScenarioRequest):
    """Run scenario"""
    summary = await get_summary()
    baseline = summary["total"]
    
    projected_dict = agent.calculate_scenario(summary, request.scenario_query)
    projected = projected_dict.get("total_emissions_kg_co2e", baseline * 0.8)
    
    return {
        "baseline": baseline,
        "projected": projected,
        "reduction_kg": baseline - projected,
        "reduction_pct": ((baseline - projected) / baseline * 100) if baseline > 0 else 0
    }

@app.post("/api/clear")
async def clear_all_data():
    """Clear all data from database and uploads"""
    try:
        # Clear database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM emissions")
        conn.commit()
        deleted_count = cursor.rowcount
        conn.close()
        
        # Clear uploaded files
        uploads_dir = Path("data/uploads")
        if uploads_dir.exists():
            for file in uploads_dir.iterdir():
                if file.is_file():
                    file.unlink()
        
        return {
            "status": "success",
            "message": f"Cleared {deleted_count} emission records and all uploaded files"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
