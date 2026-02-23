# Contact Form with JavaScript Validation

A responsive contact form with real-time JavaScript validation that provides immediate feedback to users.

## Features

- **Real-time validation** on blur and input events
- **Visual feedback** with color-coded borders (green for valid, red for invalid)
- **Error messages** displayed below each field
- **Required field validation** for name, email, subject, and message
- **Pattern validation** for email format and phone numbers
- **Minimum length validation** for name and message fields
- **Form submission** with success message
- **Accessible** with proper labels and focus management

## Validation Rules

| Field | Rules |
|-------|-------|
| Name | Required, min 2 chars, letters only |
| Email | Required, valid email format |
| Phone | Optional, valid phone format (min 10 digits) |
| Subject | Required, must select an option |
| Message | Required, min 10 characters |

## Usage

Open `index.html` in a web browser to use the contact form.

## Files

- `index.html` - Main HTML structure
- `validate.js` - JavaScript validation logic
- `styles.css` - Styling and feedback states
- `README.md` - Documentation