import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
    const csrfToken = sessionStorage.getItem('csrfToken');

    if (!csrfToken) {
        return <Navigate to="/" />;
    }

    // Если токен есть, рендерим дочерний компонент
    return children;
};

export default ProtectedRoute;