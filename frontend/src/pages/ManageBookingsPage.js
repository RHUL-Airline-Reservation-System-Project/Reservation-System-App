// src/pages/ManageBookingsPage.js
import React, { useEffect, useState } from 'react';
import './ManageBookingsPage.css';
import { getUserBookings } from '../services/api'; // if ready, otherwise stub

export default function ManageBookingsPage() {
  const [bookings, setBookings] = useState([]);
  const [loading, setLoading]   = useState(true);
  const [error, setError]       = useState(null);

  useEffect(() => {
    // real API call (uncomment when endpoint exists):
    // getUserBookings()
    //   .then(res => { setBookings(res.data); setLoading(false); })
    //   .catch(() => { setError('Could not load your bookings.'); setLoading(false); });

    // stubbed fetch:
    setTimeout(() => {
      setBookings([]);    // replace [] with real data later
      setLoading(false);
    }, 500);
  }, []);

  return (
    <div className="page-hero">
      {/* use a clip you already have */}
      <video
        className="page-video"
        src="/videos/booking-bg.mp4"
        autoPlay
        loop
        muted
        playsInline
        preload="auto"
      />

      <div className="page-content">
        <div className="container">
          <div className="card">
            <h2>My Bookings</h2>
            {loading && <p>Loading your bookings…</p>}
            {error   && <p className="error">{error}</p>}
            {!loading && !error && (
              bookings.length === 0
                ? <p>You have no bookings yet.</p>
                : (
                  <ul className="booking-list">
                    {bookings.map(b => (
                      <li key={b.id} className="booking-item">
                        <strong>{b.flight.airline}</strong> {b.flight.flightNumber} |{' '}
                        {b.flight.origin} → {b.flight.dest} on {b.flight.departureTime}
                      </li>
                    ))}
                  </ul>
                )
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
