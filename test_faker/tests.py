from faker import Faker
import requests
import httpx
import time
import asyncio
import datetime


fake = Faker()


def generate_fake_data():
    future_date = datetime.datetime.utcnow() + datetime.timedelta(days=fake.random_int(min=1, max=30))
    return {
        'passenger_name': fake.name(),
        'flight_number': fake.name(),
        'departure': fake.city(),
        'destination': fake.city(),
        'date': future_date.isoformat()
    }


def test_sync_backend(url, num_requests):
    start_time = time.time()
    
    for _ in range(num_requests):
        data = generate_fake_data()
        response = requests.post(url, json=data)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")

    elapsed_time = time.time() - start_time
    print(f"Sync backend: {elapsed_time:.2f} seconds")


async def test_async_backend(url, num_requests):
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        tasks = []
        for _ in range(num_requests):
            data = generate_fake_data()
            tasks.append(client.post(url, json=data))
        
        responses = await asyncio.gather(*tasks)
        for response in responses:
            if response.status_code != 200:
                print(f"Error: {response.status_code}")
    
    elapsed_time = time.time() - start_time
    print(f"Async backend: {elapsed_time:.2f} seconds")


num_requests = 200


sync_backend_url = 'http://localhost:8010/booking/'
async_backend_url = 'http://localhost:8000/booking/'


test_sync_backend(sync_backend_url, num_requests)
asyncio.run(test_async_backend(async_backend_url, num_requests))