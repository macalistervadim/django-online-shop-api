import React from 'react'
import Navbar from './navbar/navbar'
import LayoutMain from './layout/layoutmain'
import Footer from '../components/footer/Footer'

export default function OnlineShop() {
    return (
        <div>
            <div className='layout'>
                <Navbar />
                <LayoutMain />
            </div>
            <Footer />
        </div>
    )
};