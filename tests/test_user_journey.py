from playwright.sync_api import Page, expect

def test_landing_to_contact_to_ai_journey(page: Page):
    # Step 1: Load Landing Page
    page.goto("http://localhost:8000/")
    expect(page).to_have_title(/Landing/)
    
    # Step 2: Navigate to Contact Form
    contact_btn = page.get_by_role("link", name="Contact Us")
    contact_btn.click()
    expect(page).to_have_url(".*/contact")

    # Step 3: Verify Animation Presence (ensure no layout shift)
    form_container = page.locator(".contact-form-container")
    expect(form_container).to_be_visible()
    box_before = form_container.bounding_box()
    
    # Step 4: Fill and Submit Form
    page.fill("input[name='email']", "test@example.com")
    page.fill("textarea[name='message']", "Hello AI")
    page.click("button[type='submit']")
    
    # Step 5: Verify Transition to AI Interaction
    ai_section = page.locator(".ai-response-area")
    expect(ai_section).to_be_visible(timeout=5000)
    
    # Validate layout stability (box model shouldn't jump wildly)
    box_after = ai_section.bounding_box()
    assert abs(box_before['x'] - box_after['x']) < 50, "Significant horizontal layout shift detected"
