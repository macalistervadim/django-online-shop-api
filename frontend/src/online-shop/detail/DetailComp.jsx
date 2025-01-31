import React, { useEffect, useState } from 'react';
import { MdOutlineKeyboardArrowRight } from 'react-icons/md';
import { Link, useParams } from 'react-router-dom';
import MakeOrder from './MakeOrder';
import AddToCart from './AddToCart';
import axios from 'axios';
import { IoIosPricetags } from "react-icons/io";

export default function DetailComp() {
    const { id } = useParams();
    const [product, setProduct] = useState(null);
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        const fetchProduct = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/products/${id}`);
                setProduct(response.data);
            } catch (err) {
                console.error(err);
            }
        };

        fetchProduct();
    }, [id]);

    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/categories');
                setCategories(response.data);
            } catch (err) {
                console.error(err);
            }
        };

        fetchCategories();
    }, []);

    // Поиск названия категории по её ID
    const getCategoryName = (categoryId) => {
        const category = categories.find((cat) => cat.id === categoryId);
        return category ? category.name : 'Unknown Category';
    };

    return (
        <div>
            {product ? (
                <div>
                    <div className="navigator">
                        <div className="navigator-blok">
                            <Link to='/online-shop'>Main</Link>
                            <MdOutlineKeyboardArrowRight className='navigator__slesh' />
                            <Link to={`/online-shop/category/${product.category}`}>
                                {getCategoryName(product.category)}
                            </Link>
                            <MdOutlineKeyboardArrowRight className='navigator__slesh' />
                            <p className='navigator__p'>{product.name}</p>
                        </div>
                    </div>
                    <div className='detail'>
                        <div className="detail-blok">
                            <div className="detail-blok__section-1">
                                <div className="detail-blok__section-1__image">
                                    <img src="/images/category.jpg" alt="" />
                                </div>
                            </div>
                            <div className="detail-blok__section-2">
                                <h2>{product.name}</h2>
                                <div className="detail-blok__section-2__container">
                                    <div className="detail-blok__section-2__container-part">
                                        <p className='detail-blok__section-2__container-part__p'>
                                            <IoIosPricetags className='detail-blok__section-2__container-part__icon' />
                                            <span className='detail-blok__section-2__container-part__p__span'>
                                                {Number(product.price).toLocaleString('ru-RU')}
                                                <p>UZS</p>
                                            </span>
                                        </p>
                                    </div>
                                    <div className="detail-blok__section-2__header">
                                        <MakeOrder data={product} />
                                        <AddToCart data={product.id} />
                                    </div>
                                    <p className='detail__description'>{product.description}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            ) : (
                <div>no data</div>
            )}
        </div>
    );
};