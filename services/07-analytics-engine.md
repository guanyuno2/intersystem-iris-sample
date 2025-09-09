# Analytics Engine Service

## 🎯 Service Overview
**Purpose**: Process complex analytics queries and provide real-time insights  
**Type**: Analytics processing service  
**Priority**: High (Core functionality)

## 📋 Specifications
- **Technology**: Python 3.9+ with SQLAlchemy
- **Dependencies**: `sqlalchemy`, `pandas`, `numpy`, `redis`
- **Resources**: 
  - CPU: 1 core
  - RAM: 2GB
  - Storage: 2GB

## 🔧 Configuration
```yaml
# docker-compose.yml
analytics:
  build: ./analytics
  container_name: analytics-engine
  depends_on: [iris, redis, grafana]
  environment:
    - IRIS_HOST=iris
    - REDIS_HOST=redis
    - GRAFANA_HOST=grafana
  restart: unless-stopped
```

## 📊 Analytics Queries

### 1. Real-time Hospital KPIs
```sql
-- Current patient count
SELECT COUNT(*) as CurrentPatients
FROM PatientAdmissions 
WHERE DischargeDate IS NULL

-- Average length of stay
SELECT AVG(DATEDIFF(day, AdmissionDate, COALESCE(DischargeDate, GETDATE()))) as AvgLOS
FROM PatientAdmissions

-- Daily revenue
SELECT SUM(TotalCost) as DailyRevenue
FROM PatientBilling 
WHERE BillingDate = CURRENT_DATE

-- Active doctors
SELECT COUNT(DISTINCT DoctorID) as ActiveDoctors
FROM PatientAdmissions 
WHERE DischargeDate IS NULL
```

### 2. Department Performance
```sql
-- Department efficiency
SELECT 
    d.DepartmentName,
    COUNT(p.PatientID) as PatientCount,
    AVG(p.LengthOfStay) as AvgLOS,
    SUM(p.TotalCost) as TotalRevenue
FROM Departments d
LEFT JOIN PatientAdmissions p ON d.DepartmentID = p.DepartmentID
WHERE p.AdmissionDate >= DATEADD(day, -30, GETDATE())
GROUP BY d.DepartmentName
ORDER BY PatientCount DESC
```

### 3. Predictive Analytics
```sql
-- Patient volume forecast
SELECT 
    Department,
    AVG(PatientCount) as AvgVolume,
    AVG(PatientCount) * 1.1 as PredictedVolume
FROM DailyPatientCounts
WHERE Date >= DATEADD(day, -30, GETDATE())
GROUP BY Department
```

## 📈 Performance Metrics

### 1. System Performance
- **Query Response Time**: <500ms for simple queries
- **Complex Analytics**: <2 seconds
- **Real-time Updates**: Every 10 seconds
- **Concurrent Queries**: 10-20 simultaneous

### 2. Data Processing
- **Patient Data**: 1,000 records processed
- **Historical Data**: 2 years of data
- **Update Frequency**: Real-time
- **Cache Hit Rate**: 80%+

## 🛠️ Setup Commands
```bash
# Start analytics engine
docker-compose up -d analytics

# Test analytics queries
docker exec -it analytics-engine python test_queries.py

# View analytics logs
docker logs -f analytics-engine
```

## 📝 Key Features for Demo
1. **Real-time Processing**: Live data analysis
2. **Complex Queries**: Multi-table joins and aggregations
3. **Performance Optimization**: Query caching and indexing
4. **Data Visualization**: Prepared data for Grafana
5. **Error Handling**: Robust error recovery

## 🔍 Monitoring
- **Health Check**: HTTP endpoint on port 8080
- **Logs**: Container logs via `docker logs analytics-engine`
- **Metrics**: Query performance, cache hit rate
- **Alerts**: Slow query notifications

## 📊 Demo Scenarios

### Scenario 1: Real-time Dashboard
1. Process current patient data
2. Calculate key performance indicators
3. Update Grafana dashboards
4. Show live data updates

### Scenario 2: Department Analysis
1. Analyze department performance
2. Compare efficiency metrics
3. Generate performance reports
4. Display trends and insights

### Scenario 3: Predictive Analytics
1. Analyze historical data
2. Generate forecasts
3. Identify trends
4. Provide recommendations

## 🎯 Success Metrics
- **Query Performance**: <500ms average
- **Data Accuracy**: 99.9% correct results
- **Real-time Updates**: 10-second intervals
- **Uptime**: 99% during demo
