from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.components import TextBlock, Fact
from pyadaptivecards.inputs import Text
from pyadaptivecards.actions import Submit
from pyadaptivecards.container import Container, FactSet

# ECO Proposed Cost Rollup Card
promptTitle = TextBlock("ECO Proposed BOM Cost Rollup", weight="bolder", size="large")
prompt = TextBlock("Please enter an ECO number")
ecoNum = Text('ecoNum', placeholder="ECO-XXXXXXX")

submit = Submit(title="Process ECO")

card = AdaptiveCard(body=[promptTitle, prompt, ecoNum], actions=[submit])
card_json = card.to_json(pretty=True)
print(card_json)

# Results Summary Card
resultTitle = TextBlock(ecoNum, weight="bolder", size="large")
summaryItems = [resultTitle]

for affItem in costData:
	
	# Header for the Affected Item
	affItemPartNum = TextBlock(affItem[0])
	
	# FactSet of the summary data for that Affected Item
	origItemCost = Fact("Original Item Cost", affItem[1])
	origBOMCost = Fact("Original BOM Cost", affItem[2])
	propBOMCost = Fact("Proposed BOM Cost", affItem[3])	 
	affItemResults = FactSet([origItemCost, origBOMCost, propBOMCost])
	
	# Wrap up each Affected Item in a container
	# itemContainer = Container([affItemPartNum, affItemResults]) 
	summaryItems.append(affItemPartNum)
	summaryItems.append(affItemResults)

card = AdaptiveCard(body=[resultTitle, summaryItems])
card_json = card.to_json(pretty=True)
print(card_json)
