import pandas as pd
# Read the CSV file
input_file_path = 'gene.csv'
output_file_path = 'output.csv'
df = pd.read_csv(input_file_path)
# Iterate over columns L1 to L7 and add new columns with 1 or 0 based on the presence of genes
for i in range(1, 8):
    col_name = f'NewColumn_{i}'
    df[col_name] = df['Gene'].isin(df[f'L{i}']).astype(int)
# Reorder columns to have the new columns between the original columns
columns_order = ['Gene'] + [f'NewColumn_{i}' for i in range(1, 8)] + [f'L{i}' for i in range(1, 8)]
df = df[columns_order]
# Save the result to a new CSV file
df.to_csv(output_file_path, index=False)



# revise the output file by removing useless columns and replacing 1 and 0 with TRUE and FALSE
import pandas as pd
# Read the CSV file
df = pd.read_csv('output.csv')
# Add a new column 'SelectedGenes' containing the names of genres with TRUE values, including 'Western'
df['SelectedGenes'] = df.apply(lambda row: ','.join([col for col in df.columns if row[col]]), axis=1)
# Display the updated DataFrame
print(df)
# Save the updated DataFrame to a new CSV file
df.to_csv('final output.csv', index=False)




import pandas as pd
from upsetplot import from_memberships
from upsetplot import UpSet
genes = pd.read_csv("final output.csv")
genes_by_line = from_memberships(genes.SelectedGenes.str.split(','), data=genes)
print(genes_by_line)
UpSet(genes_by_line, min_subset_size=15, show_counts=True).plot()
from matplotlib import pyplot
pyplot.show()
