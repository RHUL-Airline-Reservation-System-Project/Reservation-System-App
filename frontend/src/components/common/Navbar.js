import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

export default function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/" className="brand">
        <img
          src="/images/logo.png"
          alt="Royal Flights Logo"
          className="brand-logo"
        />
        <span className="brand-text">Royal Flights</span>
      </Link>
      <div className="nav-links">
        <Link to="/search">Search Flights</Link>
        <Link to="/my-bookings">My Bookings</Link>
        <Link to="/info-hub">Information Hub</Link>
        <Link to="/benefits">Benefits</Link>
        <Link to="/profile/1">My Profile</Link>
        <Link to="/check-in/1">Check In</Link>
      </div>
    </nav>
  );
}
