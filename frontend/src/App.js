import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import Layout from './components/Layout';
import AppRoutes from './routes';
import './styles/globals.css';

export default function App() {
  return (
    <BrowserRouter>
      <Layout>
        <AppRoutes />
      </Layout>
    </BrowserRouter>
  );
}
