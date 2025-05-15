import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchUserProfile } from '../services/api';
import './ProfilePage.css';

export default function ProfilePage() {
  const { userId } = useParams();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    fetchUserProfile(userId).then(res => setProfile(res.data));
  }, [userId]);

  if (!profile) return <p style={{ padding: '2rem', color: '#fff' }}>Loading…</p>;

  const bgUrl = `${process.env.PUBLIC_URL}/images/profile-bg.jpg`;

  return (
    <div
      className="page-bg"
      style={{
        backgroundImage: `url(${bgUrl})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      }}
    >
      <div className="page-content">
        <div className="container">
          <h2>{profile.name}</h2>
          <p>Email: {profile.email}</p>
          <p>Member since: {new Date(profile.joined).toLocaleDateString()}</p>
        </div>
      </div>
    </div>
  );
}
