#!/usr/bin/env python3
"""
Backend Database Access Script
Shows how to access inventory database directly
"""

import sqlite3
import os

def main():
    db_path = 'instance/inventory.db'

    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        print("=== DIRECT DATABASE ACCESS ===")

        # Get table info
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print(f"📋 Tables: {[t[0] for t in tables]}")

        # Count records in each table
        for table in ['products', 'locations', 'product_movements']:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"📊 {table}: {count} records")

        # Sample product data
        cursor.execute("SELECT name FROM products LIMIT 3")
        products = cursor.fetchall()
        print("\n📦 Sample Products:")
        for p in products:
            print(f"  - {p[0]}")

        # Sample movements
        cursor.execute("""
            SELECT p.name, pm.qty, pm.timestamp
            FROM product_movements pm
            JOIN products p ON pm.product_id = p.id
            ORDER BY pm.timestamp DESC
            LIMIT 3
        """)
        movements = cursor.fetchall()
        print("\n📈 Recent Movements:")
        for m in movements:
            print(f"  - {m[0]}: {m[1]} units")

        conn.close()
        print("\n✅ Database access successful!")

    except Exception as e:
        print(f"❌ Error accessing database: {e}")

if __name__ == "__main__":
    main()