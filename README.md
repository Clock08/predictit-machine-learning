# Pipeline to process and trade on news articles.

The pipeline will work as follows:

1. The first stage of the pipeline is data input.  This stage will gather news articles relating to a markets, and publish them into a SQS queue for analysis.

2. The second stage of the pipeline is data analysis.  This stage will gather articles from SQS, analyze them in certain ways (e.g. source reliability, sentiment), and assign a score to determine whether they will affect the associated market in a positive and negative way.  The score will be queued in SQS (combined with all information from the first stage).

3. The third stage of the pipeline is the trader.  This stage will trade based on the score assigned by stage 2.  

Note that the pipeline will be designed to guarantee "at-least-once" delivery for all given news articles.  As such, the third stage of the pipeline could theoretically receive a given news article more than once.  As such, sanity checks will be performed before trading; for example, news articles more than X minutes old will be ignored.
