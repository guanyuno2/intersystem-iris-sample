# Mock Hospital Systems Service

## 🎯 Service Overview
**Purpose**: Simulate various hospital subsystems (EMR, Lab, Pharmacy)  
**Type**: Integration simulation service  
**Priority**: Medium (Demo enhancement)

## 📋 Specifications
- **Technology**: Python 3.9+ with FastAPI
- **Components**: EMR, Laboratory, Pharmacy systems
- **Resources**: 
  - CPU: 1 core total
  - RAM: 2GB total
  - Storage: 2GB total

## 🔧 Configuration
```yaml
# docker-compose.yml
mock-emr:
  build: ./mock-systems/emr
  container_name: mock-emr
  ports: ["8001:8000"]
  depends_on: [iris]
  environment:
    - IRIS_HOST=iris
    - SYSTEM_TYPE=EMR
  restart: unless-stopped

mock-lab:
  build: ./mock-systems/lab
  container_name: mock-lab
  ports: ["8002:8000"]
  depends_on: [iris]
  environment:
    - IRIS_HOST=iris
    - SYSTEM_TYPE=LAB
  restart: unless-stopped

mock-pharmacy:
  build: ./mock-systems/pharmacy
  container_name: mock-pharmacy
  ports: ["8003:8000"]
  depends_on: [iris]
  environment:
    - IRIS_HOST=iris
    - SYSTEM_TYPE=PHARMACY
  restart: unless-stopped
```

## 🏥 System Components

### 1. Electronic Medical Records (EMR)
- **Port**: 8001
- **Features**:
  - Patient registration
  - Medical history
  - Prescription management
  - Appointment scheduling
- **Data**: 100 patient records

### 2. Laboratory System
- **Port**: 8002
- **Features**:
  - Lab test orders
  - Result processing
  - Quality control
  - Report generation
- **Tests**: 20 common lab tests

### 3. Pharmacy System
- **Port**: 8003
- **Features**:
  - Medication inventory
  - Prescription filling
  - Drug interaction checking
  - Dispensing records
- **Medications**: 50 common drugs

## 📊 API Endpoints

### EMR System
```python
# Patient management
GET /api/patients - List all patients
GET /api/patients/{id} - Get patient details
POST /api/patients - Create new patient
PUT /api/patients/{id} - Update patient

# Appointments
GET /api/appointments - List appointments
POST /api/appointments - Create appointment
PUT /api/appointments/{id} - Update appointment
```

### Laboratory System
```python
# Lab tests
GET /api/tests - List available tests
POST /api/orders - Create lab order
GET /api/results/{order_id} - Get test results
PUT /api/results/{order_id} - Update results
```

### Pharmacy System
```python
# Medications
GET /api/medications - List medications
POST /api/prescriptions - Create prescription
GET /api/inventory - Check inventory
POST /api/dispense - Dispense medication
```

## 🛠️ Setup Commands
```bash
# Start all mock systems
docker-compose up -d mock-emr mock-lab mock-pharmacy

# Test EMR system
curl http://localhost:8001/api/patients

# Test Lab system
curl http://localhost:8002/api/tests

# Test Pharmacy system
curl http://localhost:8003/api/medications
```

## 📝 Key Features for Demo
1. **Realistic Data**: Vietnamese patient names, addresses
2. **HL7 Integration**: Send HL7 messages to IRIS
3. **REST APIs**: Modern web service interfaces
4. **Error Simulation**: Occasional system errors
5. **Performance Metrics**: Response time tracking

## 🔍 Monitoring
- **Health Checks**: HTTP endpoints on each port
- **Logs**: Container logs for each system
- **Metrics**: API response times, error rates

## 📊 Demo Scenarios

### Scenario 1: Patient Registration
1. EMR receives new patient
2. Sends ADT^A01 to IRIS
3. Updates patient database
4. Triggers dashboard update

### Scenario 2: Lab Test Order
1. EMR creates lab order
2. Lab system processes order
3. Generates ORU^R01 message
4. Updates patient record

### Scenario 3: Prescription Filling
1. EMR creates prescription
2. Pharmacy checks inventory
3. Dispenses medication
4. Updates patient record

## 🎯 Success Metrics
- **API Response Time**: <200ms
- **HL7 Integration**: 100% message delivery
- **Error Rate**: <2% system errors
- **Uptime**: 99% during demo
