import React from 'react'
import ProductsComp from './ProductsComp'
import Navbar from '../navbar/navbar'
import Footer from '../../components/footer/Footer'

export default function Products() {
    return (
        <div>
            <div className='layout'>
                <Navbar />
                <ProductsComp />
            </div>
            <Footer />
        </div>
    )
};