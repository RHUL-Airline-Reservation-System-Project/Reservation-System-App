import React, { useState, useEffect } from 'react';
import Papa from 'papaparse';
import './InformationHubPage.css';

export default function InformationHubPage() {
  const [data, setData]       = useState([]);
  const [headers, setHeaders] = useState([]);

  useEffect(() => {
    Papa.parse(
      `${process.env.PUBLIC_URL}/data/real_flights_dataset.csv`,
      {
        download: true,
        header: true,
        skipEmptyLines: true,
        complete: ({ data: rows, meta }) => {
          setHeaders(meta.fields);
          setData(rows);
        },
      }
    );
  }, []);

  // Inline URL to public/images/info-bg.jpg
  const bgUrl = `${process.env.PUBLIC_URL}/images/info-bg.jpg`;

  return (
    <div
      className="page-bg info-hub-bg"
      style={{
        backgroundImage: `url(${bgUrl})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        minHeight: 'calc(100vh - 60px)',
        filter: 'brightness(0.8) contrast(1.1)',
      }}
    >
      <div className="page-bg-gradient" />
      <div className="page-content">
        <div className="container">
          <h2>Information Hub</h2>

          {data.length === 0 ? (
            <p>Loading flight data…</p>
          ) : (
            <div className="table-wrapper">
              <table className="info-table">
                <thead>
                  <tr>
                    {headers.map(h => (
                      <th key={h}>{h.replace(/_/g, ' ').toUpperCase()}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {data.map((row, idx) => (
                    <tr key={idx}>
                      {headers.map(h => (
                        <td key={h}>{row[h] ?? '—'}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
