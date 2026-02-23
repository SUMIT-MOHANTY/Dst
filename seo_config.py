SEO_CONFIG = {
    "site_name": "My Website",
    "site_url": "https://example.com",
    "default_description": "Welcome to my website. Learn about our products and services.",
    "default_image": "https://example.com/images/og-image.jpg",
    "twitter_handle": "@mywebsite",
    "pages": {
        "/": {
            "title": "Home",
            "description": "Welcome to my website. Learn about our products and services.",
            "priority": 1.0,
            "changefreq": "daily"
        },
        "/about": {
            "title": "About Us",
            "description": "Learn more about our company, mission, and values.",
            "priority": 0.8,
            "changefreq": "weekly"
        },
        "/contact": {
            "title": "Contact",
            "description": "Get in touch with us. Find our contact information and form.",
            "priority": 0.5,
            "changefreq": "monthly"
        }
    }
}
