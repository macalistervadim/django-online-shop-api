import React, { useEffect, useState } from 'react';
import { IoIosPricetag, IoMdResize } from 'react-icons/io';
import { PiListNumbersDuotone } from 'react-icons/pi';
import { Link, useParams } from 'react-router-dom';
import { MdOutlineKeyboardArrowRight } from 'react-icons/md';
import axios from 'axios';

export default function ProductsComp() {
    const { id } = useParams();
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/products/');
                setProducts(response.data);
            } catch (err) {
                console.error(err);
            }
        };

        fetchProducts();
    }, []);

    // Фильтрация продуктов по ID категории
    const filteredProducts = products.filter((product) => product.category === Number(id));

    return (
        <div>
            <div className="navigator">
                <div className="navigator-blok">
                    <Link to="/online-shop">Main</Link>
                    <MdOutlineKeyboardArrowRight className="navigator__slesh" />
                    <p className="navigator__p">Products</p>
                </div>
            </div>
            <div className="producs">
                <div className="products-blok">
                    {filteredProducts.length > 0 ? (
                        filteredProducts.map((item) => (
                            <div className="products-blok__section" key={item.id}>
                                <div className="products-blok__section__image">
                                    <Link to={`/online-shop/product/${item.id}`}>
                                        <img src="/images/category.jpg" alt="" />
                                    </Link>
                                </div>
                                <Link to={`/online-shop/product/${item.id}`}>
                                    <h2>{item.name}</h2>
                                </Link>
                                <div className="products-blok__container">
                                    <div className="products-blok__container__section">
                                        <IoIosPricetag className="products-blok__container__section__icon" />
                                        <p>Price: <span style={{ color: 'blue', fontWeight: 'bold' }}>
                                            {Number(item.price).toLocaleString('ru-RU')} UZS
                                        </span></p>
                                    </div>
                                </div>
                            </div>
                        ))
                    ) : (
                        <div>
                            <p>No products found for this category.</p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};