from bs4 import BeautifulSoup
import re
import csv

PATH_TO_PAPERS ='papers/01/'
PAGES=10
START=10000
MAX_PAGES=2748


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
    
    with open(input_file, "r",encoding='UTF-8', newline='') as tsv_file:
        for line in tsv_file:
            fields = line.strip().split("\t")
            if len(fields) == 4:
                labeled_row = {
                    "Title": fields[0],
                    "Authors": fields[1],
                    "Abstract": fields[2],
                    "Keywords": fields[3]
                }
                labeled_data.append(labeled_row)
    return labeled_data



with open("papers.tsv","w",encoding='UTF-8', newline='') as tsv:

    for page_num in range(0,MAX_PAGES+1):
        paper = Paper('None','None','None','None')

        with open(f"{PATH_TO_PAPERS}2101.{START+page_num}.html", encoding='UTF-8',) as file:


                soup = BeautifulSoup(file, "html.parser")
                paper.title=(soup.find('title').text).strip()
                authors=soup.find(class_="ltx_authors")
                if authors!=None:
                    paper.authors=re.sub(r"[\n\t]*", "",authors.text)
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