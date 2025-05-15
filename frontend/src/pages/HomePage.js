// HomePage.js
import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';

export default function HomePage() {
  return (
    <div className="home-hero">
      {/* Video Background */}
      <video
        className="hero-video"
        src="/videos/background-video.mp4"
        autoPlay
        loop
        muted
        playsInline
        preload="auto"
      />

      {/* Dark Gradient Overlay */}
      <div className="hero-overlay"></div>

      {/* Main Content (Hero Card) */}
      <div className="hero-card">
        <div className="hero-brand">
          <img src="/images/logo.png" alt="Royal Flights Logo" className="hero-logo" />
          <h1 className="hero-title">ROYAL FLIGHTS</h1>
        </div>
        <p className="hero-subtitle">
          EXPERIENCE LUXURY IN THE SKIES — BOOK YOUR NEXT ADVENTURE TODAY.
        </p>
        <Link to="/search" className="btn">
          SEARCH FLIGHTS
        </Link>
      </div>
    </div>
  );
}
