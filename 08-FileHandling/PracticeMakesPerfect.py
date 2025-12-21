import re


##########              PRACTICE MAKES PERFECT               ##########

# 5. regular expressions - email

# def read_email_content(filename):
#     try:
#         with open (filename,'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         return ""


# # 1.Nadawca
# def email_sender(email_content):
#     match = re.search(r"From:.*<(.+)>", email_content)
#     if match:
#         return match.group(1)
#     return None

# # 2.Odbiorca
# def email_recipient(email_content):
#     match = re.search(r"To:.*<(.+)>", email_content)
#     if match:
#         return match.group(1)
#     return None

# # 3.Temat
# def email_subject(email_content):
#     match = re.search(r"Subject: (.+)", email_content)
#     if match:
#         return match.group(1)
#     return None

# # 4.tresc
# def email_body(email_content):
#     match = re.search(r"\n\n(.+)", email_content, re.DOTALL)
#     if match:
#         return match.group(1)
#     return None

# if __name__ == "__main__":

#     email_text = """ Return-Path: <jan.kowalski@example.com>
# Received: from mail.example.com (mail.example.com [192.168.1.100])
#     by smtp.example.com (Postfix) with ESMTP id ABC12345
#     for <anna.nowak@example.com>; Tue, 8 Oct 2024 14:32:15 +0200 (CEST)
# Received: from [192.168.1.10] (unknown [192.168.1.10])
#     by mail.example.com (Postfix) with ESMTPSA id DEF67890
#     for <anna.nowak@example.com>; Tue, 8 Oct 2024 14:32:14 +0200 (CEST)
# Message-ID: <20241008143214.DEF67890@mail.example.com>
# Date: Tue, 8 Oct 2024 14:32:14 +0200
# From: Jan Kowalski <jan.kowalski@example.com>
# To: Anna Nowak <anna.nowak@example.com>
# Subject: Report request
# MIME-Version: 1.0
# Content-Type: text/plain; charset="UTF-8"
# Content-Transfer-Encoding: 7bit

# Hi Anna,

# I hope everything is going well with you.
# I wanted to ask, have you managed to prepare
# the sales report for September yet?

# I need it by the end of the week, Friday,
# October 11, 2024.

# Please let me know if you have any questions.

# Best regards,
# Jan Kowalski
# jan.kowalski@example.com
# +48 123 456 789
# """
#     print(f"sender: {email_sender(email_text)}")
#     print(f"recipient: {email_recipient(email_text)}")
#     print(f"subject: {email_subject(email_text)}")
#     print(f"body: {email_body(email_text)}")



##########              PRACTICE MAKES PERFECT               ##########


# # 6.


# def read_content_and_do_smth(filename):
#     try:
#         with open(filename,'r',encoding="utf-8") as file:
#             content = file.read()

#             #1. liczba znakow
#             num_chars = len(content)

#             #2. liczba lini
#             lines = content.splitlines()
#             num_lines = len(lines)

#             #3. liczba slow
#             words = content.split()
#             num_words = len(words)

#             print(f"File name: {filename}")
#             print(f"Number of lines: {num_lines}")
#             print(f"Number of characters: {num_chars}")
#             print(f"Number of words: {num_words}")


            
#     except FileNotFoundError:
#         return ""
    
# (read_content_and_do_smth("report.txt"))


##########              PRACTICE MAKES PERFECT               ##########

# # 7.


# text = input("Podaj jakis tekscik, wyliczymy ile ma samoglosek: ")

# def calculate_vowels(text):

#     match = re.findall(r"[aeiouyAEIOUY]", text)
#     if match:
#         return len(match)
#     return None


# print(calculate_vowels(text))


##########              PRACTICE MAKES PERFECT               ##########

# # 8.

# # \w{4}$


# def read_content_and_extensions(filename):
#     try:
#         with open(filename,"r") as file:
#             content = file.read()
#             pattern = r"\.\w{4}$"
#             matches = re.findall(pattern,content, re.MULTILINE)

#             return matches
#     except FileNotFoundError:
#         return ""
    
# print(read_content_and_extensions("files.txt"))





##########              PRACTICE MAKES PERFECT               ##########


# # 9. 
# import csv

# with open ("it_company.csv",mode = "r", newline='') as csvfile:
#     worker_reader = csv.DictReader(csvfile)
#     for row in worker_reader:
#             if row["Job Title"] == "Graphic Designer":
#                 print(f"{row['First Name']} {row['Last Name']},{row['Email']}")



##########              PRACTICE MAKES PERFECT               ##########

# 10.


# import csv

# with open("clothing.csv", mode = "r", newline='') as csvfile:
#     clothes = csv.DictReader(csvfile)
#     for row in clothes:
#         if float(row['Price']) < 60 and int(row['Stock_Quantity']) < 40:
#             print(f"{row['Product_Name']}")




##########              PRACTICE MAKES PERFECT               ##########


# # 11.

# # Name of the file to write to
# file_name = 'numbers_and_powers.txt'

# # Writing movie details to the file
# with open(file_name, 'w') as file:
#     for i in range (1,101):
#        file.write(f"{i},{i*i},{i*i*i}")
#        file.write("\n")


##########              PRACTICE MAKES PERFECT               ##########

# 12. 

import csv

with open("books.csv", mode= "r", newline=" ") as csvfile:
    books = csv.DictReader(csvfile)
    for row in books:
        if row["Genre"] == "Fantasy":
            books_fantasy.write(row)
