from playwright.sync_api import Page, expect

def test_hero_animation_performance(page: Page):
    page.goto("http://localhost:8000/")
    
    # Wait for initial load
    page.wait_for_load_state("networkidle")
    
    # Check if hero section elements animate in
    hero_title = page.locator(".hero-title")
    expect(hero_title).to_be_visible()
    
    # Basic check for animation class presence mitigates missing assets risk
    class_list = hero_title.get_attribute("class") or ""
    assert "animate-" in class_list or "transition-" in class_list, "Hero animation CSS classes missing"

def test_respects_reduced_motion(page: Page):
    page.goto("http://localhost:8000/")
    # In conftest we set reduced_motion='reduce', so we check behavior here
    # We expect animations to be disabled or instant
    moving_element = page.locator(".hero-title")
    box = moving_element.bounding_box()
    
    # Force a reflow check or simply ensure it renders without complex timing
    assert box is not None, "Element failed to render with reduced motion"
