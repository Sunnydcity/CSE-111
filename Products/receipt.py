import csv
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.

    Return:
        A compound dictionary that contains the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = [row[0], row[1], float(row[2])]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: missing file\n{e}")
    return dictionary


def calculate_discount(quantity, price):
    """Apply a buy-one-get-one-half-off discount for item D083."""
    full_price_count = quantity // 2 + quantity % 2
    half_price_count = quantity // 2
    return (full_price_count * price) + (half_price_count * price * 0.5)


def main():
    try:
        # Read the products.csv file into a dictionary
        products_dict = read_dictionary('/home/marcus/Documents/CSE 111/Products/products.csv', 0)

        # Print store name
        print("Inkom Emporium\n")

        # Open and process the request.csv file
        with open('/home/marcus/Documents/CSE 111/Products/request.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            total_items = 0
            subtotal = 0.0
            print("Ordered Items:")

            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                try:
                    product_details = products_dict[product_number]
                    product_name = product_details[1]
                    product_price = product_details[2]

                    # Apply discount for D083
                    if product_number == "D083":
                        item_total = calculate_discount(quantity, product_price)
                        print(f"{product_name}: {quantity} @ {product_price:.2f} (discounted)")
                    else:
                        item_total = quantity * product_price
                        print(f"{product_name}: {quantity} @ {product_price:.2f}")

                    total_items += quantity
                    subtotal += item_total

                except KeyError:
                    print(f"Error: unknown product ID in the request.csv file\n'{product_number}'")

        # Print totals
        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total = subtotal + sales_tax

        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")

        # Print thank you message and current date/time
        print("\nThank you for shopping at the Inkom Emporium.")
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")

        # Print additional features
        new_years_sale_date = datetime(current_date_and_time.year + 1, 1, 1)
        days_until_sale = (new_years_sale_date - current_date_and_time).days
        print(f"\nDon't forget our New Year's Sale starts in {days_until_sale} days!")

        return_by_date = current_date_and_time + timedelta(days=30)
        print(f"Return by: {return_by_date:%a %b %d %I:%M %p %Y}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: permission denied\n{e}")


# Call the main function
if __name__ == "__main__":
    main()
