import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { MdDeleteOutline, MdOutlineKeyboardArrowRight } from 'react-icons/md'
import { Link } from 'react-router-dom'

export default function OrdersComp() {

    const [orders, setOrders] = useState([]);

    useEffect(() => {
        const fetchAllOrders = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/orders',);
                setOrders(response.data)
            } catch (error) {
                console.error(error);
            }
        }
        fetchAllOrders();
    }, []);

    // const handleDeleteOrders = async (orderId) => {
    //     try {
    //         const response = await axios.delete(`http://127.0.0.1:8000/api/orders/delete/${orderId}`, {
    //             headers: { "Content-Type": "application/json" }
    //         }, { withCredentials: true })
    //     } catch (error) {
    //         console.error(error);
    //     }
    // };

    return (
        <div>
            <div className="navigator">
                <div className="navigator-blok">
                    <Link to='/online-shop'>Main</Link>
                    <MdOutlineKeyboardArrowRight className='navigator__slesh' />
                    <p className='navigator__p'>Orders</p>
                </div>
            </div>
            <div className='orders'>
                <div className="orders-blok">
                    <div className="orders-blok__section orders-blok__section-1">
                        <div className="orders-blok__section-part__main"><p>Id</p></div>
                        <div className="orders-blok__section-part__product"><p>Product</p></div>
                        <div className="orders-blok__section-part"><p>Quantity</p></div>
                        <div className="orders-blok__section-part__price"><p>Price</p></div>
                        <div className="orders-blok__section-part"><p>Date</p></div>
                        {/* <div className="orders-blok__section-part__end"></div> */}
                    </div>
                    {orders.map(item => (
                        <div className='orders-blok__section orders-blok__section-2' key={item.id}>
                            <div className="orders-blok__section-part__main">
                                <p>{item.id}</p>
                            </div>
                            <div className="orders-blok__section-part__product">
                                <Link to={`online-shop/product/${item.id}`}>
                                    <img src="/images/category.jpg" alt="" />
                                </Link>
                                <Link to={`online-shop/product/${item.id}`}>
                                    <p>Product Name</p>
                                </Link>
                            </div>
                            <div className="orders-blok__section-part">
                                <p>{item.quantity}</p>
                            </div>
                            <div className="orders-blok__section-part__price">
                                <p>{item.price}</p>
                            </div>
                            <div className="orders-blok__section-part">
                                <p>{item.price}</p>
                            </div>
                            {/* <div className="orders-blok__section-part__end">
                            <MdDeleteOutline className='orders-blok__section-part__icon' />
                        </div> */}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
};