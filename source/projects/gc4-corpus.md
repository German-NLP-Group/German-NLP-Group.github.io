# GC4 Corpus
The German colossal, cleaned Common Crawl corpus.

This is a German text corpus which is based on [Common Crawl](https://commoncrawl.org/). It can be used for various tasks in the NLP field. For example, for the self-supervised training of language models.

GC4 has been created by [**Philipp Reißel**](https://www.reissel.eu) from [ambeRoad](https://amberoad.de/). Many thanks to [iisys](https://www.iisys.de/) (the Institute of Information Systems Hof University) for hosting this dataset.

## Preprocessing and Cleanup
TODO: add more info

## Size
TODO: add more info

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