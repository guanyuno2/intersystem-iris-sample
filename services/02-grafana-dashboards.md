# Grafana Dashboards Service

## 🎯 Service Overview
**Purpose**: Real-time visualization and analytics dashboards  
**Type**: Data visualization platform  
**Priority**: Critical (Core service)

## 📋 Specifications
- **Version**: Grafana 10.x
- **Image**: `grafana/grafana:latest`
- **Port**: 3000
- **Resources**: 
  - CPU: 1 core
  - RAM: 2GB
  - Storage: 5GB

## 🔧 Configuration
```yaml
# docker-compose.yml
grafana:
  image: grafana/grafana:latest
  container_name: grafana-dashboards
  ports:
    - "3000:3000"
  volumes:
    - ./grafana/dashboards:/var/lib/grafana/dashboards
    - ./grafana/datasources:/etc/grafana/provisioning/datasources
    - ./grafana/conf:/etc/grafana
  environment:
    - GF_SECURITY_ADMIN_PASSWORD=admin123
  restart: unless-stopped
```

## 📊 Dashboard Components

### 1. Executive Dashboard
- **Patient Volume**: Real-time patient count
- **Bed Occupancy**: Current bed utilization
- **Revenue**: Daily revenue tracking
- **Staff Utilization**: Doctor/nurse workload

### 2. Clinical Dashboard
- **Patient Flow**: Admission/discharge trends
- **Department Performance**: Efficiency metrics
- **Treatment Outcomes**: Success rates
- **Quality Indicators**: Readmission rates

### 3. Performance Dashboard
- **System Metrics**: IRIS performance
- **HL7 Processing**: Message throughput
- **Query Performance**: Response times
- **Resource Usage**: CPU/Memory utilization

## 🔌 Data Sources
- **IRIS Database**: Primary data source
- **Redis**: Real-time metrics
- **Mock Systems**: Hospital subsystem data

## 📈 Dashboard Features
- **Auto-refresh**: Every 10 seconds
- **Interactive**: Drill-down capabilities
- **Mobile**: Responsive design
- **Alerts**: Visual notifications
- **Export**: PDF/PNG export

## 🛠️ Setup Commands
```bash
# Start Grafana
docker-compose up -d grafana

# Access Grafana
open http://localhost:3000

# Login credentials
Username: admin
Password: admin123
```

## 📝 Key Metrics to Display
1. **Real-time Patient Count**: Current patients in system
2. **HL7 Message Rate**: Messages processed per minute
3. **Query Response Time**: Average response time
4. **System Uptime**: Availability percentage
5. **Department Efficiency**: Patient throughput per department

## 🎨 Dashboard Layout
```
┌─────────────────┬─────────────────┬─────────────────┐
│   Patient       │   System        │   Department    │
│   Overview      │   Performance   │   Analytics     │
├─────────────────┼─────────────────┼─────────────────┤
│   Real-time     │   HL7           │   Quality       │
│   Metrics       │   Processing    │   Indicators    │
└─────────────────┴─────────────────┴─────────────────┘
```

## 🔍 Monitoring
- **Health Check**: HTTP endpoint on port 3000
- **Logs**: Container logs via `docker logs grafana-dashboards`
- **Metrics**: Built-in Grafana monitoring
