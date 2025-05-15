import React, { useState } from 'react';
import './CheckInPage.css';
import { CLASS_PRICES } from '../utils/pricing';

export default function CheckInPage() {
  const [bookingId, setBookingId]         = useState('');
  const [seatClass, setSeatClass]         = useState('First');
  const [selectedRow, setSelectedRow]     = useState('');
  const [selectedLetter, setSelectedLetter] = useState('');

  // seat layout by class
  const seatConfig = {
    First:      { rows: [1],               letters: ['A','B','E','F'] },
    Business:   { rows: [2,3,4],           letters: ['A','B','E','F'] },
    'Economy Plus': {
      rows: Array.from({length:10},(_,i)=>i+5),
      letters: ['A','B','C','D','E','F']
    },
    Economy: {
      rows: Array.from({length:20},(_,i)=>i+15),
      letters: ['A','B','C','D','E','F']
    },
  };
  const { rows, letters } = seatConfig[seatClass] || { rows: [], letters: [] };
  const fare = CLASS_PRICES[seatClass];

  const handleSubmit = e => {
    e.preventDefault();
    console.log({ bookingId, seat: `${selectedRow}${selectedLetter}`, seatClass, fare });
    // TODO: call your check-in API, passing fare if needed
  };

  return (
    <div className="page-bg">
       <video className="page-video" src="/videos/checkin-bg.MP4" autoPlay loop muted playsInline preload="auto"/>
      <div className="page-content">
        <div className="container">
          <h2>Check-In</h2>
          <form onSubmit={handleSubmit} className="checkin-form">
            <label>
              Booking ID
              <input
                type="text"
                value={bookingId}
                onChange={e => setBookingId(e.target.value)}
                required
              />
            </label>
            <label>
              Class
              <select
                value={seatClass}
                onChange={e => {
                  setSeatClass(e.target.value);
                  setSelectedRow('');
                  setSelectedLetter('');
                }}
              >
                {Object.keys(seatConfig).map(c => (
                  <option key={c} value={c}>{c}</option>
                ))}
              </select>
            </label>
            <label>
              Row
              <select
                value={selectedRow}
                onChange={e => setSelectedRow(e.target.value)}
                required
              >
                <option value="" disabled>Select row</option>
                {rows.map(r => <option key={r} value={r}>{r}</option>)}
              </select>
            </label>
            <label>
              Seat Letter
              <select
                value={selectedLetter}
                onChange={e => setSelectedLetter(e.target.value)}
                required
              >
                <option value="" disabled>Select seat</option>
                {letters.map(l => <option key={l} value={l}>{l}</option>)}
              </select>
            </label>

            <p className="fare-display">
              Price for <strong>{seatClass}</strong>: <strong>${fare}</strong>
            </p>

            <button type="submit" className="btn">Confirm Check-In</button>
          </form>
        </div>
      </div>
    </div>
  );
}
