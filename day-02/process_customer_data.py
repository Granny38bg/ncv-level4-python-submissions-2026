
import random


# 1. Generate random machine usage minutes
def generate_minutes():
    minutes = random.randint(30, 180)
    return minutes


# 2. Calculate amount before VAT
def calc_amount(machine_type, minutes):

    # Machine charges
    initial_cost = {
        "A": 50.00,
        "B": 62.50,
        "C": 74.87
    }

    hourly_rate = {
        "A": 30.00,
        "B": 36.25,
        "C": 40.50
    }

    # Convert minutes into hours
    hours_used = minutes / 60

    # Calculate amount before VAT
    amount = initial_cost[machine_type] + (hourly_rate[machine_type] * hours_used)

    return amount


# 3. Calculate VAT and total payable
def calc_total_amount(amount):

    vat = amount * 0.14

    total_payable = amount + vat

    return vat, total_payable


# 4. Display daily summary
def display_summary(payments):

    number_customers = len(payments)

    combined_amount = sum(payments)

    average_payment = combined_amount / number_customers

    highest_payment = max(payments)

    lowest_payment = min(payments)

    print("\n========== DAILY PAYMENT SUMMARY ==========")

    print("Number of customers processed:", number_customers)

    print("Combined amount payable: R{:.2f}".format(combined_amount))

    print("Average payment per customer: R{:.2f}".format(average_payment))

    print("Highest payment: R{:.2f}".format(highest_payment))

    print("Lowest payment: R{:.2f}".format(lowest_payment))


# 5. Process customer payments
def process_payments():

    number_customers = int(input("Enter the number of customers to process: "))

    payments = []

    for i in range(number_customers):

        print("\n========== CUSTOMER", i + 1, "==========")

        customer_name = input("Enter customer's name: ")

        machine_type = input("Enter machine type (A, B or C): ").upper()

        # Generate usage minutes
        minutes = generate_minutes()

        # Calculate amount before VAT
        amount = calc_amount(machine_type, minutes)

        # Calculate VAT and total payable
        vat, total_payable = calc_total_amount(amount)

        # Store total payable
        payments.append(total_payable)

        # Display customer invoice
        print("\n========== CUSTOMER INVOICE ==========")

        print("Customer name:", customer_name)

        print("Machine type:", machine_type)

        print("Generated minutes:", minutes)

        print("Amount before VAT: R{:.2f}".format(amount))

        print("VAT (14%): R{:.2f}".format(vat))

        print("Total payable: R{:.2f}".format(total_payable))

        print("======================================")

    # Display daily summary
    display_summary(payments)


# Start the program
process_payments()
