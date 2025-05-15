import React from 'react';
import './BenefitsPage.css';

export default function BenefitsPage() {
  return (
    <div className="benefits-page">
      <div className="benefits-hero">
        <div className="hero-content">
          <h1 className="hero-title">Upgrade to Business Class</h1>
          <p className="hero-text">
            Enhance your journey to an extraordinary experience by upgrading to our premium cabin. Enjoy world-class comfort, exceptional service, and gourmet dining at 30,000 feet.
          </p>
          <button className="upgrade-button">Upgrade now</button>
        </div>
      </div>

      <div className="benefits-features">
        <h2 className="benefits-title">The Premium Difference</h2>
        <div className="benefits-grid">
          <div className="benefit-card">
            <img src="/images/lie-flat-seats.jpg" alt="Lie-Flat Seats" />
            <h3>Lie-Flat Seats</h3>
            <p>Relax with fully reclining seats for maximum comfort.</p>
          </div>
          <div className="benefit-card">
            <img src="/images/gourmet-dining.jpg" alt="Gourmet Dining" />
            <h3>Gourmet Dining</h3>
            <p>Indulge in world-class cuisine prepared by top chefs.</p>
          </div>
          <div className="benefit-card">
            <img src="/images/enhanced-privacy.jpg" alt="Dedicated Space" />
            <h3>Dedicated Space</h3>
            <p>Your own private space with personalized service.</p>
          </div>
          <div className="benefit-card">
            <img src="/images/personalized-service.jpg" alt="Personalized Service" />
            <h3>Personalized Service</h3>
            <p>Exceptional care from our dedicated cabin crew.</p>
          </div>
        </div>
      </div>
    </div>
  );
}
