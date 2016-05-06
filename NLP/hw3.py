
#Rachel Goodman
#!/usr/bin/python
import os
import sys
import glob
import math
import string
from collections import Counter
import operator

foutOne = open('bow-euclidean-tfidf-stopwords.txt.', 'w')
foutTwo = open('bow-cosine-tfidf-stopwords.txt.', 'w')

# ========== STOP WORDS ==========

def getStopWords(fin):
    return set([term.strip() for term in fin])

def removeStopWords(d, stopwords):
    for term in set(d.keys()):
        if term in stopwords:
            del d[term]

# ========== FREQUENCIES ==========

def getTermFrequencies(fin):
    tf = Counter()
    for line in fin: tf.update(map(lambda x: x.lower(), line.split()))
    return tf

def getDocumentFrequencies(tf):
    df = Counter()
    for d in tf: df.update(d.keys())
    return df

def getDocumentFrequency(df, term):
    if term in df: return df[term] + 1
    else: return 1

# ========== TF-IDF ==========

def getTFIDF(tf, df, dc):
    return tf * math.log(float(dc) / df)

def getTFIDFs(tf, df, dc):
    return [{k:getTFIDF(v, getDocumentFrequency(df,k), dc) for (k,v) in d.items()} for d in tf]

# ========== MEASUREMENTS ==========

def euclidean(d1, d2):
    s1 = set(d1.keys())
    s2 = set(d2.keys())
    t  = sum([(d1[k] - d2[k])**2 for k in s1.intersection(s2)])
    t += sum([d1[k]**2 for k in s1 - s2])
    t += sum([d2[k]**2 for k in s2 - s1])
    return math.sqrt(t)

    ###################################################
    ## TODO: implement cosine similarity ##
    ###################################################

def cosine(d1, d2):

    cos1 = Counter(d1)
    cos2 = Counter(d2)
    lms = list(set(cos1) | set(cos2))

    s3vect = [cos1.get(x, 0) for x in lms]
    s4vect = [cos2.get(y, 0) for y in lms]

    sum1 = sum(s3v*s3v for s3v in s3vect)
    sum2 = sum(s4v*s4v for s4v in s4vect)

    lens3 = math.sqrt(sum1)
    lens4 = math.sqrt(sum2)
    productof2 = lens3*lens4
    rg = sum(s3v*s4v for s3v,s4v in zip(s3vect,s4vect))

    cosine = rg/(productof2)
    return cosine
    # return 0;

# ========== EVALUATE ==========

def knn(trnFiles, devFiles, trnInsts, devInsts, sim, k, flag):
    correct = 0

    ###################################################
    ## TODO: implement k-neareast neighbor algorithm ##
    ###################################################

    # acc = 100.0 * correct / len(devFiles)
    # print '%30s: %5.2f (%d/%d)' % (flag, acc, correct, len(devFiles))
    #
    #


    if(cosine == sim):
        rach = len(devFiles)
        # dev = devFiles
        for a in range(rach):
           NextTo = []
           Distance = []
           Predict = [('BN',0),('CT',0),('WB',0),('NW',0),('AB',0),('AA',0),('BC',0)]

           for g in range(len(trnFiles)):

               dist = cosine(trnInsts[g], devInsts[a])
               Distance.append((trnFiles[g], dist))

           Distance.sort(key=operator.itemgetter(1))

           for r in range(k):
               change = 1-r
               currentLength = len(Distance)-change
               NextTo.append(Distance[currentLength][0])


               if(NextTo[r][0]=='B' and NextTo[r][1]=='N'):
                   Predict[3] = (Predict [3][0], Predict [3][1]+1)

               if(NextTo[r][0]=='C' and NextTo[r][1]=='T'):
                   Predict[4] = (Predict [4][0], Predict [4][1]+1)

               if(NextTo[r][0]=='W' and NextTo[r][1]=='B'):
                   Predict[6] = (Predict [6][0], Predict [6][1]+1)

               if(NextTo[r][0]=='N' and NextTo[r][1]=='W'):
                   Predict[5] = (Predict [5][0], Predict [5][1]+1)

               if(NextTo[r][0]=='A' and NextTo[r][1]=='B'):
                   Predict[1] = (Predict [1][0], Predict [1][1]+1)
               if(NextTo[r][0]=='A' and NextTo[r][1]=='A'):
                   Predict[0] = (Predict [0][0], Predict [0][1]+1)
               if(NextTo[r][0]=='B' and NextTo[r][1]=='C'):
                    Predict[2] = (Predict [2][0], Predict [2][1]+1)
           Predict.sort(key=operator.itemgetter(1))
           PredictioN = Predict[6][0]
           dev = devFiles[y][0] + devFiles[y][1]

           if(PredictioN == dev):
               correct = correct + 1

    if(sim == euclidean):
        for r in range(len(devFiles)):
           Distance = []
           NextTo2 = []
           Predict = [('BN',0),('CT',0),('WB',0),('NW',0),('AB',0),('AA',0),('BC',0)]
           for x in range(len(trnFiles)):
               dist = euclidean(trnInsts[x], devInsts[y])
               Distance.append((trnFiles[x], dist))
           Distance.sort(key=operator.itemgetter(1))


           for r in range(k):
               NextTo2.append(Distance[r][0])


               if(NextTo2[r][0]=='B' and NextTo2[r][1]=='N'):
                   Predict[3] = (Predict [3][0], Predict [3][1]+1)

               if(NextTo2[r][0]=='C' and NextTo2[r][1]=='T'):
                   Predict[4] = (Predict [4][0], Predict [4][1]+1)

               if(NextTo2[r][0]=='W' and NextTo2[r][1]=='B'):
                  Predict[6] = (Predict [6][0], Predict [6][1]+1)



               if(NextTo2[r][0]=='N' and NextTo2[r][1]=='W'):
                   Predict[5] = (Predict [5][0], Predict [5][1]+1)

               if(NextTo2[r][0]=='A' and NextTo2[r][1]=='B'):
                   Predict[1] = (Predict [1][0], Predict [1][1]+1)

               predictmod1 = NextTo2[r][0]=='A'
               predictmod2 = NextTo2[r][1]=='A'
               if(predictmod1 and predictmod2 ):
                   Predict[0] = (Predict [0][0], Predict [0][1]+1)


               if(NextTo2[r][0]=='B' and NextTo2[r][1]=='C'):
                   Predict[2] = (Predict [2][0], Predict [2][1]+1)



        Predict.sort(key=operator.itemgetter(1))
        pred2 = Predict[6][0]
        dev=devFiles[r][0] + devFiles[r][1]
        if(pred2 == dev):
               correct = correct + 1

    # rach = len(devFiles)
    full = 100.0
    acc = full * correct / rach
    print '%30s: %5.2f (%d/%d)' % (flag, acc, correct, rach)

    foutOne.close()
    foutTwo.close()

# ========== MAIN ==========

# ./hw3.py dat/train/ dat/dev/ stop-words_english_6_en.txt 50
TRN_DIR = sys.argv[1]
DEV_DIR = sys.argv[2]
SW_FILE = sys.argv[3]
K = int(sys.argv[4])

print 'Read training data:'
trnFiles = sorted(glob.glob(os.path.join(TRN_DIR,'*.txt')))
trnTF    = [getTermFrequencies(open(filename)) for filename in trnFiles]
trnDF    = getDocumentFrequencies(trnTF)
trnDC    = len(trnFiles) + 1
trnTFIDF = getTFIDFs(trnTF, trnDF, trnDC)
print '- # of documents : %d' % len(trnTF)
print '- # of term types: %d' % len(trnDF)

print '\nRead development data:'
devFiles = sorted(glob.glob(os.path.join(DEV_DIR,'*.txt')))
devTF = [getTermFrequencies(open(filename)) for filename in devFiles]
devTFIDF = getTFIDFs(devTF, trnDF, trnDC)
print '- # of documents : %d' % len(devTF)

print '\nRead stopwords:'
sw = getStopWords(open(SW_FILE))
print '- # of stopwords : %d' % len(sw)

print '\nEvaluate including stopwords'
trnFiles = map(os.path.basename, trnFiles)
devFiles = map(os.path.basename, devFiles)

knn(trnFiles, devFiles, trnTF   , devTF   , euclidean, K,   'bow-euclidean')
knn(trnFiles, devFiles, trnTFIDF, devTFIDF, euclidean, K, 'tfidf-euclidean')
knn(trnFiles, devFiles, trnTF   , devTF   , cosine   , K,      'bow-cosine')
knn(trnFiles, devFiles, trnTFIDF, devTFIDF, cosine   , K,    'tfidf-cosine')

print '\nEvaluate excluding stopwords'
for d in trnTF   : removeStopWords(d, sw)
for d in trnTFIDF: removeStopWords(d, sw)
for d in devTF   : removeStopWords(d, sw)
for d in devTFIDF: removeStopWords(d, sw)
removeStopWords(trnDF, sw)

knn(trnFiles, devFiles, trnTF   , devTF   , euclidean, K,   'bow-euclidean')
knn(trnFiles, devFiles, trnTFIDF, devTFIDF, euclidean, K, 'tfidf-euclidean')
knn(trnFiles, devFiles, trnTF   , devTF   , cosine   , K,      'bow-cosine')
knn(trnFiles, devFiles, trnTFIDF, devTFIDF, cosine   , K,    'tfidf-cosine')
