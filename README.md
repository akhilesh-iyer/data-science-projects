Objective of this document is to explain methodology adopted to perform text analysis to drive sentimental opinion, sentiment scores, readability, passive words, personal pronouns, etc. Sentimental analysis is the process of determining whether a piece of writing is positive, negative, or neutral. The below Algorithm is designed for use in Financial Texts. It consists of steps:
	
1)	Cleaning using Stop Words and Dictionary Lists
The Stop Words Lists (found in the folder StopWords) are used to clean the text so that Sentiment Analysis can be performed by excluding the words found in Stop Words List. The Dictionary (found in the folder Dictionary) is used for creating a dictionary of Positive and Negative words. We add only those words in the dictionary if they are not found in the Stop Words Lists. Complex words are words in the text that contain more than two syllables.
			
2) Formulae

	1) Positive Score: This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.
	2) Negative Score: This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.
	3) Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
	4) Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
	5) Average Sentence Length = the number of words / the number of sentences
	6) Percentage of Complex words = the number of complex words / the number of words 
	7) Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)
	8) Average Number of Words Per Sentence = the total number of words / the total number of sentences
	9) Word Count
	10)	Syllable Count Per Word
	11)	Personal Pronouns
	12) Average Word Length = Sum of the total number of characters in each word/Total number of words
