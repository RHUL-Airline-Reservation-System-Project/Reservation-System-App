import React, { useState, useEffect } from 'react';
import { useParams, useLocation, useNavigate } from 'react-router-dom';
import { createBooking, getFlight } from '../services/api';
import { CLASS_PRICES } from '../utils/pricing';
import './BookingPage.css';

export default function BookingPage() {
  const { flightId }            = useParams();
  const { state }               = useLocation();
  const preflight               = state?.flight;
  const travelClass             = state?.travelClass || 'Economy';
  const navigate                = useNavigate();

  const [flight, setFlight]     = useState(preflight || null);
  const [loading, setLoading]   = useState(!preflight);
  const [error, setError]       = useState(null);

  const [name, setName]   = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');

  useEffect(() => {
    if (!flight) {
      getFlight(flightId)
        .then(res => {
          setFlight(res.data);
          setLoading(false);
        })
        .catch(() => {
          setError('Could not load flight details.');
          setLoading(false);
        });
    }
  }, [flight, flightId]);

  const fare = CLASS_PRICES[travelClass];

  const handleSubmit = e => {
    e.preventDefault();
    createBooking({ flightId, passenger: { name, email, phone }, travelClass, price: fare })
      .then(res => navigate(`/confirm/${res.data.id}`, { state: { travelClass } }))
      .catch(() => setError('Booking failed.'));
  };

  return (
    <div className="page-hero">
      <video className="page-video" src="/videos/booking-bg.mp4" autoPlay loop muted playsInline preload="auto"/>
      <div className="page-content">
        <div className="container card">
          <h2>Book Flight</h2>
          {loading && <p>Loading flight…</p>}
          {error   && <p className="error">{error}</p>}

          {!loading && !error && flight && (
            <>
              <p>
                <strong>{flight.airline} {flight.flightNumber}</strong><br/>
                {flight.origin} → {flight.dest} @ {flight.departureTime}<br/>
                Class: {travelClass}<br/>
                Price: ${fare}
              </p>
              <form onSubmit={handleSubmit} className="booking-form">
                <label>
                  Full Name
                  <input type="text" value={name} onChange={e => setName(e.target.value)} required/>
                </label>
                <label>
                  Email
                  <input type="email" value={email} onChange={e => setEmail(e.target.value)} required/>
                </label>
                <label>
                  Phone
                  <input type="tel" value={phone} onChange={e => setPhone(e.target.value)} required/>
                </label>
                <button type="submit" className="btn">Confirm Booking</button>
              </form>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
