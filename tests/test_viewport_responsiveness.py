import pytest
from playwright.sync_api import Page, expect

VIEWPORTS = [
    {"width": 375, "height": 667},  # Mobile
    {"width": 768, "height": 1024}, # Tablet
    {"width": 1920, "height": 1080} # Desktop
]

BASE_URL = "http://localhost:3000"

def test_mobile_navigation(page: Page):
    page.set_viewport_size(VIEWPORTS[0])
    page.goto(BASE_URL)
    # Check hamburger menu exists and desktop nav is hidden
    expect(page.locator("nav.mobile-menu")).to_be_visible()
    expect(page.locator("nav.desktop-menu")).not_to_be_visible()

def test_no_horizontal_scroll(page: Page):
    """Verify content fits width, preventing horizontal scrolling."""
    for vp in VIEWPORTS:
        page.set_viewport_size(vp)
        page.goto(BASE_URL)
        width = page.evaluate("document.body.scrollWidth")
        assert width <= vp["width"] + 10, f"Horizontal overflow detected at {vp['width']}px"

def test_core_ui_visibility(page: Page):
    """Ensure critical elements are not obscured"""
    page.set_viewport_size(VIEWPORTS[1])
    page.goto(BASE_URL)
    hero = page.locator(".hero")
    expect(hero).to_be_in_viewport()

def test_accessibility_viewport(page: Page):
    page.set_viewport_size(VIEWPORTS[0])
    page.goto(BASE_URL)
    # Ensure buttons have minimum touch target size (48x48 via bounding box)
    buttons = page.locator("button").all()
    for btn in buttons:
        box = btn.bounding_box()
        if box:
            assert box["width"] >= 44, "Button too small for touch target"
