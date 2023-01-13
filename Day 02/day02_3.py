# Chapter 4 if
#limits = 20
#tweets = "pass" * 4
#if limits - len(tweets) >= 0:
#    print(tweets)
#else:
#    print("제한 글자수 초과")

# Walrus
tweet_limit = 199
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print(f"Went over by {abs(diff)}")

# Chapter 5 바로 전까지 진도 끝

import random
limits = 20
tweets = "pass" * random.randint(1,10) # 1에서 10 사이 상의 정수가 임의로 발생
diff = limits - len(tweets)
if diff >= 0:
    print(tweets)
else:
    print(f'글자 수 {abs(diff)}자수 초과')