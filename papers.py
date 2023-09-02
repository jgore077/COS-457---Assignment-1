from bs4 import BeautifulSoup
import re
import csv

PATH_TO_PAPERS ='papers/01/'
PAGES=10
START=10000
MAX_PAGES=2748

# Simple class for storing basic info
class Paper():
    def __init__(self,title:str,authors:str,abstract:str,keywords:str):
        self.title=title
        self.authors=authors
        self.abstract=abstract
        self.keywords=keywords


# Simple function to turn a paper into a tsv row
def turn_into_tsv_row(paper:Paper):
    return paper.title+"\t"+paper.authors+"\t"+paper.abstract+"\t"+paper.keywords+"\n"

# Function for testing the csv file
def read_tsv_and_label(input_file):
    labeled_data = []
    
    with open(input_file, "r",encoding='UTF-8') as tsv_file:
        for line in tsv_file:
            fields = line.strip().split("\t")
            labeled_row = {
                "Title": fields[0],
                "Authors": fields[1],
                "Abstract": fields[2],
                "Keywords": fields[3]
            }
            labeled_data.append(labeled_row)
    return labeled_data


# Opening tsv file
with open("papers.tsv","w",encoding='UTF-8', newline='') as tsv:
    # Creating a loop to generated the number found in the PATH_TO_PAPERS dir
    for page_num in range(0,PAGES+1):
        
        paper = Paper('None','None','None','None')
        
        # Opening a document using the PATH_TO_PAPERS and the num from the outerloop, START is equal to 10000 I.E the first document
        with open(f"{PATH_TO_PAPERS}2101.{START+page_num}.html", encoding='UTF-8',) as file:

                '''
                This block creates a beatiful soup reader with the file opened in the line above this comment
                Every attribute is searched for with only the find command instead of find_all because most documents only had 1 of the tags
                If the searched returned None, no text will be extracted because it will throw an exception
                There are also some regular expressions to remove tabs & newlines as they interfere with the tsv
                I also turned the strings into a single line with the "".join(<string>.splitlines())
                '''
                soup = BeautifulSoup(file, "html.parser")
                paper.title=(soup.find('title').text).strip()
                authors=soup.find(class_="ltx_authors")
                if authors!=None:
                    paper.authors="".join(re.sub(r"[\n\t]*", "",authors.text).splitlines())
                abstract = soup.find(class_="ltx_abstract")
                if abstract!=None:
                    paper.abstract="".join(re.sub(r"[\n\t]*", "",abstract.text).splitlines())
                keywords= soup.find(class_="ltx_keywords")
                if keywords!=None:
                    paper.keywords="".join(re.sub(r"[\n\t]*", "",keywords.text).splitlines())

                tsv.write(turn_into_tsv_row(paper))
    
                




for row in read_tsv_and_label('papers.tsv'):
    print("1:", row["Title"])
    print("2:", row["Authors"])
    print("3:", row["Abstract"])
    print("4:", row["Keywords"])
    print()