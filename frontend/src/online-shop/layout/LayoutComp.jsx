import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { LuClipboardList } from 'react-icons/lu';
import axios from 'axios';

export default function LayoutComp() {
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/categories');
                setCategories(response.data);
            } catch (error) {
                console.error('Failed to fetch categories:', error);
                setError('Failed to load categories');
            } finally {
                setLoading(false);
            }
        };
        fetchCategories();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div className="error-message">{error}</div>;
    }

    return (
        <div className="layout-blok">
            {categories.length > 0 ? (
                categories.map((item) => (
                    <div className="layout-blok__section" key={item.id}>
                        <div className="layout__container">
                            <div className="layout-blok__section__image">
                                <Link to={`/online-shop/category/${item.id}`}>
                                    <img src="/images/category.jpg" alt={`Category: ${item.name}`} />
                                </Link>
                            </div>
                            <div className="layout__container__info">
                                <Link to={`/online-shop/category/${item.id}`}>
                                    <h2>{item.name}</h2>
                                </Link>
                                <div className="layout-blok__section__footer">
                                    <LuClipboardList className="layout-blok__section__footer__icon" />
                                    <p>
                                        Products: <span>{item.product_count}</span>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                ))
            ) : (
                <div>No categories available</div>
            )}
        </div>
    );
}
