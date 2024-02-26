# WordleBot

## Overview
Using Python and the Selenium framework, WordleBot is an automated Wordle solver that averages around 3.8 guesses per game. 

This project was made with the help of my friend [Borui](https://github.com/chenborui1?tab=repositories) who helped write and teach me about the algorithms involved in solving Wordle efficiently. His project goes further and involves a ton of deeper information theory concepts to solve Wordle on Hard mode whereas mine is only capable of solving it on Normal.

I decided it would be fun to add some sort of automation component to this I was more interested in that aspect for a project like this, so I decided to use Selenium to interact with the browser and read elements for outputs. Reading the output is specific to this Wordle site, as each one uses different HTML/CSS and stores the information differently depending on letter states, but the concept is the same.

In the future, I plan on updating the benchmarking method that was used previously before the process was automated and working on documentation.

## Addendums
Make sure you have the following installed on your machine:

- Python 3.x
- Selenium
- Chrome WebDriver 
  - Since Chrome is now updated past the Chrome WebDriver's latest release, you can find download links for the current Chrome Browser [here](https://googlechromelabs.github.io/chrome-for-testing/).




