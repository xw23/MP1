import metapy

def tokens_lowercase(doc):
    #Write a token stream that tokenizes with ICUTokenizer (use the argument "suppress_tags=True"), 
    #lowercases, removes words with less than 2 and more than 5  characters
    #performs stemming and creates trigrams (name the final call to ana.analyze as "trigrams")
    

    '''Place your code here'''

    tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)

    tok = metapy.analyzers.LowercaseFilter(tok)

    tok = metapy.analyzers.LengthFilter(tok, min=2, max=5)

    #tok = metapy.analyzers.ListFilter(tok,
    #                                  "lemur-stopwords.txt",
    #                metapy.analyzers.ListFilter.Type.Reject)
                   ####  Remove  STOP Words

    tok = metapy.analyzers.Porter2Filter(tok)


    ## tok = metapy.analyzers.CharacterTokenizer()
                      ####  CHARs  not  words

    ana = metapy.analyzers.NGramWordAnalyzer(3, tok)

    trigrams = ana.analyze(doc)

    #print(trigrams)

    #print("\n\n")
    
    
    #leave the rest of the code as is
    tok.set_content(doc.content())
    tokens, counts = [], []
    for token, count in trigrams.items():
        counts.append(count)
        tokens.append(token)

##    tokens = []
##    for token in tok:
##        tokens.append(token)
    
    return tokens


    
if __name__ == '__main__':
    
    doc = metapy.index.Document()
    
    # doc.content("I SAID that I Can't BELieve THAT it only costs $19.95! I could only find it for MORE THAN $30 BEfore.")
    doc.content("I said that I can't believe that it only costs $19.95! I could only find it for more than $30 before.")

    print(doc.content())
         #you can access the document string with .content()

    tokens = tokens_lowercase(doc)
    print(tokens)









