# 📦 Inventory Management System

A modern, professional inventory management web application built with Flask. Features a clean, responsive UI with Chennai-centric business workflow optimization.

## 📸 Application Screenshots

### 🏠 Dashboard - Main Overview
![Dashboard](screenshots/dashboard.png)
*Main dashboard showing real-time inventory statistics, recent activity, and quick action buttons*

### 📦 Product Management
![Product List](screenshots/products-list.png)
*Complete product catalog with add, edit, view, and delete capabilities*

![Add Product](screenshots/add-product.png)
*User-friendly product creation form with validation*

### 🏪 Location Management
![Location List](screenshots/locations-list.png)
*Warehouse and storage location management interface*

![Add Location](screenshots/add-location.png)
*Location creation form for setting up warehouses*

### 📊 Stock Movements
![Movement List](screenshots/movements-list.png)
*Complete movement tracking with stock in, out, and transfers*

![Record Movement](screenshots/record-movement.png)
*Movement recording form with dropdown selections*

### 📈 Reports & Analytics
![Balance Report](screenshots/balance-report.png)
*Real-time inventory balance report with interactive charts*

![Charts Dashboard](screenshots/charts-dashboard.png)
*Advanced analytics with Chart.js visualizations*

### 📱 Responsive Design
![Mobile View](screenshots/mobile-view.png)
*Mobile-optimized responsive interface*

## ✨ Features

### Core Functionality
- **Product Management**: Add, edit, view, and delete products with detailed specifications
- **Location Management**: Manage multiple warehouse locations (Chennai-focused)
- **Stock Movements**: Record stock in, stock out, and transfers between locations
- **Real-time Reports**: Balance reports showing inventory levels by product and location
- **Activity Tracking**: Recent movements dashboard with complete audit trail

### User Experience
- **Modern UI**: Clean, professional interface with intuitive navigation
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Real-time Statistics**: Live dashboard with inventory counts and trends
- **Chennai Business Integration**: Optimized for Chennai-based inventory operations

## 🛠️ Tech Stack

- **Backend**: Flask 3.x, SQLAlchemy, SQLite (configurable to PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, JavaScript, Jinja2 templates
- **Database**: SQLite (development), PostgreSQL/MySQL (production ready)
- **Charts**: Chart.js for analytics and reporting

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd aerele
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**
   ```bash
   python seed.py
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:5000`

## 📱 Usage Guide

### Getting Started
1. **Add Products**: Start by creating your product catalog
2. **Set Up Locations**: Create warehouse/storage locations
3. **Record Movements**: 
   - **Stock In**: Add inventory to locations
   - **Stock Out**: Remove inventory from locations  
   - **Transfer**: Move inventory between locations
4. **Monitor**: Use the dashboard to track inventory levels and recent activity

### Business Workflow
The system is optimized for Chennai-based businesses with features like:
- Local currency display (₹)
- Regional business hour optimization
- Indian standard time tracking
- Location naming conventions suitable for Chennai operations

## 🏗️ Project Structure

```
aerele/
├── app/
│   ├── routes/          # Route handlers (products, locations, movements, reports)
│   ├── static/          # CSS, JavaScript, and image files
│   ├── templates/       # Jinja2 HTML templates
│   ├── __init__.py      # App factory and configuration
│   └── models.py        # Database models
├── instance/            # Instance-specific files (created automatically)
├── .venv/              # Virtual environment (gitignored)
├── requirements.txt     # Python dependencies
├── run.py              # Application entry point
├── seed.py             # Database initialization script
└── README.md           # This file
```

## ⚙️ Configuration

### Environment Variables
- `DATABASE_URL`: Database connection string (default: SQLite)
- `SECRET_KEY`: Secret key for session security (set in production)
- `FLASK_ENV`: Environment mode (development/production)

### Database Setup
```bash
# For production with PostgreSQL
export DATABASE_URL="postgresql://user:password@localhost/inventory_db"

# For production with MySQL
export DATABASE_URL="mysql://user:password@localhost/inventory_db"
```

## 📊 Features in Detail

### Dashboard
- Real-time inventory statistics
- Recent activity feed
- Quick action buttons
- Visual progress indicators

### Product Management
- Complete CRUD operations
- Product categorization
- Detailed product information
- Stock level tracking

### Location Management
- Multiple warehouse support
- Location-based inventory tracking
- Transfer capabilities between locations

### Movement Tracking
- Comprehensive movement logging
- Automatic balance calculations
- Historical transaction records
- Date and time stamping

### Reporting
- Current stock levels by location
- Product-wise inventory reports
- Movement history analysis
- Chart-based visualizations

## 🔧 Development

### Adding New Features
1. Create new route handlers in `app/routes/`
2. Add corresponding templates in `app/templates/`
3. Update models in `app/models.py` if needed
4. Add CSS/JS in `app/static/`

### Database Migrations
The app uses Flask-Migrate for database changes:
```bash
flask db init        # Initialize migrations (first time only)
flask db migrate     # Create migration
flask db upgrade     # Apply migration
```

## 🚀 Production Deployment

### Recommended Production Setup
1. Use PostgreSQL or MySQL instead of SQLite
2. Set proper environment variables
3. Use a WSGI server like Gunicorn
4. Set up reverse proxy with Nginx
5. Enable HTTPS with SSL certificates

### Sample Production Command
```bash
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 Future Enhancements

- [ ] User authentication and role-based access
- [ ] Advanced reporting with export capabilities
- [ ] API endpoints for integration
- [ ] Barcode scanning support
- [ ] Email notifications for low stock
- [ ] Advanced search and filtering
- [ ] Data import/export (CSV, Excel)
- [ ] Multi-language support

## 📞 Support

For support, email your-email@domain.com or create an issue in the GitHub repository.

## 🚀 GitHub Deployment Guide

### Step 1: Create GitHub Repository
1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon and select "New repository"
3. Name your repository (e.g., `inventory-management-system`)
4. Add a description: "Modern Flask inventory management system with responsive UI"
5. Keep it public for portfolio showcase
6. **Don't** initialize with README (we already have one)
7. Click "Create repository"

### Step 2: Connect Local Repository to GitHub
```bash
# Add GitHub as remote origin
git remote add origin https://github.com/YOUR_USERNAME/inventory-management-system.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Add Screenshots
After pushing to GitHub:
1. Take screenshots of each page while the app is running
2. Save them in the `screenshots/` folder with these names:
   - `dashboard.png` - Main dashboard
   - `products-list.png` - Products listing page
   - `add-product.png` - Add product form
   - `locations-list.png` - Locations listing page
   - `add-location.png` - Add location form
   - `movements-list.png` - Movements listing page
   - `record-movement.png` - Record movement form
   - `balance-report.png` - Balance report with charts
   - `charts-dashboard.png` - Charts and analytics page
   - `mobile-view.png` - Mobile responsive view

3. Commit and push the screenshots:
```bash
git add screenshots/
git commit -m "Add application screenshots for documentation"
git push
```

### Step 4: Customize for Your Profile
Update these sections in README.md:
- Replace `YOUR_USERNAME` with your GitHub username
- Update email in Support section
- Add your name to Contributing section
- Update the clone URL in Quick Start

### 🎯 Portfolio Tips
- ⭐ Star your own repository
- 📝 Write a detailed commit history
- 🏷️ Add relevant tags/topics: `flask`, `python`, `inventory`, `web-app`, `responsive`
- 📖 Pin the repository to your profile
- 🔗 Add the live demo link (if deployed)

**Your Flask Inventory Management System is now ready to showcase on GitHub!** 🌟

