from wordcloud import  WordCloud, STOPWORDS

comment_word = ' '
stopwords = set(STOPWORDS)

f=open('files.txt', 'r+')
textdata=f.read().replace('\n','')

wordcloud = WordCloud(width=800,
                      height=800,
                      background_color='skyblue',
                      stopwords=stopwords, min_font_size=10).generate(textdata)

wordcloud.to_file('Image1.png')
print('Image Saved Successfully')
