# Programming Assignment #6

## Description
Process data in a file and produce a receipt

## Instructions
1. Write a program to read through a file of unknown length, i.e., use a sentinel-controlled while loop. The data in
the file contains information about items purchased by a customer. It is in sets of data as follows:
	- department letter (“C” = Clothes, “P” = Produce, “H” = Hardware, “O” = Other)
	- cost of item purchased

	As we have done, and has been explained in class, you will read the data a “set” at a time.
Stop reading when the department letter is an “X” (uppercase).

NOTE: There may be entries in the file for department letters other than
those specified above. If so, do not process those entries.

You may assume that there will be at least one entry for each of the
departments listed above.

As you read through the file, there are several tasks to carry out.
Compute tax for food items
- Compute tax for non-food items
- Print a receipt, with a “fancy” banner at the top
- Determine and print which department had the “most” number of items purchased
- Determine and print which department had the “most” money spent in it

Food items are taxed at 2% (department ‘P’)
Non-food items are taxed at 8.5% (all other departments)

2. Required Functions
You must have the following functions:

	**PrintHeader():**
	This function will print the header for the receipt. No parameters and it is a void function.

	**ComputeTax(amount,taxRate):**
	This function must compute the tax on the amount passed in as a parameter at the rate passed in as a
	parameter. The return value will be the computed tax.

	**MaxItems(countC,countP,countH,countO):**
	This function determines the largest of the parameters passed in to it and returns a single character, either a
	‘C’, a ‘P’, an ‘H’ or an ‘O’.

	**MaxSpent(sumC,sumP,sumH,sumO):**
	This function determines the largest of the parameters passed in to it and returns a single character, either a
	‘C’, a ‘P’, an ‘H’ or an ‘O’.

	You are allowed to have other programmer-defined functions as well.

## Sample Run
	+------------------------------------+
	+ +
	+ SuperMarket XYZ +
	+ Where You Always Save ! +
	+ +
	+ Sales Receipt +
	+ October 23, 2015 +
	+ +
	+------------------------------------+
	Clothes 49.59
	Clothes 30.79
	Other 11.78
	...
	...
	...
	Hardware 4.95
	-------------------------------
	Subtotal (food)
	Subtotal (non-food)
	Tax (food)
	Tax (non-food)
	-------------------------------
	Total
	------------------------------------------------
	Maximum Items: Hardware 3
	Maximum Cost: Clothes 80.38