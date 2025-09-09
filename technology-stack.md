## 🏗️ Demo Architecture & Technology Stack

### **System Architecture:**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   HL7 Simulator │────┤ InterSystems    │────┤   Grafana       │
│   (Patient Data)│    │      IRIS       │    │   Dashboards    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Mock Hospital  │────┤  Message Queue  │────┤  Real-time      │
│    Systems      │    │   (Redis)       │    │   Alerts        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### **Technology Stack:**
- **Core Platform**: InterSystems IRIS 2024
- **Integration**: HL7 FHIR R4, Custom HL7 v2.x messages
- **Visualization**: Grafana 10.x with advanced panels
- **Data Simulation**: Python scripts generating realistic hospital data
- **Real-time Processing**: IRIS Integration Engine
- **Analytics**: IRIS SQL + MDX queries

---