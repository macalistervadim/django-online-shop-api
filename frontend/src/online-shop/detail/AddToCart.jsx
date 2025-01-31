import axios from 'axios';
import React, { useState } from 'react';
import { FaCartShopping } from "react-icons/fa6";

export default function AddToCart({ data }) {
    const [successMessage, setSuccessMessage] = useState(false);
    const [errorMessage, setErrorMessage] = useState(false);
    const csrfToken = localStorage.getItem('csrfToken');

    const handleAddToCart = async () => {
        try {
            const response = await axios.post(
                `http://127.0.0.1:8000/api/cart/`,
                {
                    product_id: data.id
                },
                {
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFTOKEN": csrfToken
                    },
                    withCredentials: true
                }
            );

            if (response.data.success) {
                setSuccessMessage(true);

                setTimeout(() => {
                    setSuccessMessage(false);
                }, 5000);
            }
        } catch (error) {
            console.error("Ошибка при добавлении в корзину:", error.message);

            setErrorMessage(true);

            setTimeout(() => {
                setErrorMessage(false);
            }, 5000);
        }
    };

    return (
        <div>
            {successMessage && (
                <div className="notification">
                    <p>Added to cart!</p>
                    <div className="notification-bar"></div>
                </div>
            )}
            {errorMessage && (
                <div className="notification">
                    <p style={{color: 'red'}}>Failed to add to cart!</p>
                    <div style={{backgroundColor: 'red'}} className="notification-bar"></div>
                </div>
            )}
            <button
                className="detail-blok__section-2__header__button-2"
                onClick={handleAddToCart}
            >
                To cart
                <FaCartShopping className='detail-blok__section-2__header__button-2__icon' />
            </button>
        </div>
    );
};