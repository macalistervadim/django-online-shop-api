import React from 'react'
import Navbar from '../navbar/navbar'
import OrdersComp from './OrdersComp'
import Footer from '../../components/footer/Footer'

export default function Orders() {
    return (
        <div>
            <div className='layout'>
                <Navbar />
                <OrdersComp />
            </div>
            <Footer />
        </div>
    )
};