from reader_categorize import printAllCategories
from reader_categorize import getCategory
from reader_categorize import printCategories
#from reader_compare import getDiff
from reader_search import search_str

fna_path = "example_data.fna"
searchVal1 = "23352"
searchVal2 = "rap1 GTPase-activating protein 1 isoform 5"

#printAllCategories(fna_path)
searchedGeneLine1 = search_str(fna_path, searchVal1, 21, "output1")
searchedGeneLine2 = search_str(fna_path, searchVal2, 21, "output1")
#print(searchedGeneLine1)
#print(searchedGeneLine2)
#printCategories(fna_path, searchedGeneLine1)
#print("gene", searchedGeneLine1, "\'s protein:", getCategory(fna_path, searchedGeneLine1, "protein"))
#print(f"Similarity rate: {getDiff(searchedGeneLine1, searchedGeneLine2, fna_path, True):.2f}%")
