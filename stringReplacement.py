def filter(tweet):
	tweet = tweet.lower().split()
	print tweet
	for i in range(0, len(tweet)-1):
		if tweet[i] == "witnesses":
			tweet[i] = "these dudes i know"

		elif tweet[i] == "allegedly":
			tweet[i] = "kinda probably"

		elif tweet[i] == "rebuild":
			tweet[i] = "avenge"

		elif tweet[i] == "space":
			tweet[i] = "spaaqce"

		elif tweet[i] == "smartphone":
			tweet[i] = "pokedex"

		elif tweet[i] == "electric":
			tweet[i] = "atomic"

		elif tweet[i] == "car":
			tweet[i] = "cat"

		elif tweet[i] == "election":
			tweet[i] = "eating contest"

		elif tweet[i] == "car":
			tweet[i] = "cat"

		elif tweet[i] == "senator":
			tweet[i] = "elf-lord"

		elif tweet[i] == "president":
			tweet[i] = "self proclaimed leader"

		elif tweet[i] == "donald":
			if tweet[i+1] == "trump":
				tweet[i] = ""
				tweet[i+1] = "leader of the free world"
			else:
				tweet[i] = "leader of the free world"

		elif tweet[i] == "president":
			tweet[i] = "self proclaimed leader"

	return " ".join(tweet)


print filter("w sdfs Donald trump kjasnf kbksd allegedly")