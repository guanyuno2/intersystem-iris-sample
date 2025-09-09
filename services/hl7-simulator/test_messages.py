#!/usr/bin/env python3
"""
Test script for HL7 Message Simulator
"""

import asyncio
import json
import requests
import time

# Configuration
BASE_URL = "http://localhost:8080"

def test_health():
    """Test health endpoint"""
    print("Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Health check: {response.status_code} - {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_message_generation():
    """Test message generation"""
    print("\nTesting message generation...")
    try:
        response = requests.get(f"{BASE_URL}/test")
        messages = response.json()
        
        print(f"Generated {len(messages)} test messages:")
        for msg_type, content in messages.items():
            print(f"\n{msg_type}:")
            print(content[:200] + "..." if len(content) > 200 else content)
        
        return True
    except Exception as e:
        print(f"Message generation test failed: {e}")
        return False

def test_simulation():
    """Test simulation start/stop"""
    print("\nTesting simulation...")
    
    # Start simulation
    config = {
        "message_rate": 10,  # 10 messages per minute for testing
        "duration": 60,      # 1 minute test
        "patient_count": 10,
        "department_count": 3,
        "doctor_count": 5
    }
    
    try:
        # Start simulation
        print("Starting simulation...")
        response = requests.post(f"{BASE_URL}/start", json=config)
        print(f"Start response: {response.status_code} - {response.json()}")
        
        if response.status_code == 200:
            # Wait a bit
            print("Waiting 30 seconds...")
            time.sleep(30)
            
            # Check status
            print("Checking status...")
            response = requests.get(f"{BASE_URL}/status")
            status = response.json()
            print(f"Status: {status}")
            
            # Stop simulation
            print("Stopping simulation...")
            response = requests.post(f"{BASE_URL}/stop")
            print(f"Stop response: {response.status_code} - {response.json()}")
            
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Simulation test failed: {e}")
        return False

def test_recent_messages():
    """Test getting recent messages"""
    print("\nTesting recent messages...")
    try:
        response = requests.get(f"{BASE_URL}/messages?limit=5")
        messages = response.json()
        
        print(f"Retrieved {len(messages)} recent messages:")
        for i, msg in enumerate(messages):
            print(f"\nMessage {i+1}:")
            print(f"  Type: {msg.get('message_type', 'Unknown')}")
            print(f"  Timestamp: {msg.get('timestamp', 'Unknown')}")
            print(f"  Status: {msg.get('status', 'Unknown')}")
            print(f"  Content: {msg.get('content', '')[:100]}...")
        
        return True
    except Exception as e:
        print(f"Recent messages test failed: {e}")
        return False

async def main():
    """Run all tests"""
    print("HL7 Message Simulator - Test Suite")
    print("=" * 50)
    
    tests = [
        ("Health Check", test_health),
        ("Message Generation", test_message_generation),
        ("Simulation", test_simulation),
        ("Recent Messages", test_recent_messages)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            result = test_func()
            results.append((test_name, result))
            print(f"✅ {test_name}: {'PASSED' if result else 'FAILED'}")
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {e}")
            results.append((test_name, False))
    
    # Summary
    print(f"\n{'='*50}")
    print("TEST SUMMARY")
    print(f"{'='*50}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
    else:
        print("⚠️  Some tests failed. Check the logs above.")

if __name__ == "__main__":
    asyncio.run(main())
