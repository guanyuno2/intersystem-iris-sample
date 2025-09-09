# Performance Monitoring Service

## 🎯 Service Overview
**Purpose**: Monitor system performance and generate metrics  
**Type**: Monitoring service  
**Priority**: Medium (Demo enhancement)

## 📋 Specifications
- **Technology**: Python 3.9+ with Prometheus client
- **Dependencies**: `prometheus_client`, `psutil`, `redis`, `requests`
- **Resources**: 
  - CPU: 0.5 cores
  - RAM: 1GB
  - Storage: 2GB

## 🔧 Configuration
```yaml
# docker-compose.yml
monitoring:
  build: ./monitoring
  container_name: performance-monitoring
  ports: ["9090:9090"]
  depends_on: [iris, redis, grafana]
  environment:
    - IRIS_HOST=iris
    - REDIS_HOST=redis
    - GRAFANA_HOST=grafana
  restart: unless-stopped
```

## 📊 Monitoring Metrics

### 1. System Performance
```python
# CPU usage
cpu_usage = psutil.cpu_percent(interval=1)

# Memory usage
memory = psutil.virtual_memory()
memory_usage = memory.percent

# Disk usage
disk = psutil.disk_usage('/')
disk_usage = (disk.used / disk.total) * 100

# Network I/O
network = psutil.net_io_counters()
network_bytes_sent = network.bytes_sent
network_bytes_recv = network.bytes_recv
```

### 2. IRIS Database Metrics
```python
# Database connections
db_connections = get_iris_connections()

# Query performance
query_response_time = get_avg_query_time()

# HL7 message processing
hl7_messages_processed = get_hl7_message_count()
hl7_processing_rate = get_hl7_processing_rate()

# Database size
db_size = get_database_size()
```

### 3. Application Metrics
```python
# API response times
api_response_time = get_api_response_time()

# Error rates
error_rate = get_error_rate()

# Active users
active_users = get_active_user_count()

# Cache hit rate
cache_hit_rate = get_cache_hit_rate()
```

## 📈 Performance Targets

### 1. System Performance
- **CPU Usage**: <80%
- **Memory Usage**: <85%
- **Disk Usage**: <90%
- **Network Latency**: <100ms

### 2. Database Performance
- **Query Response Time**: <500ms
- **HL7 Processing Rate**: 50+ messages/minute
- **Connection Pool**: <80% utilization
- **Database Size**: <1GB

### 3. Application Performance
- **API Response Time**: <200ms
- **Error Rate**: <2%
- **Cache Hit Rate**: >80%
- **Uptime**: >99%

## 🛠️ Setup Commands
```bash
# Start monitoring service
docker-compose up -d monitoring

# View metrics
curl http://localhost:9090/metrics

# Test monitoring
docker exec -it performance-monitoring python test_monitoring.py
```

## 📝 Key Features for Demo
1. **Real-time Metrics**: Live performance data
2. **Historical Data**: Performance trends over time
3. **Alert Integration**: Performance-based alerts
4. **Dashboard Integration**: Metrics for Grafana
5. **Export Options**: CSV, JSON data export

## 🔍 Monitoring Endpoints

### 1. Prometheus Metrics
- **URL**: `http://localhost:9090/metrics`
- **Format**: Prometheus text format
- **Update Frequency**: Every 10 seconds

### 2. Health Check
- **URL**: `http://localhost:9090/health`
- **Response**: JSON health status
- **Check Frequency**: Every 30 seconds

### 3. Performance Summary
- **URL**: `http://localhost:9090/summary`
- **Response**: JSON performance summary
- **Update Frequency**: Every minute

## 📊 Demo Scenarios

### Scenario 1: Normal Operations
1. Monitor system performance
2. Display real-time metrics
3. Show performance trends
4. Demonstrate stability

### Scenario 2: High Load
1. Simulate high system load
2. Monitor performance degradation
3. Show alert generation
4. Demonstrate recovery

### Scenario 3: Performance Comparison
1. Compare IRIS vs traditional systems
2. Show performance improvements
3. Display efficiency gains
4. Demonstrate scalability

## 🎯 Success Metrics
- **Monitoring Coverage**: 100% of critical metrics
- **Data Accuracy**: 99.9% accurate measurements
- **Update Frequency**: 10-second intervals
- **Uptime**: 99% during demo
