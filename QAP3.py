# Description: Program for Honest Harry Car Sales to keep track of used vehicle sales.
# Author: Sarah Murphy
# Date: June 10, 2024 - June 12, 2024

# Define required libraries.
import datetime


# Program constants.
LICENSE_FEE_LOW = 75.00
LICENSE_FEE_HIGH = 165.00
TRANS_FEE = 0.01
LUX_TAX = 0.016
HST_RATE = 0.15
FINANCE_FEE = 39.99


# Main program begins here.
while True:

    # User inputs.
    CustFirst = input("Please enter the customer's first name. If you wish to exit, type 'End': ").title()
    if CustFirst == "End":
        exit()
    while True:
        if CustFirst == "":
            print("Data entry error: This field cannot be blank. Please try again.")
            CustFirst = input("Please enter the customer's first name: ").title()
        else:
            break

    while True:
        CustLast = input("Please enter the customer's last name: ").title()
        if CustLast == "":
            print("Data entry error: This field cannot be blank. Please try again.")
        else:
            break
    
    allowed_char = set("0123456789")
    while True:
        CustPhone = input("Please enter the customer's 10 digit phone number: ")
        if CustPhone == "":
            print("Data entry error: This field cannot be blank. Please try again.")
        elif len(CustPhone) != 10:
            print("Data entry error: Phone number must be 10 digits. Please try again.")
        elif set(CustPhone).issubset(allowed_char) == False:
            print("Data entry error: Phone number contains invalid characters. Please try again.")
        else:
            CustPhoneDsp = "(" + CustPhone[0:3] + ")" + CustPhone[3:6] + "-" + CustPhone[6:]
            break
     
    while True:
        PlateNum = input("Please enter the vehicle's license plate number: ").upper()
        if PlateNum == "":
            print("Data entry error: This field cannot be blank. Please try again.")
        elif len(PlateNum) != 6:
            print("Data entry error: License plate number must be 6 characters. Please try again.")
        elif PlateNum[0:3].isalpha() == False:
            print("Data entry error: License plate number must start with 3 letters.")
        elif PlateNum[3:6].isdigit() == False:
            print("Data entry error: License plate number must end with 3 numbers.")
        else:
            break
        
    CarMake = input("Please enter the make of the vehicle: ").title()
    CarModel = input("Please input the model of the vehicle: ").title()

    allowed_char = set("0123456789")
    while True:
        CarYear = input("Please enter the year of the vehicle: ")
        if len(CarYear) !=4:
            print("Data entry error: This field must contain the 4 digit year of the vehicle's make. Please try again.")
        elif set(CarYear).issubset(allowed_char) == False:
            print("Data entry error: This field contains invalid characters. Please try again.")
        else:
            break
    
    while True:
        SellPrice = float(input("Please enter the selling price of the vehicle: "))
        if SellPrice > 50000.00:
            print("Data entry error: Vehicle selling price cannot exceed $50,000.00. Please try again.")
        else:
            break

    while True:
        TradeValue = float(input("Please enter the trade-in value of the vehicle: "))
        if TradeValue > SellPrice:
            print("Data entry error: The trade-in value cannot exceed the vehicle selling price. Please try again.")
        else: 
            break
            
        SalesName = input("Please enter the name of the salesperson: ")


    # Program calculations.
    TradePrice = SellPrice - TradeValue
    
    if SellPrice <= 5000.00:
        LicenseFee = LICENSE_FEE_LOW
    else:
        LicenseFee = LICENSE_FEE_HIGH

    if SellPrice > 20000.00:
        TransFee = (SellPrice * TRANS_FEE)
    else:
        TransFee = (SellPrice * TRANS_FEE) + (SellPrice * LUX_TAX)

    Subtotal = TradePrice + LicenseFee + TransFee
    Tax = (Subtotal * HST_RATE)
    TotSalesPrice = Subtotal + Tax

    CurrDate = datetime.datetime.now()
    FirstPayDate = CurrDate + datetime.timedelta(days=30)

    ReceiptNum = CustFirst[0] + CustLast[0] + "-" + PlateNum[3:7] + "-" + CustPhone[6:]


    # Program outputs for invoice.
    print()
    print(f"Honest Harry Car Sales                         Invoice Date:{CurrDate.strftime("%B %d, %Y"):>14s}") # Formatted Month dd, yyyy
    print(f"Used Car Sale and Receipt                        Receipt No:{ReceiptNum:>16s}")
    print()
    SellPriceDsp = "${:,.2f}".format(SellPrice)
    print(f"                                        Sale price:               {SellPriceDsp:>10s}")
    TradeValueDsp = "${:,.2f}".format(TradeValue)
    print(f"Sold to:                                Trade Allowance:          {TradeValueDsp:>10s}")
    print(f"                                        ------------------------------------")
    CustNameDsp = CustFirst[0] + ". " + CustLast
    TradePriceDsp = "${:,.2f}".format(TradePrice)
    print(f"     {CustNameDsp:<28s}       Price after Trade:        {TradePriceDsp:>10s}")
    LicenseFeeDsp = "${:,.2f}".format(LicenseFee)
    print(f"     {CustPhoneDsp}                      License Fee:              {LicenseFeeDsp:>10s}")
    TransFeeDsp = "${:,.2f}".format(TransFee)
    print(f"                                        Transfer Fee:             {TransFeeDsp:>10s}")
    print(f"                                        ------------------------------------")
    SubtotalDsp = "${:,.2f}".format(Subtotal)
    print(f"Car Details:                            Subtotal:                 {SubtotalDsp:>10s}")
    TaxDsp = "${:,.2f}".format(Tax)
    print(f"                                        HST:                      {TaxDsp:>10s}")
    print(f"     {CarYear:<4s} {CarMake:<13s} {CarModel:<10s}      ------------------------------------")
    TotSalesPriceDsp = "${:,.2f}".format(TotSalesPrice)
    print(f"                                        Total sales price:        {TotSalesPriceDsp:>10s}")
    print()
    print(f"----------------------------------------------------------------------------")
    print()
    print(f"                                 Financing      Total          Monthly")
    print(f"       # Years    # Payments        Fee         Price          Payment")
    print(f"       ---------------------------------------------------------------")

    for NumYears in range (1,5):
        NumPayments = NumYears * 12
        FinanceFee = FINANCE_FEE * NumYears
        TotalPrice = TotSalesPrice + FinanceFee
        MonthPay = TotalPrice / NumPayments

        NumYearsDsp = "{:1d}".format(NumYears)
        NumPaymentsDsp = "{:2d}".format(NumPayments)
        FinanceFeeDsp = "${:,.2f}".format(FinanceFee)
        TotalPriceDsp = "${:,.2f}".format(TotalPrice)
        MonthPayDsp = "${:,.2f}".format(MonthPay)
    
        print(f"          {NumYearsDsp:>1s}           {NumPaymentsDsp:>2s}          {FinanceFeeDsp:>7s}     {TotalPriceDsp:>9s}     {MonthPayDsp:>9s}")
    print(f"       ---------------------------------------------------------------")
    print(f"       Invoice date: {CurrDate.strftime("%d-%b-%y")}           First payment date: {FirstPayDate.strftime("%d-%b-%y")}") # Formatted dd-MON-yy
    print()
    print(f"-----------------------------------------------------------------------------")
    print(f"                     Best used cars at the best prices!")
    print()