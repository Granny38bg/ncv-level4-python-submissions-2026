
# Dictionary containing facility codes and hourly rates
amount = {
    "squa": 13,
    "swim": 12,
    "gym": 11,
    "wei": 8
}


# Function to receive customer details
def getDetails():
    name = input("Enter customer's name: ")
    facility_code = input("Enter facility code (Squa, Swim, Gym, Wei): ").lower()
    hours = int(input("Enter number of hours: "))

    return name, facility_code, hours


# Function to calculate amount due
def AmountDue(facility_code, hours):

    if facility_code in amount:
        payment = hours * amount[facility_code]
        return payment
    else:
        return -1


# Function to calculate VAT
def calculateVAT(subtotal):
    vat = subtotal * 0.15
    return vat


# Function to calculate final amount
def calculatePayment(subtotal, vat):
    total = subtotal + vat
    return total


# Function to display customer's payment
def displayPayment(name, facility_code, hours, subtotal, vat, total):

    print("\n========== CUSTOMER PAYMENT ==========")
    print("Customer Name:", name)
    print("Facility Code:", facility_code)
    print("Number of Hours:", hours)
    print("--------------------------------------")
    print("Amount Due: R", format(subtotal, ".2f"))
    print("VAT (15%): R", format(vat, ".2f"))
    print("--------------------------------------")
    print("TOTAL PAYMENT: R", format(total, ".2f"))
    print("======================================")


# Main program
def main():

    # Receive customer details
    name, facility_code, hours = getDetails()

    # Calculate amount due
    subtotal = AmountDue(facility_code, hours)

    if subtotal == -1:
        print("Invalid facility code. Please try again.")

    else:
        # Calculate VAT
        vat = calculateVAT(subtotal)

        # Calculate final payment
        total = calculatePayment(subtotal, vat)

        # Display payment
        displayPayment(name, facility_code, hours,
                       subtotal, vat, total)


# Call main function
main()
