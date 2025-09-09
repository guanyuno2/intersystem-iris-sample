#!/usr/bin/env python3
"""
Analytics Engine Service
Processes complex analytics queries and provides real-time insights
"""

import asyncio
import json
import logging
import os
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional

import pandas as pd
import redis
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/app/logs/analytics.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
IRIS_HOST = os.getenv('IRIS_HOST', 'iris')
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
GRAFANA_HOST = os.getenv('GRAFANA_HOST', 'grafana')

# Initialize FastAPI
app = FastAPI(title="Analytics Engine", version="1.0.0")

# Initialize Redis
redis_client = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

# Pydantic models
class AnalyticsQuery(BaseModel):
    query_type: str
    parameters: Dict = {}
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class AnalyticsResult(BaseModel):
    query_type: str
    result: Dict
    execution_time: float
    timestamp: str

class AnalyticsEngine:
    def __init__(self):
        self.cache = {}
        self.cache_ttl = 300  # 5 minutes
        self.is_running = False
        self.query_count = 0
        self.avg_response_time = 0
        
    def get_cached_result(self, query_key: str) -> Optional[Dict]:
        """Get cached query result"""
        if query_key in self.cache:
            cached_data, timestamp = self.cache[query_key]
            if time.time() - timestamp < self.cache_ttl:
                return cached_data
            else:
                del self.cache[query_key]
        return None
    
    def cache_result(self, query_key: str, result: Dict):
        """Cache query result"""
        self.cache[query_key] = (result, time.time())
    
    def execute_query(self, query_type: str, parameters: Dict = None) -> Dict:
        """Execute analytics query"""
        start_time = time.time()
        
        if parameters is None:
            parameters = {}
        
        # Check cache first
        query_key = f"{query_type}:{json.dumps(parameters, sort_keys=True)}"
        cached_result = self.get_cached_result(query_key)
        if cached_result:
            logger.info(f"Cache hit for query: {query_type}")
            return cached_result
        
        # Execute query based on type
        if query_type == "hospital_kpis":
            result = self.get_hospital_kpis()
        elif query_type == "department_performance":
            result = self.get_department_performance(parameters)
        elif query_type == "patient_flow":
            result = self.get_patient_flow(parameters)
        elif query_type == "revenue_analysis":
            result = self.get_revenue_analysis(parameters)
        elif query_type == "staff_utilization":
            result = self.get_staff_utilization(parameters)
        elif query_type == "predictive_analytics":
            result = self.get_predictive_analytics(parameters)
        else:
            raise ValueError(f"Unknown query type: {query_type}")
        
        # Cache result
        self.cache_result(query_key, result)
        
        # Update metrics
        execution_time = time.time() - start_time
        self.query_count += 1
        self.avg_response_time = (self.avg_response_time * (self.query_count - 1) + execution_time) / self.query_count
        
        logger.info(f"Executed query {query_type} in {execution_time:.3f}s")
        return result
    
    def get_hospital_kpis(self) -> Dict:
        """Get real-time hospital KPIs"""
        # Simulate data retrieval from IRIS
        # In real implementation, this would query IRIS database
        
        current_patients = 150 + int(time.time()) % 50  # Simulate varying patient count
        avg_los = 4.2 + (time.time() % 10) * 0.1  # Simulate varying LOS
        daily_revenue = 25000 + int(time.time()) % 10000  # Simulate varying revenue
        active_doctors = 18 + int(time.time()) % 5  # Simulate varying doctor count
        
        return {
            "current_patients": current_patients,
            "average_los": round(avg_los, 1),
            "daily_revenue": daily_revenue,
            "active_doctors": active_doctors,
            "bed_occupancy": round((current_patients / 200) * 100, 1),  # Assuming 200 total beds
            "patient_satisfaction": round(4.2 + (time.time() % 10) * 0.05, 1)
        }
    
    def get_department_performance(self, parameters: Dict) -> Dict:
        """Get department performance metrics"""
        departments = [
            {"name": "Emergency", "patients": 45, "avg_los": 2.1, "revenue": 8500, "efficiency": 92},
            {"name": "Cardiology", "patients": 32, "avg_los": 5.8, "revenue": 12000, "efficiency": 88},
            {"name": "Neurology", "patients": 28, "avg_los": 6.2, "revenue": 10500, "efficiency": 85},
            {"name": "Orthopedics", "patients": 38, "avg_los": 4.5, "revenue": 9800, "efficiency": 90},
            {"name": "ICU", "patients": 15, "avg_los": 8.1, "revenue": 15000, "efficiency": 95}
        ]
        
        # Add some variation based on time
        for dept in departments:
            variation = int(time.time()) % 10 - 5
            dept["patients"] = max(0, dept["patients"] + variation)
            dept["efficiency"] = max(0, min(100, dept["efficiency"] + variation))
        
        return {
            "departments": departments,
            "total_patients": sum(dept["patients"] for dept in departments),
            "total_revenue": sum(dept["revenue"] for dept in departments),
            "average_efficiency": round(sum(dept["efficiency"] for dept in departments) / len(departments), 1)
        }
    
    def get_patient_flow(self, parameters: Dict) -> Dict:
        """Get patient flow analytics"""
        # Simulate patient flow data
        hours = list(range(24))
        admissions = [max(0, 5 + int(time.time() + h) % 15) for h in hours]
        discharges = [max(0, 4 + int(time.time() + h) % 12) for h in hours]
        
        return {
            "hourly_flow": {
                "hours": hours,
                "admissions": admissions,
                "discharges": discharges
            },
            "peak_admission_hour": admissions.index(max(admissions)),
            "peak_discharge_hour": discharges.index(max(discharges)),
            "net_patient_change": sum(admissions) - sum(discharges)
        }
    
    def get_revenue_analysis(self, parameters: Dict) -> Dict:
        """Get revenue analysis"""
        # Simulate revenue data
        daily_revenue = 25000 + int(time.time()) % 15000
        monthly_revenue = daily_revenue * 30
        revenue_by_department = {
            "Emergency": daily_revenue * 0.25,
            "Cardiology": daily_revenue * 0.30,
            "Neurology": daily_revenue * 0.20,
            "Orthopedics": daily_revenue * 0.15,
            "ICU": daily_revenue * 0.10
        }
        
        return {
            "daily_revenue": daily_revenue,
            "monthly_revenue": monthly_revenue,
            "revenue_by_department": revenue_by_department,
            "revenue_growth": round((time.time() % 20) - 10, 1)  # Simulate growth rate
        }
    
    def get_staff_utilization(self, parameters: Dict) -> Dict:
        """Get staff utilization metrics"""
        # Simulate staff utilization data
        doctors_utilization = 75 + int(time.time()) % 20
        nurses_utilization = 80 + int(time.time()) % 15
        support_staff_utilization = 65 + int(time.time()) % 25
        
        return {
            "doctors_utilization": doctors_utilization,
            "nurses_utilization": nurses_utilization,
            "support_staff_utilization": support_staff_utilization,
            "average_utilization": round((doctors_utilization + nurses_utilization + support_staff_utilization) / 3, 1),
            "overtime_hours": 45 + int(time.time()) % 30
        }
    
    def get_predictive_analytics(self, parameters: Dict) -> Dict:
        """Get predictive analytics"""
        # Simulate predictive data
        current_patients = 150 + int(time.time()) % 50
        predicted_patients = current_patients + int(time.time() % 20) - 10
        
        return {
            "current_patient_count": current_patients,
            "predicted_patient_count": predicted_patients,
            "prediction_confidence": 85 + int(time.time()) % 10,
            "trend": "increasing" if predicted_patients > current_patients else "decreasing",
            "recommended_actions": [
                "Increase ICU capacity" if predicted_patients > 180 else "Maintain current capacity",
                "Schedule additional staff" if predicted_patients > current_patients else "Optimize current staffing"
            ]
        }
    
    async def send_to_grafana(self, data: Dict, panel_name: str):
        """Send analytics data to Grafana"""
        try:
            # In real implementation, this would send to Grafana API
            logger.info(f"Sending {panel_name} data to Grafana")
            
            # Store in Redis for Grafana to consume
            redis_client.set(f"grafana:{panel_name}", json.dumps(data), ex=300)
            
        except Exception as e:
            logger.error(f"Error sending to Grafana: {e}")
    
    async def run_analytics_loop(self):
        """Run continuous analytics processing"""
        self.is_running = True
        logger.info("Starting analytics processing loop...")
        
        while self.is_running:
            try:
                # Process different analytics queries
                queries = [
                    ("hospital_kpis", "hospital_overview"),
                    ("department_performance", "department_metrics"),
                    ("patient_flow", "patient_flow"),
                    ("revenue_analysis", "revenue_metrics"),
                    ("staff_utilization", "staff_metrics"),
                    ("predictive_analytics", "predictive_insights")
                ]
                
                for query_type, panel_name in queries:
                    result = self.execute_query(query_type)
                    await self.send_to_grafana(result, panel_name)
                
                # Wait 10 seconds before next iteration
                await asyncio.sleep(10)
                
            except Exception as e:
                logger.error(f"Error in analytics loop: {e}")
                await asyncio.sleep(5)
        
        logger.info("Analytics processing loop stopped")

# Initialize analytics engine
analytics_engine = AnalyticsEngine()

# API Endpoints
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "query_count": analytics_engine.query_count,
        "avg_response_time": round(analytics_engine.avg_response_time, 3)
    }

@app.get("/status")
async def get_status():
    """Get analytics engine status"""
    return {
        "is_running": analytics_engine.is_running,
        "query_count": analytics_engine.query_count,
        "avg_response_time": round(analytics_engine.avg_response_time, 3),
        "cache_size": len(analytics_engine.cache)
    }

@app.post("/query")
async def execute_analytics_query(query: AnalyticsQuery):
    """Execute analytics query"""
    try:
        result = analytics_engine.execute_query(query.query_type, query.parameters)
        return AnalyticsResult(
            query_type=query.query_type,
            result=result,
            execution_time=analytics_engine.avg_response_time,
            timestamp=datetime.now().isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/queries")
async def get_available_queries():
    """Get list of available analytics queries"""
    return {
        "available_queries": [
            "hospital_kpis",
            "department_performance",
            "patient_flow",
            "revenue_analysis",
            "staff_utilization",
            "predictive_analytics"
        ],
        "query_descriptions": {
            "hospital_kpis": "Real-time hospital key performance indicators",
            "department_performance": "Department efficiency and performance metrics",
            "patient_flow": "Patient admission and discharge flow analysis",
            "revenue_analysis": "Revenue analysis by department and time period",
            "staff_utilization": "Staff utilization and efficiency metrics",
            "predictive_analytics": "Predictive insights and recommendations"
        }
    }

@app.post("/start")
async def start_analytics():
    """Start analytics processing"""
    if analytics_engine.is_running:
        raise HTTPException(status_code=400, detail="Analytics already running")
    
    asyncio.create_task(analytics_engine.run_analytics_loop())
    return {"message": "Analytics processing started"}

@app.post("/stop")
async def stop_analytics():
    """Stop analytics processing"""
    analytics_engine.is_running = False
    return {"message": "Analytics processing stopped"}

@app.get("/cache")
async def get_cache_info():
    """Get cache information"""
    return {
        "cache_size": len(analytics_engine.cache),
        "cache_ttl": analytics_engine.cache_ttl,
        "cached_queries": list(analytics_engine.cache.keys())
    }

@app.delete("/cache")
async def clear_cache():
    """Clear analytics cache"""
    analytics_engine.cache.clear()
    return {"message": "Cache cleared"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
