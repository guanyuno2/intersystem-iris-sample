#!/usr/bin/env python3
"""
HL7 Message Simulator Service
Generates realistic HL7 messages for hospital operations demo
"""

import asyncio
import json
import logging
import os
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional

import redis
import requests
from faker import Faker
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/app/logs/hl7_simulator.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialize Faker with Vietnamese locale
fake = Faker('vi_VN')

# Configuration
IRIS_HOST = os.getenv('IRIS_HOST', 'iris')
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
MESSAGE_RATE = int(os.getenv('MESSAGE_RATE', '50'))
SIMULATION_DURATION = int(os.getenv('SIMULATION_DURATION', '3600'))

# Initialize FastAPI
app = FastAPI(title="HL7 Message Simulator", version="1.0.0")

# Initialize Redis
redis_client = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

# Pydantic models
class HL7Message(BaseModel):
    message_type: str
    patient_id: str
    content: str
    timestamp: str
    status: str = "PENDING"

class SimulationConfig(BaseModel):
    message_rate: int = 50
    duration: int = 3600
    patient_count: int = 100
    department_count: int = 5
    doctor_count: int = 10

class HL7Simulator:
    def __init__(self):
        self.is_running = False
        self.message_count = 0
        self.error_count = 0
        self.start_time = None
        self.patients = []
        self.doctors = []
        self.departments = []
        self.initialize_data()
    
    def initialize_data(self):
        """Initialize demo data"""
        logger.info("Initializing demo data...")
        
        # Generate departments
        self.departments = [
            {'id': 'DEPT001', 'name': 'Emergency', 'beds': 20},
            {'id': 'DEPT002', 'name': 'Cardiology', 'beds': 15},
            {'id': 'DEPT003', 'name': 'Neurology', 'beds': 12},
            {'id': 'DEPT004', 'name': 'Orthopedics', 'beds': 18},
            {'id': 'DEPT005', 'name': 'ICU', 'beds': 10}
        ]
        
        # Generate doctors
        specialties = ['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Surgery']
        for i in range(10):
            doctor = {
                'id': f'D{i:03d}',
                'name': fake.name(),
                'specialty': random.choice(specialties),
                'department': random.choice(self.departments)['id'],
                'license': fake.random_number(digits=8)
            }
            self.doctors.append(doctor)
        
        # Generate patients
        for i in range(100):
            patient = {
                'id': f'P{i:06d}',
                'name': fake.name(),
                'dob': fake.date_of_birth(minimum_age=0, maximum_age=100).strftime('%Y%m%d'),
                'gender': random.choice(['M', 'F']),
                'address': fake.address().replace('\n', ' '),
                'phone': fake.phone_number(),
                'insurance': random.choice(['A', 'B', 'C']),
                'admission_date': fake.date_between(start_date='-30d', end_date='today').strftime('%Y%m%d%H%M%S')
            }
            self.patients.append(patient)
        
        logger.info(f"Initialized {len(self.patients)} patients, {len(self.doctors)} doctors, {len(self.departments)} departments")
    
    def generate_adt_a01(self) -> str:
        """Generate ADT^A01 (Patient Admission) message"""
        patient = random.choice(self.patients)
        doctor = random.choice(self.doctors)
        department = random.choice(self.departments)
        
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        msg_id = f"MSG{int(time.time())}"
        
        message = f"""MSH|^~\\&|HIS|HOSPITAL_ABC|IRIS|INTEGRATION|{timestamp}||ADT^A01^ADT_A01|{msg_id}|P|2.5
PID|1||{patient['id']}^^^HIS^MR||{patient['name']}||{patient['dob']}|{patient['gender']}|||{patient['address']}||{patient['phone']}
PV1|1|I|{department['id']}^{random.randint(1, 20)}^{random.randint(1, 4)}|||{doctor['id']}||||MED||||A|||{doctor['name']}"""
        
        return message.strip()
    
    def generate_adt_a03(self) -> str:
        """Generate ADT^A03 (Patient Discharge) message"""
        patient = random.choice(self.patients)
        doctor = random.choice(self.doctors)
        department = random.choice(self.departments)
        
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        msg_id = f"MSG{int(time.time())}"
        
        message = f"""MSH|^~\\&|HIS|HOSPITAL_ABC|IRIS|INTEGRATION|{timestamp}||ADT^A03^ADT_A03|{msg_id}|P|2.5
PID|1||{patient['id']}^^^HIS^MR||{patient['name']}||{patient['dob']}|{patient['gender']}
PV1|1|O|{department['id']}^{random.randint(1, 20)}^{random.randint(1, 4)}|||{doctor['id']}||||MED||||A|||{doctor['name']}"""
        
        return message.strip()
    
    def generate_oru_r01(self) -> str:
        """Generate ORU^R01 (Lab Results) message"""
        patient = random.choice(self.patients)
        doctor = random.choice(self.doctors)
        
        test_codes = ['CBC', 'CHEM7', 'LIPID', 'GLUCOSE', 'BUN', 'CREATININE']
        test_code = random.choice(test_codes)
        result_value = round(random.uniform(10, 200), 1)
        units = random.choice(['mg/dL', 'g/dL', 'U/L', 'cells/uL'])
        
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        msg_id = f"MSG{int(time.time())}"
        lab_order_id = f"LAB{int(time.time())}"
        
        message = f"""MSH|^~\\&|LAB|HOSPITAL_ABC|IRIS|INTEGRATION|{timestamp}||ORU^R01^ORU_R01|{msg_id}|P|2.5
PID|1||{patient['id']}^^^HIS^MR||{patient['name']}||{patient['dob']}|{patient['gender']}
OBR|1||{lab_order_id}||{test_code}||{timestamp}||||||||{doctor['id']}
OBX|1|NM|{test_code}||{result_value}||{units}||F|||{timestamp}"""
        
        return message.strip()
    
    def send_to_iris(self, message: str) -> bool:
        """Send HL7 message to IRIS database"""
        try:
            # In a real implementation, this would send to IRIS HL7 service
            # For demo purposes, we'll simulate the call
            logger.info(f"Sending HL7 message to IRIS: {message[:100]}...")
            
            # Simulate processing time
            time.sleep(0.1)
            
            # Store in Redis for analytics
            redis_client.lpush('hl7_messages', json.dumps({
                'message': message,
                'timestamp': datetime.now().isoformat(),
                'status': 'PROCESSED'
            }))
            
            return True
        except Exception as e:
            logger.error(f"Error sending to IRIS: {e}")
            return False
    
    def send_to_redis(self, message: str, message_type: str) -> bool:
        """Send message to Redis queue"""
        try:
            message_data = {
                'message_type': message_type,
                'content': message,
                'timestamp': datetime.now().isoformat(),
                'status': 'PENDING'
            }
            
            redis_client.lpush('hl7_messages', json.dumps(message_data))
            return True
        except Exception as e:
            logger.error(f"Error sending to Redis: {e}")
            return False
    
    async def run_simulation(self, config: SimulationConfig):
        """Run HL7 message simulation"""
        self.is_running = True
        self.start_time = time.time()
        self.message_count = 0
        self.error_count = 0
        
        logger.info(f"Starting HL7 simulation: {config.message_rate} msg/min for {config.duration}s")
        
        message_types = ['ADT^A01', 'ADT^A03', 'ORU^R01']
        message_generators = {
            'ADT^A01': self.generate_adt_a01,
            'ADT^A03': self.generate_adt_a03,
            'ORU^R01': self.generate_oru_r01
        }
        
        end_time = time.time() + config.duration
        interval = 60.0 / config.message_rate  # seconds between messages
        
        while self.is_running and time.time() < end_time:
            try:
                # Choose random message type
                msg_type = random.choice(message_types)
                generator = message_generators[msg_type]
                
                # Generate message
                message = generator()
                
                # Send to systems
                iris_success = self.send_to_iris(message)
                redis_success = self.send_to_redis(message, msg_type)
                
                if iris_success and redis_success:
                    self.message_count += 1
                    logger.info(f"Generated {msg_type} message #{self.message_count}")
                else:
                    self.error_count += 1
                    logger.error(f"Failed to send {msg_type} message")
                
                # Wait for next message
                await asyncio.sleep(interval)
                
            except Exception as e:
                logger.error(f"Error in simulation: {e}")
                self.error_count += 1
                await asyncio.sleep(1)
        
        self.is_running = False
        logger.info(f"Simulation completed: {self.message_count} messages sent, {self.error_count} errors")

# Initialize simulator
simulator = HL7Simulator()

# API Endpoints
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/status")
async def get_status():
    """Get simulation status"""
    return {
        "is_running": simulator.is_running,
        "message_count": simulator.message_count,
        "error_count": simulator.error_count,
        "start_time": simulator.start_time,
        "uptime": time.time() - simulator.start_time if simulator.start_time else 0
    }

@app.post("/start")
async def start_simulation(config: SimulationConfig):
    """Start HL7 message simulation"""
    if simulator.is_running:
        raise HTTPException(status_code=400, detail="Simulation already running")
    
    # Start simulation in background
    asyncio.create_task(simulator.run_simulation(config))
    
    return {"message": "Simulation started", "config": config.dict()}

@app.post("/stop")
async def stop_simulation():
    """Stop HL7 message simulation"""
    simulator.is_running = False
    return {"message": "Simulation stopped"}

@app.get("/messages")
async def get_recent_messages(limit: int = 10):
    """Get recent HL7 messages"""
    try:
        messages = redis_client.lrange('hl7_messages', 0, limit - 1)
        return [json.loads(msg) for msg in messages]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test")
async def test_message_generation():
    """Generate test HL7 messages"""
    messages = {
        "ADT^A01": simulator.generate_adt_a01(),
        "ADT^A03": simulator.generate_adt_a03(),
        "ORU^R01": simulator.generate_oru_r01()
    }
    return messages

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
