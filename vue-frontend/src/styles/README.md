# Theme Configuration

This folder contains the centralized color palette for the entire application.

## How to Change Colors

To change the color palette across the entire app, simply edit `/src/styles/theme.css`.

All components use CSS custom properties (CSS variables) from this file, so changes here will automatically apply everywhere.

## Color Variables

### Main Colors

- `--color-bg-primary`: Main background color (cream)
- `--color-bg-secondary`: Secondary background color (lighter cream)
- `--color-primary`: Primary brand color (teal)
- `--color-primary-hover`: Hover state for primary color
- `--color-text`: Main text color (dark blue)
- `--color-accent`: Accent/highlight color (orange)
- `--color-accent-hover`: Hover state for accent color
- `--color-white`: White color for backgrounds

### Semantic Colors

- `--color-node-selected`: Selected skill tree node color
- `--color-node-available`: Available skill tree node color
- `--color-node-locked`: Locked skill tree node color

### Opacity Variants

Pre-defined colors with specific opacity levels for consistency:

- `--color-primary-10`: Primary color at 10% opacity
- `--color-primary-15`: Primary color at 15% opacity
- `--color-primary-60`: Accent color at 60% opacity
- `--color-text-08`: Text color at 8% opacity (subtle shadows)
- `--color-text-12`: Text color at 12% opacity (medium shadows)

### Special Purpose Colors

- `--color-overlay-bg`: Scrollytelling overlay background
- `--color-overlay-active`: Active scrollytelling step background
- `--color-overlay-shadow`: Overlay shadow color
- `--color-overlay-shadow-active`: Active overlay shadow
- `--color-tooltip-bg`: Tooltip background color
- `--color-tooltip-text`: Tooltip text color
- `--color-tooltip-bg-opacity`: Tooltip background with opacity

## Example: Changing to a Different Color Scheme

To switch from the current teal/orange theme to a blue/purple theme:

```css
:root {
  /* Update these values in theme.css */
  --color-bg-primary: #e8f4f8; /* Light blue background */
  --color-primary: #2563eb; /* Blue */
  --color-primary-hover: #1d4ed8; /* Darker blue */
  --color-accent: #9333ea; /* Purple */
  --color-accent-hover: #7e22ce; /* Darker purple */

  /* Update semantic colors accordingly */
  --color-node-selected: #2563eb;
  --color-node-available: #9333ea;

  /* Update opacity variants */
  --color-primary-10: rgba(37, 99, 235, 0.1);
  --color-primary-15: rgba(37, 99, 235, 0.15);
  /* ... and so on */
}
```

That's it! All components will automatically use the new colors.
