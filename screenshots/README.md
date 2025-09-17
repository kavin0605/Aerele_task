# Screenshots Guide

## Required Screenshots for Documentation

Take screenshots of the following pages while the app is running at http://127.0.0.1:5000:

### 1. dashboard.png
- URL: http://127.0.0.1:5000
- Shows: Main dashboard with statistics, recent activity, quick actions

### 2. products-list.png  
- URL: http://127.0.0.1:5000/products
- Shows: Product listing page with all products

### 3. add-product.png
- URL: http://127.0.0.1:5000/products/create
- Shows: Add new product form

### 4. locations-list.png
- URL: http://127.0.0.1:5000/locations  
- Shows: Location listing page

### 5. add-location.png
- URL: http://127.0.0.1:5000/locations/create
- Shows: Add new location form

### 6. movements-list.png
- URL: http://127.0.0.1:5000/movements
- Shows: Movement history and listing

### 7. record-movement.png
- URL: http://127.0.0.1:5000/movements/create
- Shows: Record new movement form

### 8. balance-report.png
- URL: http://127.0.0.1:5000/reports/balance
- Shows: Balance report with charts and statistics

### 9. charts-dashboard.png
- URL: http://127.0.0.1:5000/reports/charts
- Shows: Advanced charts and analytics page

### 10. mobile-view.png
- Any page viewed on mobile/responsive mode
- Shows: Mobile responsive design

## Screenshot Tips
- Use full screen for desktop screenshots
- Ensure all content is visible
- For mobile view, use browser developer tools to simulate mobile
- Save as PNG format for best quality
- Use consistent naming as specified above

After taking screenshots, run:
```bash
git add screenshots/
git commit -m "Add application screenshots for documentation"
git push
```
