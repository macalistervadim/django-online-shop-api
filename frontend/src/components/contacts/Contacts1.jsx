import React from 'react'
import { OFFICES } from '../../utils/contactOffices'

export default function Contacts1() {
    return (
        <div className='contacts1'>
            <h1>Explore Our Office Worldwide</h1>
            <div className="contacts1-blok">
                {OFFICES.map(item => (
                    <div className='contacts1-blok__section' key={item.id}>
                        <div className="contacts1-blok__section__image">
                            <img src={item.image} alt={item.city} />
                        </div>
                        <p className='contacts1-blok__section__p1'>{item.city}</p>
                        <a href={`tel:${item.phone}`}><p className='contacts1-blok__section__p2'>{item.phone}</p></a>
                        <a href={`mailto:${item.email}`}><p className='contacts1-blok__section__p3'>{item.email}</p></a>
                        <p className='contacts1-blok__section__p4'>{item.address}</p>
                    </div>
                ))}
            </div>
        </div>
    )
};