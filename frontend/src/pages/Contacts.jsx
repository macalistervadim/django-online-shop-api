import React from 'react'
import { FaHome } from "react-icons/fa";
import { Link } from 'react-router-dom';
import Contacts1 from '../components/contacts/Contacts1';
import Contacts2 from '../components/contacts/Contacts2';
import Footer from '../components/footer/Footer';

export default function Contacts() {
    return (
        <div>
            <div className="contacts">
                <div className="contacts-blok">
                    <div className="contacts-blok__section">
                        <Link to='/'><img src="/images/logo.jpg" alt="" /></Link>
                    </div>
                    <div className="contacts-blok__section">
                        <div className="contacts-blok__section__container">
                            <div className="contacts-blok__section__container-part">
                                <Link to='/'>
                                    <FaHome className='contacts-blok__section__container-part__icon' />
                                    <p className='contatcs-blok__section__container-part__p1'>HOME</p>
                                </Link>
                            </div>
                            <div className="contacts-blok__section__container-part">
                                <p className='contatcs-blok__section__container-part__p1'>/</p>
                            </div>
                            <div className="contacts-blok__section__container-part">
                                <p className='contatcs-blok__section__container-part__p2'>CONTACT US</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <Contacts1 />
            <Contacts2 />
            <Footer />
        </div>
    )
};