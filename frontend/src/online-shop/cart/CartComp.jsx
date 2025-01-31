import React, { useEffect, useState } from 'react'
import Navbar from '../navbar/navbar'
import { MdOutlineKeyboardArrowRight } from 'react-icons/md'
import { Link } from 'react-router-dom'
import { RiCloseLargeFill } from 'react-icons/ri'
import axios from 'axios'
import Footer from '../../components/footer/Footer'

export default function CartComp() {

    const [cart, setCart] = useState([]);

    useEffect(() => {
        const fetchCarts = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/cart/', {
                    headers: {
                        'X-CSRFToken': sessionStorage.getItem('csrfToken'),
                        'Content-Type': 'application/json',
                    }
                });
                console.log(response.data);
                setCart(response.data);
            } catch (error) {
                console.error(error);
            }
        }
        fetchCarts();
    }, []);

    const handleDeleteCart = async (itemId) => {
        try {
            await axios.delete(`http://127.0.0.1:8000/api/cart/delete/${itemId}/`, {
                headers: { "Content-Type": "application/json" },
                withCredentials: true,
            });
            setCart((prevCart) => prevCart.filter(item => item.id !== itemId));
        } catch (error) {
            console.error(error.message);
        }
    };

    return (
        <div>
            <div className='layout'>
                <Navbar />
                <div className="navigator">
                    <div className="navigator-blok">
                        <Link to='/online-shop'>Main</Link>
                        <MdOutlineKeyboardArrowRight className='navigator__slesh' />
                        <p className='navigator__p'>Cart</p>
                    </div>
                </div>
                <div className='cart'>
                    <div className="cart-blok">
                        <div className="cart-blok__section cart-blok__section__header">
                            <div className="cart-blok__section-part" style={{ color: 'var(--main-color' }}>PRODUCT</div>
                            <div className="cart-blok__section-part" style={{ color: 'var(--main-color' }}>PRICE</div>
                            <div className="cart-blok__section-part__end"></div>
                        </div>
                        <br />
                        <hr />
                        <br />
                        {cart ? (
                            cart.map(item => (
                                <div className='cart-blok__section cart-blok__section-2'>
                                    <div className="cart-blok__section-part">
                                        <div className="cart-blok__section-part__footer">
                                            <div className="cart-blok__section-part__footer__image">
                                                <Link to={`online-shop/product/${item.id}`}>
                                                    <img src={item.image} alt="" />
                                                </Link>
                                            </div>
                                            <Link to={`online-shop/product/${item.id}`}>
                                                <h3>{item.name}</h3>
                                            </Link>
                                        </div>
                                    </div>
                                    <div className="cart-blok__section-part">
                                        <p>{item.price} UZS</p>
                                    </div>
                                    <div className="cart-blok__section-part__end">
                                        <RiCloseLargeFill onClick={() => handleDeleteCart(item.id)} className="cart-blok__section-part__end__icon" />
                                    </div>
                                </div>
                            ))
                        ) : (
                            <div>
                                <p>no data</p>
                            </div>
                        )}
                    </div>
                </div>
            </div>
            <Footer />
        </div>
    )
};