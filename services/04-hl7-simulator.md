# HL7 Message Simulator Service

## 🎯 Service Overview
**Purpose**: Generate realistic HL7 messages for hospital operations  
**Type**: Data simulation service  
**Priority**: High (Demo essential)

## 📋 Specifications
- **Technology**: Python 3.9+
- **Dependencies**: `hl7apy`, `faker`, `redis`, `requests`
- **Resources**: 
  - CPU: 1 core
  - RAM: 1GB
  - Storage: 1GB

## 🔧 Configuration
```yaml
# docker-compose.yml
hl7-simulator:
  build: ./hl7-simulator
  container_name: hl7-simulator
  depends_on: [iris, redis]
  environment:
    - IRIS_HOST=iris
    - REDIS_HOST=redis
    - MESSAGE_RATE=50
    - SIMULATION_DURATION=3600
  restart: unless-stopped
```

## 📊 Message Types

### 1. ADT^A01 - Patient Admission
```python
def generate_adt_a01():
    return f"""
MSH|^~\&|HIS|HOSPITAL_ABC|IRIS|INTEGRATION|{timestamp}||ADT^A01^ADT_A01|{msg_id}|P|2.5
PID|1||{patient_id}^^^HIS^MR||{name}||{dob}|{gender}|||{address}||{phone}
PV1|1|I|{ward}^{room}^{bed}|||{doctor_id}||||MED||||A|||{attending_dr}
"""
```

### 2. ADT^A03 - Patient Discharge
```python
def generate_adt_a03():
    return f"""
MSH|^~\&|HIS|HOSPITAL_ABC|IRIS|INTEGRATION|{timestamp}||ADT^A03^ADT_A03|{msg_id}|P|2.5
PID|1||{patient_id}^^^HIS^MR||{name}||{dob}|{gender}
PV1|1|O|{ward}^{room}^{bed}|||{doctor_id}||||MED||||A|||{attending_dr}
"""
```

### 3. ORU^R01 - Lab Results
```python
def generate_oru_r01():
    return f"""
MSH|^~\&|LAB|HOSPITAL_ABC|IRIS|INTEGRATION|{timestamp}||ORU^R01^ORU_R01|{msg_id}|P|2.5
PID|1||{patient_id}^^^HIS^MR||{name}||{dob}|{gender}
OBR|1||{lab_order_id}||{test_code}||{timestamp}||||||||{doctor_id}
OBX|1|NM|{test_code}||{result_value}||{units}||F|||{timestamp}
"""
```

## 📈 Simulation Parameters
- **Message Rate**: 50 messages/minute (reduced from 100-500)
- **Patient Count**: 100 active patients
- **Departments**: 5 departments
- **Doctors**: 10 doctors
- **Simulation Duration**: 1 hour demo

## 🛠️ Setup Commands
```bash
# Build and start simulator
docker-compose up -d hl7-simulator

# View simulator logs
docker logs -f hl7-simulator

# Test message generation
docker exec -it hl7-simulator python test_messages.py
```

## 📝 Key Features for Demo
1. **Realistic Data**: Vietnamese names, addresses, phone numbers
2. **Message Validation**: HL7 v2.5 compliant messages
3. **Error Simulation**: Occasional invalid messages for error handling demo
4. **Rate Control**: Configurable message generation rate
5. **Logging**: Detailed message generation logs

## 🔍 Monitoring
- **Health Check**: HTTP endpoint on port 8080
- **Logs**: Container logs via `docker logs hl7-simulator`
- **Metrics**: Message count, error rate, processing time

## 📊 Demo Scenarios

### Scenario 1: Normal Operations (30 minutes)
- Generate 25 ADT^A01 messages (admissions)
- Generate 20 ADT^A03 messages (discharges)
- Generate 30 ORU^R01 messages (lab results)

### Scenario 2: High Volume (10 minutes)
- Increase rate to 100 messages/minute
- Show system performance under load
- Demonstrate error handling

### Scenario 3: Emergency (5 minutes)
- Simulate emergency patient admission
- Generate critical alerts
- Show real-time dashboard updates

## 🎯 Success Metrics
- **Message Generation**: 50+ messages/minute
- **Error Rate**: <5% invalid messages
- **Processing Time**: <100ms per message
- **Uptime**: 99% during demo
