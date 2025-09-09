# InterSystems IRIS Database Service

## 🎯 Service Overview
**Purpose**: Core database platform and HL7 message processing engine  
**Type**: Primary data storage and integration platform  
**Priority**: Critical (Core service)

## 📋 Specifications
- **Version**: InterSystems IRIS 2024 Community Edition
- **Image**: `intersystemsdc/iris-community:latest`
- **Ports**: 
  - 52773 (Management Portal)
  - 1972 (Database)
- **Resources**: 
  - CPU: 2 cores
  - RAM: 4GB
  - Storage: 20GB

## 🔧 Configuration
```yaml
# docker-compose.yml
iris:
  image: intersystemsdc/iris-community:latest
  container_name: iris-database
  ports:
    - "52773:52773"
    - "1972:1972"
  volumes:
    - ./iris-data:/opt/irissys/mgr
    - ./src:/opt/demo/src
  environment:
    - IRIS_USERNAME=SuperUser
    - IRIS_PASSWORD=SYS
  restart: unless-stopped
```

## 📊 Database Schema
- **Patients**: 1,000 records (simplified from 10,000)
- **Doctors**: 20 records
- **Departments**: 10 records
- **Appointments**: 100 daily records
- **HL7 Messages**: Process 50-100 messages/minute

## 🔄 HL7 Integration
- **Message Types**: ADT^A01, ADT^A03, ORU^R01
- **Processing Rate**: 50-100 messages/minute
- **Validation**: Built-in HL7 message validation
- **Error Handling**: Automatic retry and logging

## 📈 Performance Targets
- **Query Response**: <500ms for simple queries
- **HL7 Processing**: 100 messages/minute
- **Concurrent Users**: 10-20 users
- **Uptime**: 99% during demo

## 🛠️ Setup Commands
```bash
# Start IRIS
docker-compose up -d iris

# Access Management Portal
open http://localhost:52773

# Login credentials
Username: SuperUser
Password: SYS
```

## 📝 Key Features for Demo
1. Real-time HL7 message processing
2. SQL queries for dashboard data
3. Built-in analytics capabilities
4. Web-based management interface
5. REST API endpoints for Grafana

## 🔍 Monitoring
- **Health Check**: HTTP endpoint on port 52773
- **Logs**: Container logs via `docker logs iris-database`
- **Metrics**: Built-in IRIS monitoring tools
