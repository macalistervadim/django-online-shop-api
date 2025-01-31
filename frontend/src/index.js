import React from 'react';
import ReactDOM from 'react-dom/client';

import App from "./App";

import './styles/styles.css'
import './styles/landing.css'
import './styles/modal.css'
import './styles/section.css'
import './styles/about.css'
import './styles/video.css'
import './styles/contacts.css'
import './styles/contacts1.css'
import './styles/contacts2.css'
import './styles/footer.css'

import './online-shop/styles/navbar.css'
import './online-shop/styles/layout.css'
import './online-shop/styles/products.css'
import './online-shop/styles/navigator.css'
import './online-shop/styles/cart.css'
import './online-shop/styles/detail.css'
import './online-shop/styles/orders.css'
import './online-shop/styles/notification.css'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);