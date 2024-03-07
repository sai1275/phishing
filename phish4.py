# data collection
import requests as re
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

# unstructured to structured
from bs4 import BeautifulSoup
import pandas as pd
import phish3 as fe

disable_warnings(InsecureRequestWarning)

# Step 1: csv to dataframe
URL_file_name = "Book3.csv"
data_frame = pd.read_csv(URL_file_name)

# retrieve only "url" column and convert it to a list
URL_list = list(data_frame['URL'])

# restrict the URL count
collection_list = URL_list

# only for the legitimate
#tag = "http://"
#collection_list = [tag + url for url in collection_list]


# function to scrape the content of the URL and convert to a structured form for each
def create_structured_data(url_list):
    data_list = []
    for i in range(0, len(url_list)):
        try:
            response = re.get(url_list[i], verify=False, timeout=4)
            soup = BeautifulSoup(response.content, "html.parser")
            vector = fe.create_vector(soup)
            vector.append(str(url_list[i]))
            data_list.append(vector)
        except re.exceptions.RequestException as e:
            print(i, " --> ", e)
            continue
    return data_list


data = create_structured_data(collection_list)

columns = [
    'has_title',
    'has_input',
    'has_button',
    'has_image',
    'has_submit',
    'has_link',
    'has_password',
    'has_email_input',
    'has_hidden_element',
    'has_audio',
    'has_video',
    'number_of_inputs',
    'number_of_buttons',
    'number_of_images',
    'number_of_option',
    'number_of_list',
    'number_of_th',
    'number_of_tr',
    'number_of_href',
    'number_of_paragraph',
    'number_of_script',
    'length_of_title',
    'has_h1',
    'has_h2',
    'has_h3',
    'length_of_text',
    'number_of_clickable_button',
    'number_of_a',
    'number_of_img',
    'number_of_div',
    'number_of_figure',
    'has_footer',
    'has_form',
    'has_text_area',
    'has_iframe',
    'has_text_input',
    'number_of_meta',
    'has_nav',
    'has_object',
    'has_picture',
    'number_of_sources',
    'number_of_span',
    'number_of_table',
    'URL'
]

df = pd.DataFrame(data=data, columns=columns)

# labelling
df['label'] = 0

df.to_csv("restart1bad.csv")  # header should be false after the first run