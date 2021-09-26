# EC601-project-2

Twitter API Keys:
The first necessary step is to have a Twitter account and get the necessary credentials on the Twitter developer platform to access the Twitter API.
By registration on https://developer.twitter.com/ I have got the four necessary authentication codes:

Access Token
1441894841265262595-ZNbKjnV8LIQCz0C6ntVHpXGoOKPJ5j

Access Token Secret
T18zEtLLq1JoqoPVLeE56TLb1WVOC5qCge6NS7NFJDvHZ

API Key
lGhEtjifVUr7xyM7U6xrD8EqQ

API Key Secret
WNc81uNSrSH5vzqT93pSAjtFdVivSt3zOBYaaIN6C4qwJpe4s5

Then create an Auther Client connection.

From twitter API url can be obtained:
https://api.twitter.com/1.1/search/tweets.json

Remove retweets from the extraction results and filter all replies to tweets, which are often unnecessary for analysis.

None of tweets to be retrieved per one call and parameters according to twitter API.

We retrieve tweets in the number of 100 since it is the maximum amount for one-time search.

In the document there are some examples I tried.


Author:
Yi Xiang U42741183
