'''
Author: XPectuer
LastEditor: XPectuer

replacement program
input:  file with:
          1. <img src="" alt="" />
          2. ![](/path/to/images)
 output: {{< pic src=""  alt="" >}}

method:
1. find the tags
2. fetch the parameters
3. replace with 
'''
import sys
import os
import re 
import markdown
from collections import deque
from bs4 import BeautifulSoup


prefix = "/posts/compilers/static-analysis/data-flow-analysis/images/"

def process_src(src):
    return prefix+src


def find_img_tag(text):
    img_tag = re.compile("<img.*")
    result = img_tag.match(text)
    return result


#print(my_tag)

# string for test

# html = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#        <img src="wwww" alt="www"/>
#    <img src="wwww1" alt="www1"/>
#    <img src="wwww2" alt="www2"/>
#    <img src="wwww3" alt="www3"/>
# </body>
# </html>
# """



def replace_img_tag(html):
    soup = BeautifulSoup(html,'html.parser')
    # main loop
    for tag in soup.find_all('img'):
        src = tag.attrs['src']
        alt = tag.attrs['alt']

        src = process_src(src)

    #  print(src,alt)
        my_tag = "{{{{< pic src=\"{src}\"  alt=\"{alt}\" >}}}}".format(src=src, alt=alt)
        
        tag.insert_before(my_tag)
        tag.extract()
    # print("inserted:",my_tag)
    #print(soup.prettify(formatter=None)) 
        return soup.prettify(encoding=str,formatter=None)


def replace_markdown_tag(text):
    re_str =  r"!\[.*?\]\(.*?\)"
    res =  re.findall(re_str,text)
    print(len(res))
    html = markdown.markdown(text=text)
    soup = BeautifulSoup(html,'html.parser')

    imgs = soup.find_all("img")
    my_tags = deque()

    # extract attrs
    for img in imgs:
        my_tag = "\r {{{{< pic src=\"{src}\"  alt=\"{alt}\" >}}}} \r".format(src=img.attrs['src'], alt=img.attrs['alt'])
        my_tags.append(my_tag)
    #print(my_tags)

    for e in res:
        text = text.replace(e, my_tags.popleft())
             

    print(text)



if __name__ == '__main__':


    filename = sys.argv[1]
    path = os.path.abspath("./"+filename)
    with open(path,'r') as f:
        html = f.read()
        
    

    
    src = "path/to/pic"
    alt = "this is an alt text"
    #my_tag = "\r{{{{< pic src=\"{src}\"  alt=\"{alt}\" >}}}}\r".format(src=src, alt=alt)



    #replace_img_tag(html)
    #print(type(text))
    replace_markdown_tag(html)    
    




# https://stackoverflow.com/questions/5466451/how-can-i-print-literal-curly-brace-characters-in-a-string-and-also-use-format

#print(find_img_tag(html))


#print(my_tag)
