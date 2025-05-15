// src/routes.js
import React from 'react';
import { Routes, Route } from 'react-router-dom';

import Layout                from './components/Layout';
import HomePage              from './pages/HomePage';
import SearchFlightsPage     from './pages/SearchFlightsPage';
import ResultsPage           from './pages/ResultsPage';
import BookingPage           from './pages/BookingPage';
import ConfirmationPage      from './pages/ConfirmationPage';
import ManageBookingsPage    from './pages/ManageBookingsPage';
import InformationHubPage    from './pages/InformationHubPage';
import CheckInPage           from './pages/CheckInPage';
import ProfilePage           from './pages/ProfilePage';
import BenefitsPage          from './pages/BenefitsPage';

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/"                   element={<HomePage />} />
      <Route path="/search"             element={<SearchFlightsPage />} />
      <Route path="/results"            element={<ResultsPage />} />
      <Route path="/book/:flightId"     element={<BookingPage />} />
      <Route path="/confirm/:bookingId" element={<ConfirmationPage />} />
      <Route path="/my-bookings"        element={<ManageBookingsPage />} />
      <Route path="/info-hub"           element={<InformationHubPage />} />
      <Route path="/check-in/:bookingId"element={<CheckInPage />} />
      <Route path="/profile/:userId"    element={<ProfilePage />} />
      <Route path="/benefits"           element={<BenefitsPage />} />
    </Routes>
  );
}
