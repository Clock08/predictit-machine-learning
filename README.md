# PredictIt ML

A ML pipeline to trade PredictIt shares based on news events.

# Pipeline Description

The pipeline will have five discrete units:

1. The first stage is **data input**.  This stage will gather data from various sources and compile them into units of data.  For example, a unit of data could represent a Tweet or a news headline.

2. The second stage is **source analysis**.  This stage will use a local model to assign a reliability score to a given source.

3. The second stage is **entity analysis**.  This stage will determine whether a given news article pertains to a PredictIt market.  It will assign a score to any market it pertains to.  This stage will use the Google Natural Language API to identify possible entities, and then a local model to associate those entities with markets.

4. The third stage is **sentiment analysis**.  This stage will determine whether a given tweet implies that a certain share is more or less likely to be redeemed at $1.  This stage will use the Google Natural Language Syntax API to determine if the headline implies that something "will" or "will not" happen. 

5. The fourth stage is **trading**.  This stage will either buy or sell shares of a given market based on the output of stages 1, 2 and 3.

An additional task will be run every minute to sell any positions open for more than 5 minutes.  This is to avoid prolonged exposure to any given market.
