import React from 'react'
import LandingPage from './LandingPage'
import Section from './components/section/Section'
import About from './components/about/About'
import Video from './components/video/Video'
import Footer from './components/footer/Footer'

export default function Home() {
    return (
        <div className='home'>
            <LandingPage />
            <Section />
            <About />
            <Video />
            <Footer />
        </div>
    )
};