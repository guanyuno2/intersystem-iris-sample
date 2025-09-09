# Alert Management System Service

## 🎯 Service Overview
**Purpose**: Real-time alert management for critical events  
**Type**: Alert processing service  
**Priority**: Medium (Demo enhancement)

## 📋 Specifications
- **Technology**: Python 3.9+ with FastAPI
- **Dependencies**: `fastapi`, `redis`, `requests`, `pydantic`
- **Resources**: 
  - CPU: 0.5 cores
  - RAM: 1GB
  - Storage: 1GB

## 🔧 Configuration
```yaml
# docker-compose.yml
alerts:
  build: ./alerts
  container_name: alert-system
  ports: ["8080:8000"]
  depends_on: [iris, redis, grafana]
  environment:
    - IRIS_HOST=iris
    - REDIS_HOST=redis
    - GRAFANA_HOST=grafana
  restart: unless-stopped
```

## 📊 Alert Types

### 1. Critical Patient Alerts
```python
# Emergency patient admission
{
    "alert_id": "ALERT001",
    "type": "CRITICAL_PATIENT",
    "severity": "HIGH",
    "message": "Emergency patient admitted to ICU",
    "patient_id": "P123456",
    "department": "ICU",
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "ACTIVE"
}

# Patient condition change
{
    "alert_id": "ALERT002",
    "type": "CONDITION_CHANGE",
    "severity": "MEDIUM",
    "message": "Patient condition deteriorated",
    "patient_id": "P123456",
    "department": "Cardiology",
    "timestamp": "2024-01-15T10:35:00Z",
    "status": "ACTIVE"
}
```

### 2. System Alerts
```python
# High system load
{
    "alert_id": "ALERT003",
    "type": "SYSTEM_LOAD",
    "severity": "MEDIUM",
    "message": "High CPU usage detected",
    "system": "IRIS",
    "metric": "CPU_USAGE",
    "value": "85%",
    "timestamp": "2024-01-15T10:40:00Z",
    "status": "ACTIVE"
}

# Database connection issues
{
    "alert_id": "ALERT004",
    "type": "DATABASE_ERROR",
    "severity": "HIGH",
    "message": "Database connection timeout",
    "system": "IRIS",
    "error_code": "CONNECTION_TIMEOUT",
    "timestamp": "2024-01-15T10:45:00Z",
    "status": "ACTIVE"
}
```

### 3. HL7 Processing Alerts
```python
# Message processing errors
{
    "alert_id": "ALERT005",
    "type": "HL7_ERROR",
    "severity": "MEDIUM",
    "message": "HL7 message validation failed",
    "message_id": "MSG123456",
    "error_type": "VALIDATION_ERROR",
    "timestamp": "2024-01-15T10:50:00Z",
    "status": "ACTIVE"
}
```

## 📈 Alert Processing

### 1. Alert Generation
- **Source**: IRIS database events
- **Trigger**: Patient data changes, system metrics
- **Frequency**: Real-time
- **Volume**: 10-50 alerts/hour

### 2. Alert Routing
- **Critical**: Immediate notification
- **Medium**: Delayed notification
- **Low**: Logged only

### 3. Alert Resolution
- **Auto-resolution**: System recovery
- **Manual resolution**: User acknowledgment
- **Escalation**: Unresolved alerts

## 🛠️ Setup Commands
```bash
# Start alert system
docker-compose up -d alerts

# Test alert generation
docker exec -it alert-system python test_alerts.py

# View active alerts
curl http://localhost:8080/api/alerts/active
```

## 📝 Key Features for Demo
1. **Real-time Alerts**: Instant notification system
2. **Alert Classification**: Severity-based routing
3. **Dashboard Integration**: Visual alert display
4. **Alert History**: Historical alert tracking
5. **Notification System**: Email/SMS alerts

## 🔍 Monitoring
- **Health Check**: HTTP endpoint on port 8080
- **Logs**: Container logs via `docker logs alert-system`
- **Metrics**: Alert count, resolution time
- **API Status**: REST API health monitoring

## 📊 Demo Scenarios

### Scenario 1: Emergency Patient
1. Patient admitted to ICU
2. Critical alert generated
3. Dashboard shows red alert
4. Medical staff notified

### Scenario 2: System Performance
1. High CPU usage detected
2. System alert generated
3. Dashboard shows warning
4. IT team notified

### Scenario 3: HL7 Processing
1. Message validation fails
2. Processing alert generated
3. Dashboard shows error
4. Integration team notified

## 🎯 Success Metrics
- **Alert Response Time**: <30 seconds
- **Alert Accuracy**: 95% valid alerts
- **Resolution Time**: <5 minutes
- **Uptime**: 99% during demo
