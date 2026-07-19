"""
Simple Agent - Rule-based processing without LLM
Used when API keys are not available
"""
from typing import Dict, Any, List
import re
from datetime import datetime
from loguru import logger


class SimpleAgent:
    """
    Provides basic AI-like functionality without requiring LLM API calls.
    Uses rule-based logic, keyword matching, and statistical analysis.
    """
    
    def __init__(self):
        self.emission_keywords = {
            "scope1": ["fuel", "gasoline", "petrol", "diesel", "natural gas", "combustion", "vehicle", "fleet"],
            "scope2": ["electricity", "kwh", "power", "energy", "heating", "cooling", "utility"],
            "scope3": ["flight", "travel", "hotel", "cloud", "aws", "azure", "gcp", "office supplies", "commute"]
        }
    
    def classify_document(self, text: str) -> Dict[str, Any]:
        """Classify document into emission scope based on keywords"""
        text_lower = text.lower()
        
        scores = {
            "scope1": 0,
            "scope2": 0,
            "scope3": 0
        }
        
        # Count keyword matches
        for scope, keywords in self.emission_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    scores[scope] += 1
        
        # Determine classification
        best_scope = max(scores, key=scores.get)
        confidence = scores[best_scope] / sum(scores.values()) if sum(scores.values()) > 0 else 0.5
        
        # Default to scope3 if no clear match
        if scores[best_scope] == 0:
            best_scope = "scope3"
            confidence = 0.3
        
        return {
            "scope": best_scope,
            "confidence": confidence,
            "reasoning": f"Detected {scores[best_scope]} relevant keywords for {best_scope}"
        }
    
    def extract_amounts(self, text: str) -> List[Dict[str, Any]]:
        """Extract monetary amounts and quantities from text"""
        # Pattern for currency amounts
        currency_pattern = r'\$?\s*(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s*(?:USD|dollars?|\$)?'
        
        # Pattern for quantities with units
        quantity_pattern = r'(\d+(?:\.\d+)?)\s*(kwh|liters?|litres?|km|miles|hours?|gb|tb|nights?)'
        
        amounts = []
        
        # Find currency amounts
        for match in re.finditer(currency_pattern, text, re.IGNORECASE):
            amount = float(match.group(1).replace(',', ''))
            amounts.append({
                "type": "currency",
                "value": amount,
                "unit": "USD"
            })
        
        # Find quantities
        for match in re.finditer(quantity_pattern, text, re.IGNORECASE):
            value = float(match.group(1))
            unit = match.group(2).lower()
            amounts.append({
                "type": "quantity",
                "value": value,
                "unit": unit
            })
        
        return amounts
    
    def generate_insights(self, data: List[Dict[str, Any]]) -> List[str]:
        """Generate simple insights from emission data"""
        if not data:
            return ["No data available for analysis"]
        
        insights = []
        
        # Calculate totals by scope
        by_scope = {}
        for record in data:
            scope = record.get("scope", "scope3")
            emissions = record.get("total_emissions_kg_co2e", 0)
            by_scope[scope] = by_scope.get(scope, 0) + emissions
        
        total = sum(by_scope.values())
        
        # Highest contributor
        if by_scope:
            highest_scope = max(by_scope, key=by_scope.get)
            pct = (by_scope[highest_scope] / total * 100) if total > 0 else 0
            insights.append(f"{highest_scope.title()} is your largest contributor at {pct:.1f}% of total emissions")
        
        # Trends
        if len(data) >= 2:
            recent_avg = sum(d.get("total_emissions_kg_co2e", 0) for d in data[-3:]) / min(3, len(data))
            older_avg = sum(d.get("total_emissions_kg_co2e", 0) for d in data[:3]) / min(3, len(data))
            
            if recent_avg > older_avg * 1.1:
                change_pct = ((recent_avg - older_avg) / older_avg * 100)
                insights.append(f"Emissions have increased by {change_pct:.1f}% recently")
            elif recent_avg < older_avg * 0.9:
                change_pct = ((older_avg - recent_avg) / older_avg * 100)
                insights.append(f"Great news! Emissions have decreased by {change_pct:.1f}%")
        
        # Total emissions
        insights.append(f"Total tracked emissions: {total:.1f} kg CO₂e ({total/1000:.2f} tonnes)")
        
        return insights
    
    def generate_recommendations(self, emissions_summary: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate standard reduction recommendations"""
        total = emissions_summary.get("total_emissions_kg_co2e", 1000)
        by_scope = emissions_summary.get("by_scope", {})
        
        recommendations = []
        
        # Travel recommendations if Scope 3 is high
        if by_scope.get("scope3", 0) > total * 0.4:
            recommendations.append({
                "title": "Implement Virtual Meeting Policy",
                "description": "Replace 50% of short-distance travel with virtual meetings using video conferencing",
                "category": "travel",
                "scope": "scope3",
                "estimated_reduction_percentage": 20,
                "estimated_reduction_kg_co2e": total * 0.2,
                "implementation_cost": "low",
                "timeframe": "short",
                "effort": "low",
                "feasibility": 95,
                "priority_score": 85,
                "priority_label": "High",
                "prerequisites": ["Video conferencing tools", "Policy documentation", "Employee training"]
            })
        
        # Energy recommendations if Scope 2 is high
        if by_scope.get("scope2", 0) > total * 0.3:
            recommendations.append({
                "title": "Switch to Renewable Energy",
                "description": "Transition office electricity to renewable energy sources through green energy programs",
                "category": "renewable",
                "scope": "scope2",
                "estimated_reduction_percentage": 50,
                "estimated_reduction_kg_co2e": by_scope.get("scope2", 0) * 0.5,
                "implementation_cost": "medium",
                "timeframe": "medium",
                "effort": "medium",
                "feasibility": 80,
                "priority_score": 75,
                "priority_label": "High",
                "prerequisites": ["Renewable energy provider", "Contract negotiation", "Budget approval"]
            })
        
        # Cloud optimization for Scope 3
        recommendations.append({
            "title": "Optimize Cloud Infrastructure",
            "description": "Right-size cloud resources, implement auto-scaling, and shut down unused instances",
            "category": "cloud",
            "scope": "scope3",
            "estimated_reduction_percentage": 15,
            "estimated_reduction_kg_co2e": total * 0.15,
            "implementation_cost": "low",
            "timeframe": "short",
            "effort": "medium",
            "feasibility": 90,
            "priority_score": 80,
            "priority_label": "High",
            "prerequisites": ["Cloud monitoring tools", "DevOps team", "Cost analysis"]
        })
        
        # Energy efficiency
        recommendations.append({
            "title": "LED Lighting Upgrade",
            "description": "Replace traditional lighting with LED bulbs for 75% energy savings",
            "category": "energy",
            "scope": "scope2",
            "estimated_reduction_percentage": 10,
            "estimated_reduction_kg_co2e": by_scope.get("scope2", 0) * 0.1,
            "implementation_cost": "low",
            "timeframe": "short",
            "effort": "low",
            "feasibility": 95,
            "priority_score": 75,
            "priority_label": "Medium",
            "prerequisites": ["Lighting audit", "Procurement", "Installation schedule"]
        })
        
        # Fuel efficiency if Scope 1 exists
        if by_scope.get("scope1", 0) > 0:
            recommendations.append({
                "title": "Fleet Vehicle Optimization",
                "description": "Implement route optimization and driver training for fuel efficiency",
                "category": "fuel",
                "scope": "scope1",
                "estimated_reduction_percentage": 15,
                "estimated_reduction_kg_co2e": by_scope.get("scope1", 0) * 0.15,
                "implementation_cost": "low",
                "timeframe": "short",
                "effort": "medium",
                "feasibility": 85,
                "priority_score": 70,
                "priority_label": "Medium",
                "prerequisites": ["Route planning software", "Driver training program"]
            })
        
        return recommendations
    
    def calculate_scenario(self, baseline: Dict[str, Any], scenario_text: str) -> Dict[str, Any]:
        """Calculate scenario impact using simple percentage reduction"""
        # Extract percentage from scenario text
        percentage_match = re.search(r'(\d+)%', scenario_text)
        reduction_pct = int(percentage_match.group(1)) if percentage_match else 20
        
        # Determine which scope to target
        if "travel" in scenario_text.lower() or "virtual" in scenario_text.lower():
            target_scope = "scope3"
        elif "energy" in scenario_text.lower() or "renewable" in scenario_text.lower():
            target_scope = "scope2"
        elif "cloud" in scenario_text.lower():
            target_scope = "scope3"
        else:
            target_scope = "all"
        
        # Calculate projected emissions
        projected = baseline.copy()
        
        if target_scope == "all":
            reduction_factor = 1 - (reduction_pct / 100)
            if "total_emissions_kg_co2e" in projected:
                projected["total_emissions_kg_co2e"] *= reduction_factor
            if "by_scope" in projected:
                for scope in projected["by_scope"]:
                    projected["by_scope"][scope] *= reduction_factor
        else:
            if "by_scope" in projected and target_scope in projected["by_scope"]:
                reduction_factor = 1 - (reduction_pct / 100)
                projected["by_scope"][target_scope] *= reduction_factor
                projected["total_emissions_kg_co2e"] = sum(projected["by_scope"].values())
        
        return projected


# Global instance
simple_agent = SimpleAgent()
