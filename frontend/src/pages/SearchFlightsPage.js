import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './SearchFlightsPage.css';

export default function SearchFlightsPage() {
  const [origin, setOrigin]         = useState('');
  const [dest, setDest]             = useState('');
  const [date, setDate]             = useState('');
  const [travelClass, setTravelClass] = useState('Economy');
  const navigate = useNavigate();

  const handleSubmit = e => {
    e.preventDefault();
    navigate('/results', { state: { origin, dest, date, travelClass } });
  };

  return (
    <div className="page-hero">
      <video className="page-video" src="/videos/search-bg.mp4" autoPlay loop muted playsInline preload="auto"/>
      <div className="page-content">
        <div className="container card search-card">
          <h2>Find Your Flight</h2>
          <form onSubmit={handleSubmit} className="search-form">
            <label>
              From
              <input
                type="text"
                value={origin}
                onChange={e => setOrigin(e.target.value)}
                placeholder="e.g. LHR"
                required
              />
            </label>
            <label>
              To
              <input
                type="text"
                value={dest}
                onChange={e => setDest(e.target.value)}
                placeholder="e.g. JFK"
                required
              />
            </label>
            <label>
              Date
              <input
                type="date"
                value={date}
                onChange={e => setDate(e.target.value)}
                required
              />
            </label>
            <label>
              Class
              <select
                value={travelClass}
                onChange={e => setTravelClass(e.target.value)}
              >
                <option>Economy</option>
                <option>Economy Plus</option>
                <option>Business</option>
                <option>First</option>
              </select>
            </label>
            <button type="submit" className="btn">Search Flights</button>
          </form>
        </div>
      </div>
    </div>
  );
}
