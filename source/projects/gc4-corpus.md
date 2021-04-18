# GC4 Corpus
The German colossal, cleaned Common Crawl corpus.

This is a German text corpus which is based on [Common Crawl](https://commoncrawl.org/). It has been cleaned up and preprocessed and can be used for various tasks in the NLP field. For example, for the self-supervised training of language models.

GC4 has been created by [**Philipp Reißel**](https://www.reissel.eu) from [ambeRoad](https://amberoad.de/) with support from [Philip May](https://may.la/). Many thanks to [iisys](https://www.iisys.de/) (the Institute of Information Systems Hof University) for hosting this dataset.

**For [download](#download) scroll way down.**

In a very simplified matter one can say:

- **HEAD**: Consists of high quality text (e.g. newspaper, government websites)
- **MIDDLE**: More colloquial language like forum entries, commentary sections
- TAIL: The dark side of the Internet

As it is classified through n-gram occurrences in comparison with the German wikipedia n-gram from our practical experience it worked quite well.

## Preprocessing
Preprocessing was done through the [cc_net library](https://github.com/facebookresearch/cc_net)

| CC Dump                       | Total Size: German tail + middle + head  (before dedup)      | CC Original Size (TB) |
| ----------------------------- | ------------------------------------------------------------ | --------------------- |
| 2015-22 (2015-27 not working) | stopped                                                      |                       |
| 2015-48                       | 8.9 GB                                                       | 151                   |
| 2016-18                       | 17.7 GB                                                      |                       |
| 2016-44                       | 119 GB                                                       |                       |
| 2017-13                       | 84 GB                                                        | March 250             |
| 2017-30                       | ~80 GB                                                       |                       |
| 2017-39                       | 75.6 GB                                                      | September 250         |
| 2017-51                       | ~120 GB                                                      | December 240          |
| 2018-09                       | 128 GB                                                       | Februrary 270         |
| 2018-17                       | ~120-130 GB                                                  | April 230             |
| 2018-30                       | 131 GB                                                       | July 255              |
| 2018-39                       | ~120 GB                                                      | September 220         |
| 2018-51                       | ~120 GB                                                      | December 250          |
| 2019-09                       | 119.8 GB                                                     | February              |
| 2019-18                       | 119 GB                                                       | April 198           |
| 2019-30                       | 120 GB                                                       |                       |
| 2019-47                       | 150.2 GB                                                     | November              |
| 2020-10                       | 134 GB                                                       | February 240          |
| 2020-34 / 2020-29             | NOT WORKING ENCODING ISSUE - see [issue](https://github.com/facebookresearch/cc_net/issues/16) | August 235            |

This preprocessing is filtering duplicates only inside the same dump. This step took approx. 50,000 CPU hours and 400 TB of network traffic to the common crawl s3 bucket.

## Common Crawl News Dataset
You can convert the Common Crawl News Shards with a WARC to WET library and then feed to cc_net just as the normal Common Crawl dumps.

Given the average sizes of the hourly News shards:

- WARC: 1100 mb
- WARC -> WET: 124mb
- Filtering WET for german only: 2.6 mb
- Head only (highest quality): 0.8 mb

One can approximate that all news shards combined are just the extent of one monthly common crawl. As large portions of news articles are already included, we decided to not include this because of the low overall quantity.

## Clean-Up
To also delete duplicates which occur in more than one Common Crawl dump, we did a deduplication through mongoDB. The Code is available [here](https://github.com/German-NLP-Group/german-transformer-training/tree/master/Hashing)

It requires approx 1+ TB of RAM and at least 64+ CPUs to complete the task in ~3 days.

The tail section is not further processed, as these are nearly always scam/porn websites.

This table sums up the sizes of all preprocessed monthly dumps and 2 different approaches of deduplication:

-  Deduplication through similar Text:
  - Every content field is hashed and same hashes are removed
  - Problem here is that urls are included multiple times when very little change on the website has happend (e.g. just the year in the imprint has changed)
  - This approach filters out webpages which are copied/mirrored (e.g. there are a lot of wikipedia mirrors out there)
-  **Deduplication through similar Text and URLs**:
  - To avoid having sites with the same URL from different monthly dumps in more strict filtering we filtered out every URL that appeared twice
  - One edge case which we couldn't solve, were URLs were a hashed parameter is appended, but this is pretty rare

| Size here is with metadata but compressed<br/>as .gz so raw text is approx. 2x the given size | Head<br/>pages/size  | Middle<br/>pages/size          | Tail<br/>pages/size         |
| ------------------------------------------------------------ | ---------------- | -------------------------- | ------------ |
| Original                                                     | 263 Mio<br/>392 GB | 332 Mio<br/>499 GB           | ------<br/>1 TB |
| Deduplication through similar Text<br/>(available on request)    | 181 Mio<br/>294 GB | 251 Mio<br/>not yet exported |              |
| **Deduplication through similar Text and URLs**<br/>(this is the one you can download here) | 142 Mio<br/>194 GB | 186 Mio<br/>254 GB           |              |

## Comparison to other Datasets which are based on Common Crawl and very large
- C4/mC4 Dataset used by Google:
  - Multilingual one is only available on request (see issue [here](https://github.com/allenai/allennlp/discussions/5056))
  - As the English only is already a requester pays, it requires you to have approx. 100 $ of Google Cloud Credits
  - The way of filtering here is different (and in our mind inferior to [cc_net library](https://github.com/facebookresearch/cc_net)
    - They doesn't split for quality like cc_net
    - Filtering out every article were one swearword occures, so your models can't learn at all how to deal with them
- CC100 [download here](http://data.statmt.org/cc-100/)
  - This data is also preprocessed with cc_net
  - But only dumps from January-December 2018 are used, so a lack of size and temporal diversity
- [ORCAS dataset ](https://oscar-corpus.com/)
  - It only uses one monthly dump (November 2018) from Common Crawl
  - The filtering for quality seems to be less precise than cc_net

## Terms of Use
Since this dataset is based on [Common Crawl](https://commoncrawl.org/) we would like to just refer to their [terms of use](https://commoncrawl.org/terms-of-use/). Nevertheless, we would like to ask you to publish the work based on it under open source license. Although this is not mandatory.

## Download
The corpus is split into multiple files. Below are links to each single archive.

Instead of downloading the single links you can download two files with all URLs and then use `wget` to download the single archives:

```bash
wget https://german-nlp-group.github.io/_static/file/gc4_corpus_head_urls.txt
wget -i gc4_corpus_head_urls.txt
wget https://german-nlp-group.github.io/_static/file/gc4_corpus_middle_urls.txt
wget -i gc4_corpus_middle_urls.txt
```

### Head
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2015-48.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2016-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2017-13.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0000_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2017-13.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0001_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2017-13.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0002_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2017-13.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0003_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0004_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0005_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0006_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0006_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0006_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0006_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0006_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0006_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0006_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0006_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0006_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0006_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0007_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0007_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0007_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0007_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0007_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/head/de_head_0007_2020-10.tar.gz

### Middle
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2015-48.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2016-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2017-13.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0000_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2017-13.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0001_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2017-13.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0002_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2017-13.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0003_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2017-13.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0004_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2017-13.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2017-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0005_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2016-44.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2017-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0006_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2017-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0007_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0008_2018-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0008_2018-17.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0008_2018-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0008_2018-39.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0008_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0008_2019-09.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0008_2019-18.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0008_2019-30.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0008_2019-47.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0008_2020-10.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0009_2018-51.tar.gz
- https://opendata.iisys.de/systemintegration/Datasets/CommonCrawl/middle/de_middle_0009_2019-47.tar.gz
