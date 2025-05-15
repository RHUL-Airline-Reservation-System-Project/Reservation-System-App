// src/services/api.js
import Papa from 'papaparse';

/**
 * Search for flights in your CSV.
 * Filters by exact match on origin, destination, and date (YYYY-MM-DD).
 */
export function searchFlights({ origin, dest, date }) {
  return new Promise((resolve, reject) => {
    Papa.parse(
      `${process.env.PUBLIC_URL}/data/real_flights_dataset.csv`,
      {
        download: true,
        header: true,
        skipEmptyLines: true,
        complete: ({ data }) => {
          // filter rows that match origin, destination and departure date
          const matched = data.filter(row =>
            row.origin === origin &&
            row.destination === dest &&
            row.scheduled_departure.startsWith(date)
          );

          // map into the shape your ResultsPage expects
          const flights = matched.map(row => ({
            id: row.flight_number,
            airline: 'Royal Flights',
            flightNumber: row.flight_number,
            origin: row.origin,
            dest: row.destination,
            departureTime: row.scheduled_departure,
            price: 100  // placeholder price—tweak as desired
          }));

          resolve({ data: flights });
        },
        error: err => {
          console.error('CSV parse error:', err);
          reject(err);
        }
      }
    );
  });
}

// fallback stubs so other pages keep working
export function getFlight(id) {
  return Promise.resolve({
    data: {
      id,
      airline: 'Royal Flights',
      flightNumber: id,
      origin: 'LHR',
      dest: 'JFK',
      departureTime: '2025-06-01T08:00:00Z',
      price: 100
    }
  });
}

export function createBooking(data) {
  return Promise.resolve({ data: { id: 'BOOK123' } });
}

export function getBooking(id) {
  return Promise.resolve({
    data: {
      id,
      flight: {
        airline: 'Royal Flights',
        flightNumber: 'RF101',
        origin: 'LHR',
        dest: 'JFK',
        departureTime: '2025-06-01T08:00:00Z'
      },
      passenger: { name: 'John Doe', email: 'john@ex.com', phone: '555-5555' },
      price: 100
    
    }
  });
}

export function getUserBookings() {
  return Promise.resolve({ data: [] });
}

export function fetchInfoHub() {
  return Promise.resolve({ data: [] });
}

export function checkIn(bookingId, payload) {
  return Promise.resolve({ data: { status: 'checked-in' } });
}

export function fetchUserProfile(userId) {
  return Promise.resolve({
    data: { id: userId, name: 'John Doe', email: 'john@ex.com', joined: '2024-09-01' }
  });
}

export function fetchBenefits() {
  return Promise.resolve({ data: [] });
}
