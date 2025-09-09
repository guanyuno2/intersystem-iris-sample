#!/usr/bin/env python3
"""
Hospital Data Generator Service
Generates realistic hospital data for demo
"""

import csv
import json
import logging
import os
import random
from datetime import datetime, timedelta
from typing import Dict, List

import pandas as pd
from faker import Faker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
PATIENT_COUNT = int(os.getenv('PATIENT_COUNT', '1000'))
DOCTOR_COUNT = int(os.getenv('DOCTOR_COUNT', '20'))
DEPARTMENT_COUNT = int(os.getenv('DEPARTMENT_COUNT', '10'))

# Initialize Faker with Vietnamese locale
fake = Faker('vi_VN')

class HospitalDataGenerator:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.departments = []
        self.appointments = []
        self.lab_tests = []
        self.medications = []
        
    def generate_departments(self) -> List[Dict]:
        """Generate department data"""
        logger.info("Generating departments...")
        
        departments = [
            {'id': 'DEPT001', 'name': 'Emergency', 'beds': 20, 'location': '1F', 'phone': '01-234-5678'},
            {'id': 'DEPT002', 'name': 'Cardiology', 'beds': 15, 'location': '2F', 'phone': '01-234-5679'},
            {'id': 'DEPT003', 'name': 'Neurology', 'beds': 12, 'location': '3F', 'phone': '01-234-5680'},
            {'id': 'DEPT004', 'name': 'Orthopedics', 'beds': 18, 'location': '4F', 'phone': '01-234-5681'},
            {'id': 'DEPT005', 'name': 'Pediatrics', 'beds': 25, 'location': '5F', 'phone': '01-234-5682'},
            {'id': 'DEPT006', 'name': 'Surgery', 'beds': 8, 'location': '6F', 'phone': '01-234-5683'},
            {'id': 'DEPT007', 'name': 'ICU', 'beds': 10, 'location': '7F', 'phone': '01-234-5684'},
            {'id': 'DEPT008', 'name': 'Laboratory', 'beds': 0, 'location': 'B1', 'phone': '01-234-5685'},
            {'id': 'DEPT009', 'name': 'Radiology', 'beds': 0, 'location': 'B2', 'phone': '01-234-5686'},
            {'id': 'DEPT010', 'name': 'Pharmacy', 'beds': 0, 'location': 'B3', 'phone': '01-234-5687'}
        ]
        
        self.departments = departments
        logger.info(f"Generated {len(departments)} departments")
        return departments
    
    def generate_doctors(self) -> List[Dict]:
        """Generate doctor data"""
        logger.info("Generating doctors...")
        
        specialties = [
            'Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Surgery',
            'Emergency Medicine', 'Internal Medicine', 'Anesthesiology', 'Radiology', 'Pathology'
        ]
        
        doctors = []
        for i in range(DOCTOR_COUNT):
            doctor = {
                'id': f'D{i:03d}',
                'name': fake.name(),
                'specialty': random.choice(specialties),
                'department': random.choice(self.departments)['id'],
                'license': fake.random_number(digits=8),
                'phone': fake.phone_number(),
                'email': fake.email(),
                'experience_years': random.randint(1, 30),
                'education': random.choice(['MD', 'DO', 'MBBS']),
                'certification': random.choice(['Board Certified', 'Fellowship', 'Residency'])
            }
            doctors.append(doctor)
        
        self.doctors = doctors
        logger.info(f"Generated {len(doctors)} doctors")
        return doctors
    
    def generate_patients(self) -> List[Dict]:
        """Generate patient data"""
        logger.info("Generating patients...")
        
        patients = []
        for i in range(PATIENT_COUNT):
            # Generate realistic Vietnamese names and addresses
            name = fake.name()
            dob = fake.date_of_birth(minimum_age=0, maximum_age=100)
            gender = random.choice(['M', 'F'])
            
            # Generate Vietnamese address
            address_parts = [
                fake.street_address(),
                fake.city(),
                fake.state(),
                'Vietnam'
            ]
            address = ', '.join(address_parts)
            
            patient = {
                'id': f'P{i:06d}',
                'name': name,
                'dob': dob.strftime('%Y-%m-%d'),
                'gender': gender,
                'address': address,
                'phone': fake.phone_number(),
                'email': fake.email(),
                'insurance_type': random.choice(['A', 'B', 'C', 'D']),
                'insurance_number': fake.random_number(digits=10),
                'emergency_contact': fake.name(),
                'emergency_phone': fake.phone_number(),
                'admission_date': fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d'),
                'discharge_date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d') if random.random() > 0.3 else None,
                'status': random.choice(['Active', 'Discharged', 'Transferred']),
                'primary_diagnosis': random.choice([
                    'Hypertension', 'Diabetes', 'Pneumonia', 'Fracture', 'Heart Disease',
                    'Stroke', 'Cancer', 'Infection', 'Trauma', 'Respiratory Disease'
                ])
            }
            patients.append(patient)
        
        self.patients = patients
        logger.info(f"Generated {len(patients)} patients")
        return patients
    
    def generate_appointments(self) -> List[Dict]:
        """Generate appointment data"""
        logger.info("Generating appointments...")
        
        appointments = []
        appointment_types = ['Consultation', 'Follow-up', 'Emergency', 'Surgery', 'Check-up']
        
        # Generate 2 years of appointment history
        start_date = datetime.now() - timedelta(days=730)
        end_date = datetime.now()
        
        for i in range(500):  # 500 appointments over 2 years
            appointment = {
                'id': f'APT{i:06d}',
                'patient_id': random.choice(self.patients)['id'],
                'doctor_id': random.choice(self.doctors)['id'],
                'department_id': random.choice(self.departments)['id'],
                'appointment_date': fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d'),
                'appointment_time': fake.time(),
                'appointment_type': random.choice(appointment_types),
                'status': random.choice(['Scheduled', 'Completed', 'Cancelled', 'No-show']),
                'notes': fake.text(max_nb_chars=200),
                'duration_minutes': random.choice([30, 45, 60, 90, 120]),
                'room_number': f"R{random.randint(100, 999)}"
            }
            appointments.append(appointment)
        
        self.appointments = appointments
        logger.info(f"Generated {len(appointments)} appointments")
        return appointments
    
    def generate_lab_tests(self) -> List[Dict]:
        """Generate laboratory test data"""
        logger.info("Generating lab tests...")
        
        test_types = [
            {'code': 'CBC', 'name': 'Complete Blood Count', 'normal_range': '4.5-11.0', 'units': 'K/uL'},
            {'code': 'CHEM7', 'name': 'Basic Metabolic Panel', 'normal_range': '70-100', 'units': 'mg/dL'},
            {'code': 'LIPID', 'name': 'Lipid Panel', 'normal_range': '<200', 'units': 'mg/dL'},
            {'code': 'GLUCOSE', 'name': 'Blood Glucose', 'normal_range': '70-100', 'units': 'mg/dL'},
            {'code': 'BUN', 'name': 'Blood Urea Nitrogen', 'normal_range': '7-20', 'units': 'mg/dL'},
            {'code': 'CREATININE', 'name': 'Creatinine', 'normal_range': '0.6-1.2', 'units': 'mg/dL'},
            {'code': 'TSH', 'name': 'Thyroid Stimulating Hormone', 'normal_range': '0.4-4.0', 'units': 'mIU/L'},
            {'code': 'HBA1C', 'name': 'Hemoglobin A1C', 'normal_range': '<5.7', 'units': '%'}
        ]
        
        lab_tests = []
        for i in range(2000):  # 2000 lab tests
            test_type = random.choice(test_types)
            patient = random.choice(self.patients)
            doctor = random.choice(self.doctors)
            
            # Generate realistic test result
            if test_type['code'] == 'CBC':
                result_value = round(random.uniform(4.0, 12.0), 1)
            elif test_type['code'] == 'GLUCOSE':
                result_value = round(random.uniform(60, 150), 1)
            elif test_type['code'] == 'LIPID':
                result_value = round(random.uniform(120, 300), 1)
            else:
                result_value = round(random.uniform(0.1, 10.0), 2)
            
            lab_test = {
                'id': f'LAB{i:06d}',
                'patient_id': patient['id'],
                'doctor_id': doctor['id'],
                'test_code': test_type['code'],
                'test_name': test_type['name'],
                'result_value': result_value,
                'normal_range': test_type['normal_range'],
                'units': test_type['units'],
                'test_date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
                'status': random.choice(['Completed', 'Pending', 'Cancelled']),
                'notes': fake.text(max_nb_chars=100)
            }
            lab_tests.append(lab_test)
        
        self.lab_tests = lab_tests
        logger.info(f"Generated {len(lab_tests)} lab tests")
        return lab_tests
    
    def generate_medications(self) -> List[Dict]:
        """Generate medication data"""
        logger.info("Generating medications...")
        
        medications = [
            {'name': 'Aspirin', 'generic_name': 'Acetylsalicylic Acid', 'category': 'NSAID', 'dosage': '81mg'},
            {'name': 'Metformin', 'generic_name': 'Metformin HCl', 'category': 'Antidiabetic', 'dosage': '500mg'},
            {'name': 'Lisinopril', 'generic_name': 'Lisinopril', 'category': 'ACE Inhibitor', 'dosage': '10mg'},
            {'name': 'Atorvastatin', 'generic_name': 'Atorvastatin Calcium', 'category': 'Statin', 'dosage': '20mg'},
            {'name': 'Omeprazole', 'generic_name': 'Omeprazole', 'category': 'PPI', 'dosage': '20mg'},
            {'name': 'Amlodipine', 'generic_name': 'Amlodipine Besylate', 'category': 'CCB', 'dosage': '5mg'},
            {'name': 'Metoprolol', 'generic_name': 'Metoprolol Succinate', 'category': 'Beta Blocker', 'dosage': '50mg'},
            {'name': 'Losartan', 'generic_name': 'Losartan Potassium', 'category': 'ARB', 'dosage': '50mg'},
            {'name': 'Simvastatin', 'generic_name': 'Simvastatin', 'category': 'Statin', 'dosage': '40mg'},
            {'name': 'Hydrochlorothiazide', 'generic_name': 'HCTZ', 'category': 'Diuretic', 'dosage': '25mg'}
        ]
        
        self.medications = medications
        logger.info(f"Generated {len(medications)} medications")
        return medications
    
    def save_to_csv(self, data: List[Dict], filename: str):
        """Save data to CSV file"""
        if not data:
            logger.warning(f"No data to save for {filename}")
            return
        
        filepath = f"/app/data/{filename}"
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
        logger.info(f"Saved {len(data)} records to {filepath}")
    
    def save_to_json(self, data: List[Dict], filename: str):
        """Save data to JSON file"""
        if not data:
            logger.warning(f"No data to save for {filename}")
            return
        
        filepath = f"/app/data/{filename}"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        logger.info(f"Saved {len(data)} records to {filepath}")
    
    def generate_all_data(self):
        """Generate all hospital data"""
        logger.info("Starting hospital data generation...")
        
        # Generate all data
        self.generate_departments()
        self.generate_doctors()
        self.generate_patients()
        self.generate_appointments()
        self.generate_lab_tests()
        self.generate_medications()
        
        # Save to CSV files
        self.save_to_csv(self.departments, 'departments.csv')
        self.save_to_csv(self.doctors, 'doctors.csv')
        self.save_to_csv(self.patients, 'patients.csv')
        self.save_to_csv(self.appointments, 'appointments.csv')
        self.save_to_csv(self.lab_tests, 'lab_tests.csv')
        self.save_to_csv(self.medications, 'medications.csv')
        
        # Save to JSON files
        self.save_to_json(self.departments, 'departments.json')
        self.save_to_json(self.doctors, 'doctors.json')
        self.save_to_json(self.patients, 'patients.json')
        self.save_to_json(self.appointments, 'appointments.json')
        self.save_to_json(self.lab_tests, 'lab_tests.json')
        self.save_to_json(self.medications, 'medications.json')
        
        # Generate summary
        summary = {
            'generation_date': datetime.now().isoformat(),
            'total_records': {
                'departments': len(self.departments),
                'doctors': len(self.doctors),
                'patients': len(self.patients),
                'appointments': len(self.appointments),
                'lab_tests': len(self.lab_tests),
                'medications': len(self.medications)
            },
            'total_size_mb': self.calculate_total_size()
        }
        
        self.save_to_json([summary], 'generation_summary.json')
        
        logger.info("Hospital data generation completed!")
        logger.info(f"Generated {sum(summary['total_records'].values())} total records")
        
        return summary
    
    def calculate_total_size(self) -> float:
        """Calculate total size of generated data in MB"""
        total_size = 0
        for filename in ['departments.csv', 'doctors.csv', 'patients.csv', 
                        'appointments.csv', 'lab_tests.csv', 'medications.csv']:
            filepath = f"/app/data/{filename}"
            if os.path.exists(filepath):
                total_size += os.path.getsize(filepath)
        return round(total_size / (1024 * 1024), 2)

def main():
    """Main function"""
    logger.info("Hospital Data Generator Service")
    logger.info("=" * 50)
    
    generator = HospitalDataGenerator()
    summary = generator.generate_all_data()
    
    print("\n" + "=" * 50)
    print("GENERATION SUMMARY")
    print("=" * 50)
    print(f"Generation Date: {summary['generation_date']}")
    print(f"Total Records: {sum(summary['total_records'].values())}")
    print(f"Total Size: {summary['total_size_mb']} MB")
    print("\nRecord Counts:")
    for table, count in summary['total_records'].items():
        print(f"  {table}: {count:,}")
    
    print("\nFiles generated in /app/data/:")
    print("  - departments.csv/json")
    print("  - doctors.csv/json")
    print("  - patients.csv/json")
    print("  - appointments.csv/json")
    print("  - lab_tests.csv/json")
    print("  - medications.csv/json")
    print("  - generation_summary.json")

if __name__ == "__main__":
    main()
