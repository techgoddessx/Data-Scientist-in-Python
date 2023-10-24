# Sometimes we want to get more than one piece of information from a list. For example, if we have a list like ['Facebook', 0.0, 'USD', 2974676, 3.5], we might only want the name of the app and the details about its ratings (how many ratings it has and what the rating is). Here's how we can get those specific parts from the list:

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]

fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
print(fb_rating_data)
