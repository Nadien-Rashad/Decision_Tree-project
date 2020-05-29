no = 0
    please = 0
    thank = 0
    apologize = 0
    bad = 0
    clean = 0
    comfortable = 0
    dirty = 0
    enjoyed = 0
    friendly = 0
    glad = 0
    good = 0
    great = 0
    happy = 0
    hot = 0
    issues = 0
    nice = 0
    noise = 0
    old = 0
    poor = 0
    right = 0
    small = 0
    smell = 0
    sorry = 0
    wonderful = 0
    reviewsText = ''
    rating = ''

    review_words = ['no', 'please', 'thank', 'apologize', 'bad', 'clean', 'comfortable', 'dirty', 'enjoyed', 'friendly',
                    'glad', 'good', 'great', 'happy', 'hot', 'issues', 'nice', 'noise', 'old', 'poor', 'right', 'small',
                    'smell', 'sorry', 'wonderful']
    Review = input("Please enter the review:")
    Review= Review.lower()
    Review = Review.replace(',', ' ')
    list_of_review = []
    list_of_review = Review.split()
    the_row = []
    list3 = set(list_of_review) & set(review_words)  # we don't need to list3 to actually be a list

    list4 = sorted(list3, key=lambda k: review_words.index(k))


    for item in list4:
        if item == "no":
            no = 1
        elif item == "please":
            please = 1
        elif item == "thank":
            thank = 1
        elif item == "apologize":
            apologize = 1
        elif item == "bad":
            bad = 1
        elif item == "clean":
            clean = 1
        elif item == "dirty":
            dirty = 1
        elif item == "comfortable":
            comfortable = 1
        elif item == "enjoyed":
            enjoyed = 1
        elif item == "friendly":
            friendly = 1
        elif item == "glad":
            glad = 1
        elif item == "good":
            good = 1
        elif item == "great":
            great = 1
        elif item == "happy":
            happy = 1
        elif item == "hot":
            hot = 1
        elif item == "issues":
            issues = 1
        elif item == "nice":
            nice = 1
        elif item == "noise":
            noise = 1
        elif item == "old":
            old = 1
        elif item == "poor":
            poor = 1
        elif item == "right":
            right = 1
        elif item == "small":
            small = 1
        elif item == "smell":
            smell = 1
        elif item == "sorry":
            sorry = 1
        elif item == "wonderful":
            wonderful = 1

    the_roww = []
    the_roww.append([no, please, thank, apologize, bad, clean, comfortable, dirty, enjoyed, friendly, glad, good, great,
                     happy, hot, issues, nice, noise, old, poor, right, small, smell, sorry,
                     wonderful,reviewsText,rating])

    rows = []
    i = 0
    for row in the_roww:
        rows.extend(arrange(row, tree))

    print(f' Your review is  {rows}')
