# 🎨 Color Customization Guide

## How to Change Colors in Your Inventory App

Your CSS now uses **CSS Custom Properties (Variables)** that make it easy to customize colors!

### 📝 Quick Color Changes

Edit the `:root` section in `app/static/css/styles.css`:

```css
:root {
    /* Primary Colors - Main theme colors */
    --primary-color: #2563eb;        /* Change this for main blue */
    --primary-dark: #1d4ed8;        /* Darker shade */
    --primary-light: #3b82f6;       /* Lighter shade */

    /* Secondary Colors - Accent colors */
    --secondary-color: #10b981;     /* Change this for green accents */
    --secondary-dark: #059669;      /* Darker green */
    --secondary-light: #34d399;     /* Lighter green */

    /* Accent Colors - Special highlights */
    --accent-color: #f59e0b;        /* Change this for amber/orange */
    --accent-dark: #d97706;         /* Darker amber */

    /* Text Colors */
    --text-primary: #111827;        /* Main text color */
    --text-secondary: #6b7280;      /* Secondary text */
    --text-light: #9ca3af;          /* Light text */

    /* Background Colors */
    --bg-primary: #ffffff;          /* Main background */
    --bg-secondary: #f9fafb;        /* Secondary background */
    --bg-tertiary: #f3f4f6;         /* Tertiary background */
}
```

### 🎨 Popular Color Schemes

#### **Modern Blue Theme** (Current)
```css
--primary-color: #2563eb;
--secondary-color: #10b981;
--accent-color: #f59e0b;
```

#### **Professional Gray Theme**
```css
--primary-color: #374151;
--secondary-color: #6b7280;
--accent-color: #3b82f6;
```

#### **Nature Green Theme**
```css
--primary-color: #059669;
--secondary-color: #0d9488;
--accent-color: #ea580c;
```

#### **Purple Theme**
```css
--primary-color: #7c3aed;
--secondary-color: #ec4899;
--accent-color: #f59e0b;
```

#### **Dark Theme**
```css
--primary-color: #1f2937;
--secondary-color: #374151;
--accent-color: #3b82f6;
--bg-primary: #111827;
--bg-secondary: #1f2937;
--text-primary: #f9fafb;
```

### 🚀 How to Apply Changes

1. **Edit the CSS file**: `app/static/css/styles.css`
2. **Change the color values** in the `:root` section
3. **Save the file**
4. **Refresh your browser** to see changes instantly!

### 💡 Pro Tips

- **Test contrast**: Make sure text is readable on backgrounds
- **Use color tools**: Websites like Coolors.co or Adobe Color for inspiration
- **Brand colors**: Use your company/brand colors for `--primary-color`
- **Accessibility**: Ensure good contrast ratios for readability

### 🔄 Live Preview

Changes appear instantly when you refresh the page - no server restart needed!

---

**Current Theme**: Modern Blue & Green 🌊
**Last Updated**: September 2025