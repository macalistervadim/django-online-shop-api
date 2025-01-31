import React, { useState } from 'react';
import axios from 'axios';
import { MdClose } from 'react-icons/md';
import { useNavigate } from 'react-router-dom';

export default function LoginComp() {

    const [isModalOpen, setIsModalOpen] = useState(false);
    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleOpenModal = async () => {
        setIsModalOpen(true);
        setError('');
    };

    const handleCloseModal = () => {
        setIsModalOpen(false);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!login || !password) {
            setError('Please fill all inputs!');
            return;
        }

        try {
            const response = await axios.post(
                'http://127.0.0.1:8000/api/login/',
                {
                    username: login,
                    password: password
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    withCredentials: true
                }
            );

            console.log(document.cookie); 
            console.log(response.data);
            navigate('/online-shop');

            if (response.data.success) {
                handleCloseModal();
            } else {
                setError('Неверный логин или пароль.');
            }
        } catch (error) {
            setError('Произошла ошибка при отправке данных.');
        }
    };

    return (
        <div>
            <p className="landing-header__login" onClick={handleOpenModal}>Login</p>

            {isModalOpen && (
                <div className="modal">
                    <div className="modal-content">
                        <div className="modal-content__header">
                            <h2>Login</h2>
                            <MdClose className="close-button" onClick={handleCloseModal} />
                        </div>
                        <form onSubmit={handleSubmit}>
                            <div className="form-group">
                                <label htmlFor="login">Login</label>
                                <input
                                    type="text"
                                    id="login"
                                    value={login}
                                    onChange={(e) => setLogin(e.target.value)}
                                    placeholder="Enter Login"
                                    required
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="password">Password</label>
                                <input
                                    type="password"
                                    id="password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    placeholder="Enter Password"
                                    required
                                />
                            </div>
                            {error && <p className="error-message">{error}</p>}
                            <button type="submit" className="submit-button">
                                Submit
                            </button>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};