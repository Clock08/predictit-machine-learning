from data_input import DataInput
from source_analysis import SourceAnalysis
from entity_analysis import EntityAnalysis
from sentiment_analysis import SentimentAnalysis
from trader import Trader

class Main:
	def __init__(self):
		self.dataInput = DataInput()
		self.sourceAnalysis = sourceAnalysis()
		self.entityAnalysis = EntityAnalysis()
		self.sentimentAnalysis = SentimentAnalysis()
		self.trader = Trader()

	def start(self):
		dataInputReceived = lambda(data):
			sourceDataReceived = lambda(sourceData):
				entityDataReceived = lambda(entityData):
					sentimentDataReceived = lambda(sentimentData):
						self.trader.trade(sourceData, entityData, sentimentData)
					self.sentimentAnalysis.run(sentimentDataReceived, data)
				self.entityAnalysis.run(entityDataReceived, data)
			self.sourceAnalysis.run(sourceDataReceived, data)
		self.dataInput.poll(dataInputReceived)
