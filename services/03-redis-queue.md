# Redis Message Queue Service

## 🎯 Service Overview
**Purpose**: Real-time message queuing and caching  
**Type**: Message broker and cache  
**Priority**: High (Integration service)

## 📋 Specifications
- **Version**: Redis 7.x
- **Image**: `redis:7-alpine`
- **Port**: 6379
- **Resources**: 
  - CPU: 0.5 cores
  - RAM: 1GB
  - Storage: 2GB

## 🔧 Configuration
```yaml
# docker-compose.yml
redis:
  image: redis:7-alpine
  container_name: redis-queue
  ports:
    - "6379:6379"
  volumes:
    - ./redis-data:/data
  command: redis-server --appendonly yes
  restart: unless-stopped
```

## 📊 Message Queues

### 1. HL7 Messages Queue
- **Queue Name**: `hl7_messages`
- **Message Types**: ADT, ORU, ORM
- **Processing Rate**: 50-100 messages/minute
- **Retention**: 24 hours

### 2. Analytics Queue
- **Queue Name**: `analytics_events`
- **Event Types**: Patient events, system metrics
- **Processing Rate**: 100-200 events/minute
- **Retention**: 7 days

### 3. Alerts Queue
- **Queue Name**: `alerts`
- **Alert Types**: Critical events, system warnings
- **Processing Rate**: 10-50 alerts/minute
- **Retention**: 30 days

## 🔄 Message Flow
```
HL7 Simulator → Redis Queue → IRIS Database → Grafana Dashboard
Mock Systems → Redis Queue → Analytics Engine → Grafana Dashboard
IRIS Database → Redis Queue → Alert System → Grafana Dashboard
```

## 📈 Performance Targets
- **Throughput**: 200 messages/minute
- **Latency**: <10ms for message processing
- **Memory Usage**: <500MB
- **Uptime**: 99% during demo

## 🛠️ Setup Commands
```bash
# Start Redis
docker-compose up -d redis

# Test Redis connection
docker exec -it redis-queue redis-cli ping

# Monitor Redis
docker exec -it redis-queue redis-cli monitor
```

## 📝 Key Features for Demo
1. **Message Queuing**: Reliable message delivery
2. **Caching**: Fast data access for dashboards
3. **Pub/Sub**: Real-time event broadcasting
4. **Persistence**: Message durability
5. **Monitoring**: Queue statistics

## 🔍 Monitoring
- **Health Check**: `redis-cli ping`
- **Logs**: Container logs via `docker logs redis-queue`
- **Metrics**: Redis INFO command
- **Queue Stats**: `redis-cli llen hl7_messages`

## 📊 Redis Commands for Demo
```bash
# Check queue length
redis-cli llen hl7_messages

# View recent messages
redis-cli lrange hl7_messages 0 10

# Monitor real-time activity
redis-cli monitor

# Check memory usage
redis-cli info memory
```
