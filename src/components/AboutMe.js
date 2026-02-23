import React from 'react';
import { ABOUT_DATA } from '../constants/aboutData';
import { sanitizeHTML } from '../utils/sanitize';
import '../styles/AboutMe.css';

const AboutMe = () => {
  return (
    <section className="about-me" aria-labelledby="about-heading">
      <div className="about-me__container">
        <h2 id="about-heading" className="about-me__title">About Me</h2>
        
        <div className="about-me__content">
          {/* Profile Picture Placeholder with Error Handling */}
          <div className="about-me__avatar-wrapper">
            <img 
              src="/images/profile-placeholder.png"
              alt={ABOUT_DATA.profilePicAlt}
              className="about-me__avatar"
              onError={(e) => {
                e.target.style.display = 'none';
                e.target.nextSibling.style.display = 'flex';
              }}
            />
            <div className="about-me__avatar-fallback">
              <span>No Image</span>
            </div>
          </div>

          {/* Bio Content sanitized to prevent XSS */}
          <div className="about-me__bio">
            <p 
              dangerouslySetInnerHTML={{ 
                __html: sanitizeHTML(ABOUT_DATA.bio) 
              }} 
            />
          </div>
        </div>

        {/* Responsive Skills Grid */}
        <div className="about-me__skills-section">
          <h3 className="about-me__skills-title">Skills</h3>
          <ul className="skills-grid" role="list">
            {ABOUT_DATA.skills.map((skill, index) => (
              <li key={index} className="skills-grid__item">
                {skill}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
};

export default AboutMe;
