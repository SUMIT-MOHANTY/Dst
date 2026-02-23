from flask import Response
import xml.etree.ElementTree as ET
from datetime import datetime

def generate_sitemap(urls):
    """urls is a list of dicts: [{'loc': 'url', 'lastmod': 'ISO-date', 'priority': '0.5'}]"""
    urlset = ET.Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    
    for url_data in urls:
        url = ET.SubElement(urlset, 'url')
        loc = ET.SubElement(url, 'loc')
        loc.text = url_data['loc']
        
        if 'lastmod' in url_data:
            lastmod = ET.SubElement(url, 'lastmod')
            lastmod.text = url_data['lastmod']
        
        priority = ET.SubElement(url, 'priority')
        priority.text = url_data.get('priority', '0.5')
    
    return Response(ET.tostring(urlset, encoding='unicode'), mimetype='application/xml')
