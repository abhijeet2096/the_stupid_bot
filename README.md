# the_stupid_bot
A telegram bot for telling institute vehicle schedule available @the_stupid_bot

****
## Software Stack used
1. [Python telegram Wrapper](https://github.com/python-telegram-bot/python-telegram-bot)

2. [Spacy](https://spacy.io/)  

3. [Tabula-py](https://github.com/chezou/tabula-py/)

4. [MySQL](https://www.mysql.com/)

****
##  Background and motivation
The motivation to do this project was from my day to day life. Our institute vehicle schedule changes every month and every time to see a bus timing , i have to open the vehicle schedule and then search for an appropriate bus. So one day i thought why not, a bot that could do this thing for me. At the same time i received a mail from our faculty for hackathon'18, so i thought why not put this project as an entry for this competition.
 ****
## Project summary
The Project can be divided into three parts, viz:
1. Extracting Vehicle schedule from a PDF to MySQL database.
2. Process the input from user programmatically using some NLP framework.
3. Applying appropriate query after the input and  sending the response back.

let's discuss each part briefly

**Extracting Data** : As you may know the pdf format was only created to provide a universal format to print documents and nothing else, which makes the extraction of data from pdf difficult. Thanks to [Tabula](http://tabula.technology/) tool , i was able to extract tables from our schedule pdf file. The extraction of data from pdf file involves a intermediate step i.e "csv" , this csv file is then processed by another custom python script which changes the format of schedule from 12-hr format to 24-hr format. After this update the pdf is imported to a MySQL database.

**NLP** : Due to very short time duration of this project, i have used NLP tokenization to process the user input, intially our system can process only some proper sentences as it extracts nouns from the sentences. Future work should be focused in this part.

**Response** :  After getting appropriate intended meaning of sentence the system applies appropriate predefined query and sends back the data to the user.
****
## Block diagram
![Block Diagram](/resources/the_stupid_bot.jpg?raw=true "Block Diagram")
****
## Results
here is a screenshot attached

![Sample screenshot](/resources/sample.jpg?raw=true "Sample")

****
## About
The Project is an entry for hackathon'18 at IIT Mandi
****

## Future work
1. Adding Smart Contact Support.
2. Better N.L.P Support.

## Contributors

[Abhijeet sharma](http://students.iitmandi.ac.in/~abhijeet_sharma)
1. Github: http://github.com/abhijeet2096
2. Email: sharma.abhijeet2096@gmail.com
3. Mobile: +91-8629015433
****
## References

1. https://github.com/python-telegram-bot/python-telegram-bot#learning-by-example
2. https://core.telegram.org/
