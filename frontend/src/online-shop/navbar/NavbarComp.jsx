import React, { useEffect, useState } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
import { NAME } from '../../utils/name'
import { PiShoppingCartBold } from "react-icons/pi";
import { FaHistory } from 'react-icons/fa';
import { IoExitOutline } from "react-icons/io5";

export default function NavbarComp() {

    const location = useLocation();
    const [activePage, setAcitvePage] = useState(location.pathname);
    const navigate = useNavigate();

    useEffect(() => {
        setAcitvePage(location.pathname)
    }, [location]);

    const handleLogOut = () => {
        // Удаляем csrfToken из куков (если он был установлен)
        document.cookie = 'csrftoken=; Max-Age=0; path=/;';
        localStorage.removeItem("csrfToken"); // если сохранял в localStorage
        navigate('/');
    };

    return (
        <div className='navbar'>
            <div className="navbar-blok">
                <div className="navbar-blok__section">
                    <Link to='/'><img src="/images/logo.jpg" alt={`${NAME} Logo`} /></Link>
                </div>
                <div className="navbar-blok__section">
                    <div className="navbar-blok__section__container">
                        <div onClick={handleLogOut}><IoExitOutline className='navbar-blok__section__container__icon__exit' /></div>
                        <Link to='/online-shop/cart' className='navbar-blok__section__container__part' style={{ backgroundColor: activePage === '/online-shop/cart' ? 'var(--main-color)' : '' }}>
                            <p style={{ color: activePage === '/online-shop/cart' ? '#fff' : '' }}>Cart</p>
                            <PiShoppingCartBold
                                className='navbar-blok__section__container__icon'
                                style={{ color: activePage === '/online-shop/cart' ? '#fff' : '' }}
                            />
                        </Link>
                    </div>
                    <div className="navbar-blok__section__container">
                        <Link to='/online-shop/orders' className='navbar-blok__section__container__part' style={{ backgroundColor: activePage === '/online-shop/orders' ? 'var(--main-color)' : '' }}>
                            <p style={{ color: activePage === '/online-shop/orders' ? '#fff' : '' }}>Orders</p>
                            <FaHistory
                                className='navbar-blok__section__container__icon'
                                style={{ color: activePage === '/online-shop/orders' ? '#fff' : '' }}
                            />
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    )
};