# Hospital Management Demo - Service Architecture

## 🎯 Overview
This directory contains detailed specifications for all 10 services required for the Hospital Management Demo. Each service is designed for a **small demo** with minimal resource requirements.

## 📊 Service Summary

| # | Service | Type | Priority | CPU | RAM | Storage |
|---|---------|------|----------|-----|-----|---------|
| 1 | [IRIS Database](01-iris-database.md) | Core | Critical | 2 | 4GB | 20GB |
| 2 | [Grafana Dashboards](02-grafana-dashboards.md) | Core | Critical | 1 | 2GB | 5GB |
| 3 | [Redis Queue](03-redis-queue.md) | Integration | High | 0.5 | 1GB | 2GB |
| 4 | [HL7 Simulator](04-hl7-simulator.md) | Simulation | High | 1 | 1GB | 1GB |
| 5 | [Mock Systems](05-mock-systems.md) | Integration | Medium | 1 | 2GB | 2GB |
| 6 | [Data Generator](06-data-generator.md) | Setup | Medium | 1 | 2GB | 5GB |
| 7 | [Analytics Engine](07-analytics-engine.md) | Analytics | High | 1 | 2GB | 2GB |
| 8 | [Alert System](08-alert-system.md) | Monitoring | Medium | 0.5 | 1GB | 1GB |
| 9 | [Performance Monitoring](09-performance-monitoring.md) | Monitoring | Medium | 0.5 | 1GB | 2GB |
| 10 | [Benchmarking Service](10-benchmarking-service.md) | Testing | Medium | 1 | 2GB | 3GB |

## 💻 Total Resource Requirements
- **Total CPU**: 9 cores
- **Total RAM**: 18GB
- **Total Storage**: 43GB

## 🚀 Quick Start

### 1. Core Services (Start First)
```bash
# Start essential services
docker-compose up -d iris grafana redis

# Verify core services
curl http://localhost:52773  # IRIS Management Portal
curl http://localhost:3000   # Grafana
redis-cli ping              # Redis
```

### 2. Integration Services
```bash
# Start integration services
docker-compose up -d hl7-simulator mock-emr mock-lab mock-pharmacy

# Verify integration
curl http://localhost:8001/api/patients  # EMR
curl http://localhost:8002/api/tests     # Lab
curl http://localhost:8003/api/medications # Pharmacy
```

### 3. Analytics & Monitoring
```bash
# Start analytics services
docker-compose up -d analytics alerts monitoring

# Verify analytics
curl http://localhost:8080/health  # Alerts
curl http://localhost:9090/metrics # Monitoring
```

### 4. Data Setup
```bash
# Generate demo data
docker-compose run --rm data-generator python generate_all_data.py

# Run performance benchmarks
docker-compose run --rm benchmarking python run_all_benchmarks.py
```

## 📋 Service Dependencies

```
IRIS Database (Core)
├── Grafana Dashboards
├── Redis Queue
├── HL7 Simulator
├── Mock Systems (EMR, Lab, Pharmacy)
├── Analytics Engine
├── Alert System
├── Performance Monitoring
└── Data Generator (Setup only)

Redis Queue
├── HL7 Simulator
├── Analytics Engine
└── Alert System

Grafana Dashboards
├── Analytics Engine
└── Performance Monitoring
```

## 🔧 Configuration Files

### docker-compose.yml
```yaml
version: '3.8'
services:
  iris:
    # See 01-iris-database.md for details
    
  grafana:
    # See 02-grafana-dashboards.md for details
    
  redis:
    # See 03-redis-queue.md for details
    
  # ... other services
```

### Environment Variables
```bash
# Core services
IRIS_HOST=iris
REDIS_HOST=redis
GRAFANA_HOST=grafana

# Demo configuration
PATIENT_COUNT=1000
DOCTOR_COUNT=20
DEPARTMENT_COUNT=10
MESSAGE_RATE=50
```

## 📊 Demo Scenarios

### Scenario 1: Basic Demo (5 minutes)
1. Start core services (IRIS, Grafana, Redis)
2. Generate sample data
3. Show basic dashboard
4. Demonstrate HL7 processing

### Scenario 2: Full Demo (15 minutes)
1. Start all services
2. Run complete data generation
3. Show all dashboards
4. Demonstrate performance comparison
5. Show alert system

### Scenario 3: Performance Demo (10 minutes)
1. Run benchmarking tests
2. Show performance comparisons
3. Demonstrate scalability
4. Show monitoring metrics

## 🎯 Success Criteria

### Technical Requirements
- [ ] All services start successfully
- [ ] IRIS processes HL7 messages
- [ ] Grafana displays real-time data
- [ ] Performance benchmarks complete
- [ ] Alert system functions properly

### Demo Requirements
- [ ] 15-minute presentation ready
- [ ] All dashboards functional
- [ ] Performance data available
- [ ] Error handling demonstrated
- [ ] Scalability shown

## 📝 Next Steps

1. **Review Service Specifications**: Read each service file for detailed requirements
2. **Set Up Development Environment**: Install Docker and required tools
3. **Configure Services**: Customize configurations for your environment
4. **Test Individual Services**: Verify each service works independently
5. **Integration Testing**: Test service interactions
6. **Demo Preparation**: Practice demo scenarios
7. **Performance Tuning**: Optimize for your hardware

## 🔍 Troubleshooting

### Common Issues
- **Port Conflicts**: Check if ports 3000, 52773, 6379 are available
- **Memory Issues**: Ensure sufficient RAM (18GB minimum)
- **Docker Issues**: Update Docker to latest version
- **Network Issues**: Check Docker network configuration

### Service Health Checks
```bash
# Check all services
docker-compose ps

# Check service logs
docker-compose logs [service-name]

# Restart specific service
docker-compose restart [service-name]
```

This architecture provides a complete, functional hospital management demo with minimal resource requirements, perfect for academic presentation and demonstration of InterSystems IRIS capabilities.
