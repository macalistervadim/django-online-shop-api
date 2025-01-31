import React from 'react'
import { FaCircleCheck } from "react-icons/fa6";

export default function About() {
    return (
        <div className='about'>
            <div className="about-blok">
                <div className="about-blok__section-1">
                    <img src="/images/about.jpg" alt="" />
                    <div className="about-blok__section-1__container">
                        <p className='about-blok__section-1__container__p1'>25+</p>
                        <p className='about-blok__section-1__container__p2'>Year experience in Fabiflex</p>
                    </div>
                </div>
                <div className="about-blok__section-2">
                    <p className='about-blok__section-2__p1'>GET INFORMED</p>
                    <h1>LET'S BUILD SOMETHING CREATIVE TOGETHER</h1>
                    <div className="about-blok__section-2__header">
                        <img src="/images/about-icon.png" alt="" />
                        <p>We’re in this business <span>Since 1987</span> and we provide the best service</p>
                    </div>
                    <p className='about-blok__section-2__p2'>It is additionally connected with the production of clothes. The crude material of textiles is the fiber which might be regular regenerated.</p>
                    <div className="about-blok__section-2__container">
                        <div className="about-blok__section-2__container-part">
                            <FaCircleCheck className='about-blok__section-2__container-part__icon' />
                            <p>It can be very well produced using fiber, yarn, texture, or mix.</p>
                        </div>
                        <div className="about-blok__section-2__container-part">
                            <FaCircleCheck className='about-blok__section-2__container-part__icon' />
                            <p>It is one of the most extensive terms applied to the clothing industry.</p>
                        </div>
                        <div className="about-blok__section-2__container-part">
                            <FaCircleCheck className='about-blok__section-2__container-part__icon' />
                            <p>It might be a finished or unfinished item. It has no particular use.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
};