# The index numbers help us retrieve individual elements from a list.

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
print(row_1[0]) # output : Facebook

# The syntax for retrieving individual list elements follows the model list_name[index_number]. For instance, the name of our list above is row_1, and the index number of the first element is 0 — following the list_name[index_number] model, we get row_1[0], where the index number 0 is in square brackets after the variable name row_1.

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]

difference = row_2[4] - row_1[4]
average_rating = (row_1[4] + row_2[4]) / 2

print(difference)
print(average_rating)
