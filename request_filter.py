
def filter_data(data):
    feeds = ["feed_a","feed_b","feed_c"]
    i = 0
    for feed in feeds:
        data[feed] = i
        i+= 1
        print("Adding to data feeds")
    return(data)
