from mcp.server.fastmcp import FastMCP
import mysql.connector

mcp = FastMCP("Banking Server")


@mcp.tool()
def get_customer(name: str) -> str:

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD"
        database="banking_db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM customers WHERE name=%s",
        (name,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return (
            f"ID: {result[0]}\n"
            f"Name: {result[1]}\n"
            f"Account: {result[2]}\n"
            f"Balance: ₹{result[3]}"
        )

    return "Customer not found"


@mcp.tool()
def get_all_customers() -> str:

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD"
        database="banking_db"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")

    rows = cursor.fetchall()

    output = ""

    for row in rows:
        output += (
            f"ID:{row[0]}, "
            f"Name:{row[1]}, "
            f"Account:{row[2]}, "
            f"Balance:₹{row[3]}\n"
        )

    cursor.close()
    conn.close()

    return output

@mcp.tool()
def get_all_customers() -> str:
    pass

@mcp.tool()
def check_balance(account_no: str) -> str:
    pass

@mcp.tool()
def deposit_money(account_no: str, amount: float) -> str:
    pass

@mcp.tool()
def withdraw_money(account_no: str, amount: float) -> str:
    pass

@mcp.tool()
def transfer_money(from_acc: str, to_acc: str, amount: float) -> str:
    pass

@mcp.tool()
def create_customer(name: str, account_no: str, balance: float) -> str:
    pass

@mcp.tool()
def delete_customer(name: str) -> str:
    pass

@mcp.tool()
def update_customer_balance(account_no: str, balance: float) -> str:
    pass

@mcp.tool()
def search_customer(name: str) -> str:
    pass

@mcp.tool()
def search_account(account_no: str) -> str:
    pass

@mcp.tool()
def customer_count() -> str:
    pass

@mcp.tool()
def richest_customer() -> str:
    pass

@mcp.tool()
def poorest_customer() -> str:
    pass

@mcp.tool()
def average_balance() -> str:
    pass

@mcp.tool()
def total_bank_balance() -> str:
    pass
if __name__ == "__main__":
    mcp.run()