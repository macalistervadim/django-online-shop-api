import React from 'react'
import { NAME } from './utils/name'
import LoginComp from './LoginComp'
import { Link } from 'react-router-dom'

export default function LandingPage() {
    return (
        <div className='landing'>
            <div className="landing-header">
                <div>
                    <img src="/images/logo.jpg" alt={`${NAME} Logo`} />
                </div>
                <LoginComp />
            </div>
            <div className="landing-blok">
                <h1>Langheinrich In Uzbekistan</h1>
                <p>Unsere Internetseite befindet sich derzeit im Umbau</p>
                <Link to='/online-shop'><button>Store</button></Link>
            </div>
            <div className="landing-footer">
                <div className="landing-footer__container">
                    <p className='landing-footer__p1'>Langheinrich Vertriebs GmbH</p>
                    <div className="landing-footer__container__container">
                        <p><a href="tel:+496642870">Tel: +49 6642 / 87-0</a></p>
                        <p><a href="tel:4966428763">Fax: +49 6642 / 87-63</a></p>
                    </div>
                    <p className='landing-footer__p2'><a href="mailto:service@langheinrich.de">service@langheinrich.de</a></p>
                </div>
            </div>
        </div>
    )
};