#!/usr/bin/env python3
import os
from datetime import datetime

def generate_sitemap():
    pages = [
        {"loc": "https://example.com/", "priority": "1.0", "changefreq": "daily"},
        {"loc": "https://example.com/about", "priority": "0.8", "changefreq": "weekly"},
        {"loc": "https://example.com/contact", "priority": "0.5", "changefreq": "monthly"},
    ]
    lastmod = datetime.now().strftime("%Y-%m-%d")
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        xml_content += '    <url>\n'
        xml_content += f'        <loc>{page["loc"]}</loc>\n'
        xml_content += f'        <lastmod>{lastmod}</lastmod>\n'
        xml_content += f'        <changefreq>{page["changefreq"]}</changefreq>\n'
        xml_content += f'        <priority>{page["priority"]}</priority>\n'
        xml_content += '    </url>\n'
    xml_content += '</urlset>\n'
    
    with open('/workspace/sitemap.xml', 'w') as f:
        f.write(xml_content)
    print("Sitemap generated successfully!")

if __name__ == '__main__':
    generate_sitemap()
