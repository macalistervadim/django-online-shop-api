import React, { useState } from 'react';
import { FaPlay } from "react-icons/fa";

export default function Video() {
    const [isPlaying, setIsPlaying] = useState(false);

    const handlePlay = () => {
        setIsPlaying(true);
    };

    const closeModal = () => {
        setIsPlaying(false);
    };

    return (
        <div className='video'>
            <div className="video-blok">
                <div className="video-blok__player" onClick={handlePlay}>
                    <FaPlay className='video-blok__player__icon' />
                </div>
                <p>WHAT ARE REVIEWS</p>
                <h1>Our Materials will build your Trust</h1>
            </div>

            {isPlaying && (
                <div className="video-modal" onClick={closeModal}>
                    <div className="video-modal__content" onClick={(e) => e.stopPropagation()}>
                        <video controls autoPlay>
                            <source src="/videos/video.mp4" type="video/mp4" />
                            Your browser does not support the video tag.
                        </video>
                        <button className="video-modal__close" onClick={closeModal}>✖</button>
                    </div>
                </div>
            )}
        </div>
    );
};