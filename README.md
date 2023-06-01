<h1>Random Book Name Generator in Python</h1>

<h2>Description</h2>
A fun and simple Python programme that generates a social media handle name, book title or other titular forms based off a given list of desired words / numbers.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 

<h2>Environments Used </h2>

- <b>PyCharm CE</b>
- <b>MacOS 12.5</b> 


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 

<h2>Environments Used </h2>

- <b>PyCharm CE</b>
- <b>MacOS 12.5</b> 

<h2>Program walk-through:</h2>

<p align="center">
<img src="https://imgur.com/OTs4Grv.png" height="80%" width="80%" 
<br />
<br />
1. Import the Random function.
<br />
  <br />
2. Make a list of desired words / cool words you would like included in your name. Call this 'good_word'.
<br />
  <br />
3. Use the Try and Except functions to ensure that, if a user were to enter an incorrect input to the question (e.g if they typed in 'M' by mistake instead of a number) that generates a ValueError, the programme will automatically select a set number of words for them. 
<br />
  <br />
4. Use the random.shuffle function of your list to randomly shuffle the order of words.
<br />
  <br />
5. Create a 'book name list'. This is the alphabetical part of your book name. Put in your 'good_word'list, use [] to show the range of words from 0 to 'numword' (i.e the number of words your user said they wanted in their name)
<br />
  <br />
6. Use the For loop to get a random number. Range is 0 to 'numnum' (i.e the number of numbers your user said they wanted in their name.) Call 'ran' to randomly choose numbers. random.randint gives a random integer. (0,100) gives the range of numbers the programme will choose from. Then append it to the book_name (but make sure you have converted the integer to a string. To do this, use () and put str(ran). This converts the random numbers earlier to a string.
  <br />
  <br />
7. Finally, create a new list titled final_name'. Use ' ' to include a space before your book name. If you want the first letter of each word capitalized, use the str.title(final_name). This is why there is a final_final list. Finally, use the Format to print: (f'Your suggested book name is {final_final}')

                                                               
