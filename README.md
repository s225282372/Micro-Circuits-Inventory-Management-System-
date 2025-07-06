# 📦 Micro Circuits Inventory Management System (Console-Based)

This is a console-based Inventory Management System developed for **Micro Circuits**, a newly launched electronics retailer aiming to improve operational efficiency by tracking inventory electronically. The system allows staff to manage stock codes, prices, and item counts through a simple Command-Line Interface (CLI).

---

## ✅ Features

- Maintain up to **50 unique stock codes**
- Track:
  - Stock codes (strings)
  - Prices (floating-point, max R1000.00)
  - Quantity in stock (integers, max 100 per item)
- **AddStockCode()**: Add a new stock code and price to the system
- **SearchCode(code)**: Efficiently search for stock code and return its index or a message if not found
- **AddStockItem()**: Add stock quantity to an existing code (capped at 100 per item)
- **DisplayStockList()**: View all stock codes with price, quantity, and total stock value
- **Persistent CLI Menu**: Navigate via a simple text-based menu

---

## 🧑‍💻 Usage

1. **Run the script** using a Python interpreter
2. Choose from the following menu options:
   ```
   1. Add Stock Code
   2. Add Stock Item
   3. Display Stock List
   4. Exit
   ```
3. Menu repeats after each action unless option **4 (Exit)** is selected.

---

## 📋 Sample Output Format

```
Stock code, In stock, Price, Stock value
AAA, 10, 50.00, 500.00
BBB, 5, 20.00, 100.00
Total, , , 600.00
```

---

## 🔒 Constraints

- Maximum stock types: **50**
- Maximum price per item: **R1000.00**
- Maximum items per stock code: **100**

---

## 🛠️ Functions Overview

| Function Name      | Description |
|--------------------|-------------|
| `AddStockCode()`   | Adds a new stock code and price |
| `SearchCode(code)` | Searches and returns index of a stock code |
| `AddStockItem()`   | Adds items to an existing stock code |
| `DisplayStockList()` | Displays all inventory details and total value |

---

## 💡 Example Workflow

1. Add new stock codes using option 1.
2. Increase stock quantity using option 2.
3. Check the full stock list and value using option 3.
4. Exit safely using option 4.

---

## 🧾 Requirements

- Python 3.x
- No external libraries required

---

## 📍 Project Status

✅ **Completed Specification**  
📦 **Console Only**  
⚙️ **Expandable for GUI or database integration in the future**

---

## 🧑‍🎓 Author
 **Maselaelo Glen**
 
*For educational and operational use.*
