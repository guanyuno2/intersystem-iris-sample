# Data Generator Service

## 🎯 Service Overview
**Purpose**: Generate realistic hospital data for demo  
**Type**: Data generation service  
**Priority**: Medium (Demo setup)

## 📋 Specifications
- **Technology**: Python 3.9+ with Faker
- **Dependencies**: `faker`, `pandas`, `sqlalchemy`
- **Resources**: 
  - CPU: 1 core
  - RAM: 2GB
  - Storage: 5GB

## 🔧 Configuration
```yaml
# docker-compose.yml
data-generator:
  build: ./data-generator
  container_name: data-generator
  depends_on: [iris]
  environment:
    - IRIS_HOST=iris
    - PATIENT_COUNT=1000
    - DOCTOR_COUNT=20
    - DEPARTMENT_COUNT=10
  volumes:
    - ./generated-data:/app/data
  restart: "no"
```

## 📊 Data Generation

### 1. Patient Data (1,000 records)
```python
def generate_patients(count=1000):
    patients = []
    for i in range(count):
        patient = {
            'id': f'P{i:06d}',
            'name': fake.name(),
            'dob': fake.date_of_birth(minimum_age=0, maximum_age=100),
            'gender': fake.random_element(elements=('M', 'F')),
            'address': fake.address(),
            'phone': fake.phone_number(),
            'insurance': fake.random_element(elements=('A', 'B', 'C')),
            'admission_date': fake.date_between(start_date='-2y', end_date='today')
        }
        patients.append(patient)
    return patients
```

### 2. Doctor Data (20 records)
```python
def generate_doctors(count=20):
    doctors = []
    specialties = ['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Surgery']
    for i in range(count):
        doctor = {
            'id': f'D{i:03d}',
            'name': fake.name(),
            'specialty': fake.random_element(elements=specialties),
            'department': fake.random_element(elements=departments),
            'license': fake.random_number(digits=8),
            'phone': fake.phone_number()
        }
        doctors.append(doctor)
    return doctors
```

### 3. Department Data (10 records)
```python
def generate_departments():
    departments = [
        {'id': 'DEPT001', 'name': 'Emergency', 'beds': 20, 'location': '1F'},
        {'id': 'DEPT002', 'name': 'Cardiology', 'beds': 15, 'location': '2F'},
        {'id': 'DEPT003', 'name': 'Neurology', 'beds': 12, 'location': '3F'},
        {'id': 'DEPT004', 'name': 'Orthopedics', 'beds': 18, 'location': '4F'},
        {'id': 'DEPT005', 'name': 'Pediatrics', 'beds': 25, 'location': '5F'},
        {'id': 'DEPT006', 'name': 'Surgery', 'beds': 8, 'location': '6F'},
        {'id': 'DEPT007', 'name': 'ICU', 'beds': 10, 'location': '7F'},
        {'id': 'DEPT008', 'name': 'Laboratory', 'beds': 0, 'location': 'B1'},
        {'id': 'DEPT009', 'name': 'Radiology', 'beds': 0, 'location': 'B2'},
        {'id': 'DEPT010', 'name': 'Pharmacy', 'beds': 0, 'location': 'B3'}
    ]
    return departments
```

## 📈 Data Volume
- **Patients**: 1,000 records (reduced from 10,000)
- **Doctors**: 20 records
- **Departments**: 10 records
- **Appointments**: 500 records (2 years history)
- **Lab Tests**: 2,000 records
- **Medications**: 100 records

## 🛠️ Setup Commands
```bash
# Generate all data
docker-compose run --rm data-generator python generate_all_data.py

# Generate specific data
docker-compose run --rm data-generator python generate_patients.py
docker-compose run --rm data-generator python generate_doctors.py
docker-compose run --rm data-generator python generate_appointments.py

# Verify data generation
docker-compose run --rm data-generator python verify_data.py
```

## 📝 Key Features for Demo
1. **Realistic Data**: Vietnamese names, addresses, phone numbers
2. **Historical Data**: 2 years of patient history
3. **Relationships**: Proper foreign key relationships
4. **Data Quality**: Validated data formats
5. **Export Options**: CSV, JSON, SQL formats

## 🔍 Data Validation
```python
def validate_data():
    # Check patient data
    assert len(patients) == 1000
    assert all(p['id'].startswith('P') for p in patients)
    
    # Check doctor data
    assert len(doctors) == 20
    assert all(d['id'].startswith('D') for d in doctors)
    
    # Check department data
    assert len(departments) == 10
    assert all(d['id'].startswith('DEPT') for d in departments)
```

## 📊 Generated Files
- `patients.csv` - Patient records
- `doctors.csv` - Doctor records
- `departments.csv` - Department records
- `appointments.csv` - Appointment history
- `lab_tests.csv` - Laboratory test records
- `medications.csv` - Medication inventory

## 🎯 Success Metrics
- **Data Generation**: 1,000+ records in 5 minutes
- **Data Quality**: 100% valid records
- **File Size**: <50MB total
- **Generation Time**: <10 minutes
