# Hospital Management Demo - Setup Guide

## 🎯 Overview
This guide will help you set up and run the Hospital Management Demo with all 10 services. The demo showcases InterSystems IRIS capabilities in a healthcare environment.

## 📋 Prerequisites

### System Requirements
- **OS**: Linux, macOS, or Windows with WSL2
- **Docker**: Version 20.10+
- **Docker Compose**: Version 2.0+
- **RAM**: 18GB minimum (24GB recommended)
- **CPU**: 8 cores minimum
- **Storage**: 50GB free space

### Software Installation
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker --version
docker-compose --version
```

## 🚀 Quick Start

### 1. Clone and Setup
```bash
# Clone the repository
git clone <repository-url>
cd intersystem-iris-sample

# Create necessary directories
mkdir -p iris-data grafana/dashboards grafana/datasources grafana/conf
mkdir -p redis-data generated-data benchmark-results
mkdir -p services/hl7-simulator/logs services/analytics/logs
```

### 2. Start Core Services
```bash
# Start essential services first
docker-compose up -d iris grafana redis

# Wait for services to be ready (2-3 minutes)
docker-compose logs -f iris

# Verify core services
curl http://localhost:52773  # IRIS Management Portal
curl http://localhost:3000   # Grafana
redis-cli ping              # Redis
```

### 3. Generate Demo Data
```bash
# Generate hospital data
docker-compose run --rm data-generator

# Verify data generation
ls -la generated-data/
```

### 4. Start Integration Services
```bash
# Start HL7 simulator and mock systems
docker-compose up -d hl7-simulator mock-emr mock-lab mock-pharmacy

# Verify integration services
curl http://localhost:8080/health  # HL7 Simulator
curl http://localhost:8001/api/patients  # EMR
curl http://localhost:8002/api/tests     # Lab
curl http://localhost:8003/api/medications # Pharmacy
```

### 5. Start Analytics Services
```bash
# Start analytics and monitoring
docker-compose up -d analytics alerts monitoring

# Verify analytics services
curl http://localhost:8081/health  # Analytics
curl http://localhost:8082/health  # Alerts
curl http://localhost:9090/metrics # Monitoring
```

### 6. Run Performance Benchmarks
```bash
# Run performance tests
docker-compose run --rm benchmarking

# View benchmark results
ls -la benchmark-results/
```

## 🔧 Service Configuration

### IRIS Database
- **URL**: http://localhost:52773
- **Username**: SuperUser
- **Password**: SYS
- **Database Port**: 1972

### Grafana Dashboards
- **URL**: http://localhost:3000
- **Username**: admin
- **Password**: admin123

### Redis Queue
- **Host**: localhost
- **Port**: 6379
- **Database**: 0

### Service Endpoints
| Service | URL | Port | Description |
|---------|-----|------|-------------|
| IRIS | http://localhost:52773 | 52773 | Database Management Portal |
| Grafana | http://localhost:3000 | 3000 | Analytics Dashboards |
| Redis | redis://localhost:6379 | 6379 | Message Queue |
| HL7 Simulator | http://localhost:8080 | 8080 | HL7 Message Generator |
| EMR System | http://localhost:8001 | 8001 | Electronic Medical Records |
| Lab System | http://localhost:8002 | 8002 | Laboratory System |
| Pharmacy | http://localhost:8003 | 8003 | Pharmacy System |
| Analytics | http://localhost:8081 | 8081 | Analytics Engine |
| Alerts | http://localhost:8082 | 8082 | Alert Management |
| Monitoring | http://localhost:9090 | 9090 | Performance Monitoring |

## 📊 Demo Scenarios

### Scenario 1: Basic Demo (5 minutes)
```bash
# 1. Start core services
docker-compose up -d iris grafana redis

# 2. Generate sample data
docker-compose run --rm data-generator

# 3. Start HL7 simulator
docker-compose up -d hl7-simulator

# 4. Start simulation
curl -X POST http://localhost:8080/start \
  -H "Content-Type: application/json" \
  -d '{"message_rate": 10, "duration": 300}'

# 5. View dashboards
open http://localhost:3000
```

### Scenario 2: Full Demo (15 minutes)
```bash
# 1. Start all services
docker-compose up -d

# 2. Generate complete data
docker-compose run --rm data-generator

# 3. Start analytics processing
curl -X POST http://localhost:8081/start

# 4. Start HL7 simulation
curl -X POST http://localhost:8080/start \
  -H "Content-Type: application/json" \
  -d '{"message_rate": 50, "duration": 900}'

# 5. Run performance benchmarks
docker-compose run --rm benchmarking

# 6. View all dashboards and metrics
open http://localhost:3000
```

### Scenario 3: Performance Demo (10 minutes)
```bash
# 1. Start all services
docker-compose up -d

# 2. Run comprehensive benchmarks
docker-compose run --rm benchmarking

# 3. Start high-load simulation
curl -X POST http://localhost:8080/start \
  -H "Content-Type: application/json" \
  -d '{"message_rate": 100, "duration": 600}'

# 4. Monitor performance
open http://localhost:9090/metrics
open http://localhost:3000
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. Port Conflicts
```bash
# Check if ports are in use
netstat -tulpn | grep :52773
netstat -tulpn | grep :3000
netstat -tulpn | grep :6379

# Stop conflicting services
sudo systemctl stop <service-name>
```

#### 2. Memory Issues
```bash
# Check available memory
free -h

# Increase Docker memory limit
# Edit Docker Desktop settings or /etc/docker/daemon.json
```

#### 3. Service Startup Issues
```bash
# Check service logs
docker-compose logs iris
docker-compose logs grafana
docker-compose logs redis

# Restart specific service
docker-compose restart iris
```

#### 4. Data Generation Issues
```bash
# Check data generator logs
docker-compose logs data-generator

# Regenerate data
docker-compose run --rm data-generator
```

### Health Checks
```bash
# Check all services
docker-compose ps

# Check service health
curl http://localhost:52773/csp/sys/UtilHome.csp  # IRIS
curl http://localhost:3000/api/health             # Grafana
redis-cli ping                                    # Redis
curl http://localhost:8080/health                 # HL7 Simulator
curl http://localhost:8081/health                 # Analytics
curl http://localhost:8082/health                 # Alerts
curl http://localhost:9090/metrics                # Monitoring
```

## 📈 Performance Monitoring

### Real-time Metrics
```bash
# View service status
docker-compose ps

# Monitor resource usage
docker stats

# View logs
docker-compose logs -f

# Check Redis queue
redis-cli llen hl7_messages
```

### Grafana Dashboards
1. **Hospital Overview**: Real-time KPIs
2. **Department Performance**: Efficiency metrics
3. **Patient Flow**: Admission/discharge trends
4. **Revenue Analysis**: Financial metrics
5. **Staff Utilization**: Resource usage
6. **Predictive Insights**: Forecasts and recommendations

## 🔄 Maintenance

### Daily Operations
```bash
# Start services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

### Weekly Maintenance
```bash
# Update services
docker-compose pull
docker-compose up -d

# Clean up old data
docker system prune -f

# Backup data
tar -czf backup-$(date +%Y%m%d).tar.gz iris-data/ generated-data/
```

### Monthly Maintenance
```bash
# Full system restart
docker-compose down
docker-compose up -d

# Regenerate data
docker-compose run --rm data-generator

# Run comprehensive benchmarks
docker-compose run --rm benchmarking
```

## 📝 Next Steps

1. **Customize Configuration**: Modify service configurations for your environment
2. **Add Custom Dashboards**: Create additional Grafana dashboards
3. **Extend Data Generation**: Add more realistic hospital data
4. **Performance Tuning**: Optimize services for your hardware
5. **Integration Testing**: Test with real IRIS instances
6. **Demo Preparation**: Practice demo scenarios

## 🆘 Support

### Documentation
- [InterSystems IRIS Documentation](https://docs.intersystems.com/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Docker Documentation](https://docs.docker.com/)

### Troubleshooting Resources
- Service logs: `docker-compose logs <service-name>`
- Health checks: `curl http://localhost:<port>/health`
- Performance metrics: `http://localhost:9090/metrics`

This setup guide provides everything needed to run the Hospital Management Demo successfully!
