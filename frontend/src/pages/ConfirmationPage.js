import React, { useEffect, useState } from 'react';
import { useParams, Link, useLocation } from 'react-router-dom';
import { getBooking } from '../services/api';
import './ConfirmationPage.css';

export default function ConfirmationPage() {
  const { bookingId } = useParams();
  const { state }     = useLocation();
  const travelClass   = state?.travelClass;
  const [booking, setBooking]   = useState(null);
  const [loading, setLoading]   = useState(true);
  const [error , setError ]     = useState(null);

  useEffect(() => {
    getBooking(bookingId)
      .then(res => {
        setBooking(res.data);
        setLoading(false);
      })
      .catch(() => {
        setError('Could not load booking details.');
        setLoading(false);
      });
  }, [bookingId]);

  return (
    <div className="page-hero">
      <video className="page-video" src="/videos/confirm-bg.mp4" autoPlay loop muted playsInline preload="auto"/>
      <div className="page-content">
        <div className="container card">
          <h2>Booking Confirmation</h2>
          {loading && <p>Loading…</p>}
          {error   && <p className="error">{error}</p>}

          {!loading && !error && booking && (
            <>
              <p><strong>Booking ID:</strong> {booking.id}</p>
              <p><strong>Flight:</strong> {booking.flight.airline} {booking.flight.flightNumber}</p>
              <p>{booking.flight.origin} → {booking.flight.dest} @ {booking.flight.departureTime}</p>
              <p><strong>Class:</strong> {travelClass}</p>
              <p><strong>Passenger:</strong> {booking.passenger.name}</p>
              <p><strong>Email:</strong> {booking.passenger.email}</p>
              <p><strong>Phone:</strong> {booking.passenger.phone}</p>
              <p><strong>Total Paid:</strong> ${booking.price}</p>
              <Link to="/my-bookings" className="btn">My Bookings</Link>
            </>
          )}
        </div>
      </div>
    </div>
);
}
