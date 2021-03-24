from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.components import TextBlock, Fact
from pyadaptivecards.inputs import Text
from pyadaptivecards.actions import Submit
from pyadaptivecards.options import Colors, FontWeight, FontSize
from pyadaptivecards.container import Container, FactSet

# ECO Proposed Cost Rollup Prompt Card
def ecoNum_prompt_card():

	# Body fields of the card
	promptTitle = TextBlock("ECO Proposed BOM Cost Rollup", weight=FontWeight.BOLDER, size=FontSize.LARGE, color=Colors.ACCENT)
	prompt = TextBlock("Please enter an ECO number")
	ecoNum = Text('ecoNum', placeholder="ECO-XXXXXXX")

	# Action fields of the card
	submit = Submit(title="Process ECO")

	# Creates the returns the card
	card = AdaptiveCard(body=[promptTitle, prompt, ecoNum], actions=[submit])
	print('Created ecoNum_prompt_card')
	return card

# ECO Propost Cost Rollup Results Summary Card
def cost_results_card(ecoNum, costData):

	# Header field of the card
	resultTitle = TextBlock(f'{ecoNum} Results:', weight=FontWeight.BOLDER, size=FontSize.LARGE)
	summaryItems = [resultTitle]

	for affItem in costData:
		# TextBlock for the Affected Item header
		affItemPartNum = TextBlock(f'Affected Item: {affItem[0]}', color=Colors.ACCENT)
		
		# FactSet of the summary data for that Affected Item
		origItemCost = Fact("Original Item Cost:", f'$ {affItem[1]}')
		origBOMCost = Fact("Original BOM Cost:", f'$ {affItem[2]}')
		propBOMCost = Fact("Proposed BOM Cost:", f'$ {affItem[3]}') 
		affItemResults = FactSet([origItemCost, origBOMCost, propBOMCost])

		# Create a container to segregate each FactSet
		affItemContainer = Container([affItemPartNum, affItemResults], separator=True)
		summaryItems.append(affItemContainer)
	
	# Create and return the card
	card = AdaptiveCard(body=summaryItems)
	print('Created cost_results_card')
	return card.to_dict()
