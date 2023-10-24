# Retrieve each individual rating.
# Sum the ratings.
# Divide by the number of ratings.

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Fruit Ninja Classic', 1.99, 'USD', 698516, 4.5]
row_5 = ['Minecraft: Pocket Edition', 6.99, 'USD', 522012, 4.5]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
rating_sum = 0
for app in app_data_set :
    rating = app[-1]
    rating_sum += rating
avg_rating = rating_sum / len(app_data_set)
print(avg_rating)

