import React from 'react'
import { SECTION } from '../../utils/section'

export default function Section() {
    return (
        <div className='section'>
            <h1>We Give Top Production From Every Angle.</h1>
            <div className="section-blok">
                {SECTION.map(item => (
                    <div className='section-blok__section' key={item.id}>
                        <div className="section-blok__section__image">
                            <img src={item.image} alt={item.title} />
                        </div>
                        <h2>{item.title}</h2>
                        <div className="section-blok__section__footer">
                            <p className='section-blok__section__footer__p1'>{item.subtitle}</p>
                            <p className='section-blok__section__footer__p2'>{item.number}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};