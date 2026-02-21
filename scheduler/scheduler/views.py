from django.shortcuts import render
from .models import Flight
import json
import random

def generate_simulated_flights(num_flights=15):
    """Generate simulated flight data for the simulation."""
    airlines = ['AA', 'UA', 'DL', 'SW', 'BA', 'AF', 'LH', 'KL']
    airports = ['JFK', 'LAX', 'ORD', 'DFW', 'ATL', 'DEN', 'SFO', 'LAS', 'MIA', 'BOS']
    
    simulated_flights = []
    for i in range(num_flights):
        flight_num = f"{random.choice(airlines)}{random.randint(100, 9999)}"
        origin = random.choice(airports)
        destination = random.choice([a for a in airports if a != origin])
        duration_hours = random.uniform(1, 12)
        
        simulated_flights.append({
            'flight_number': flight_num,
            'origin': origin,
            'destination': destination,
            'duration': round(duration_hours, 2)
        })
    
    return simulated_flights

def dashboard(request):
    flights = generate_simulated_flights(num_flights=15)

    labels = []
    durations = []

    for f in flights:
        labels.append(f['flight_number'])
        durations.append(f['duration'])

    context = {
        "labels": json.dumps(labels),
        "durations": json.dumps(durations),
    }

    return render(request, "dashboard.html", context)