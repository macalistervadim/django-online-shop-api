import React from 'react'
import { Link } from 'react-router-dom'
import LoginLink from '../../LoginLink'

export default function Footer() {
    return (
        <div className='footer'>
            <div className="footer-blok">
                <p>Copyright © 2022 <span>Langheinrich</span> Designed by <a href="akbarsoft.uz">Akbar Soft</a>.</p>
                <div className='footer-blok__container'>
                    <Link to='/contacts'>Contacts</Link>
                    <div>/</div>
                    <LoginLink />
                </div>
            </div>
        </div>
    )
};