from pprint import pprint
import pandas as pd

# Define a list of words related to shopping
words = ['buy', 'price', 'discount', 'promotion', 'promo', 'shop']
print(words)

# Define a list of products related to sofas
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

keywords_list = []

# Loop through each product
for product in products:
    # Loop through each word in the shopping list
    for word in words:
        # Create combinations of product and word, and append to the keywords_list
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product , word + ' ' + product])

# Use pprint to print the keywords_list in a readable format
pprint(keywords_list)

# Convert the keywords_list into a DataFrame
keywords_df = pd.DataFrame.from_records(keywords_list)

# Display the first few rows of the DataFrame to explore it
print(keywords_df.head())

# Rename the columns of the DataFrame for clarity
keywords_df = keywords_df.rename(columns={0:'Ad Group', 1:'Keyword'})

# Add a new column named 'Campaign' and set its value to 'SEM_Sofas' for all rows
keywords_df['Campaign'] = 'SEM_Sofas'

# Add another column named 'Criterion Type' and set its value to 'Exact' for all rows
keywords_df['Criterion Type'] = 'Exact'

# Make a copy of the keywords DataFrame to create a version for phrase match type
keywords_phrase = keywords_df.copy()

# Update the 'Criterion Type' column value to 'Phrase' for the copied DataFrame
keywords_phrase['Criterion Type'] = 'Phrase'

# Combine the original and copied DataFrames to have both exact and phrase match types
keywords_df_final = keywords_df.append(keywords_phrase)

# Save the combined DataFrame to a CSV file named 'keywords.csv'
keywords_df_final.to_csv('keywords.csv', index = False)

# Display a summary of the campaign work by grouping by 'Ad Group' and 'Criterion Type' and counting the keywords
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)
