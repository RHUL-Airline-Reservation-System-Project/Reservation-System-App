import React, { useEffect, useState } from 'react';
import { useLocation, Link } from 'react-router-dom';
import { CLASS_PRICES } from '../utils/pricing';
import { searchFlights } from '../services/api';
import './ResultsPage.css';

export default function ResultsPage() {
  const { state } = useLocation();
  const { origin, dest, date, travelClass } = state || {};
  const [flights, setFlights] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(null);

  useEffect(() => {
    if (!origin || !dest || !date) {
      setError('Missing search parameters.');
      setLoading(false);
      return;
    }
    searchFlights({ origin, dest, date })
      .then(res => {
        setFlights(res.data);
        setLoading(false);
      })
      .catch(() => {
        setError('Error fetching flights.');
        setLoading(false);
      });
  }, [origin, dest, date]);

  const fare = CLASS_PRICES[travelClass];

  return (
    <div className="page-hero">
      <video className="page-video" src="/videos/results-bg.mp4" autoPlay loop muted playsInline preload="auto"/>
      <div className="page-content">
        <div className="container card">
          <h2>Available Flights</h2>
          {loading && <p>Loading flights…</p>}
          {error   && <p className="error">{error}</p>}

          {!loading && !error && (
            flights.length === 0
              ? <p>No flights found for {origin} → {dest} on {date}.</p>
              : (
                <ul className="flight-list">
                  {flights.map(f => (
                    <li key={f.id} className="flight-item">
                      <div>
                        <strong>{f.airline}</strong> {f.flightNumber}<br/>
                        {f.origin} → {f.dest} @ {f.departureTime}
                      </div>
                      <div>
                        <span>${fare}</span>{' '}
                        <Link
                          to={`/book/${f.id}`}
                          state={{ flight: f, travelClass }}
                          className="btn small"
                        >
                          Book
                        </Link>
                      </div>
                    </li>
                  ))}
                </ul>
              )
          )}
        </div>
      </div>
    </div>
  );
}
