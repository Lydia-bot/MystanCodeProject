"""
File: rotten_tomato.py
Name:
-------------------------------
This file shows basic AI in classification task:
movie review classification.
First, tokenize the review
Second, count each token and give them corresponding scores
Finally, calculate the score for each word such that we can
predict a movie review by summing over the scores
"""


# The file with labels and reviews
FILENAME = 'movie_review.txt'


def main():
	with open(FILENAME, 'r') as f:
		d = {}
		for line in f:
			score, review = line.split(':')
			if score[1] == '+':
				real_score = 1
			else:
				real_score = -1
			tokens = review.split()
			for token in tokens:
				token = string_manipulation(token)
				if token not in d:
					d[token] = real_score
				else:
					d[token] += real_score
		print(d)

	a = [0]
	a[0] += 1
	print(a)


def string_manipulation(token):
	ans = ''
	for ch in token:
		if ch.isalpha():
			ans += ch.lower()
	return ans


if __name__ == '__main__':
	main()
