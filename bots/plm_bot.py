# PLMBot

from typing import List
from botbuilder.core import TurnContext, MessageFactory, CardFactory
from botbuilder.core.teams import TeamsActivityHandler
from get_eco_cost import getECOCost
from cards import ecoNum_prompt_card, cost_results_card

# PLMBot class for handling the Teams messages from the Users
class PLMBot(TeamsActivityHandler):

    # Initializes the bot with its credentials
    def __init__(self, app_id: str, app_password: str):
        self._app_id = app_id
        self._app_password = app_password

    # Handle the messages from the user messaging the bot
    async def on_message_activity(self, turn_context: TurnContext):
        
        # Removes special mentions
        # print(f'Initial message text = {turn_context.activity.text}')
        # TurnContext.remove_recipient_mention(turn_context.activity)

        # Strips out any mentions and formats the user's text for parsing
        text = turn_context.activity.text.strip().upper()

        # Basic reply to a user
        if "HELLO" in text:
            await self._cool_reply(turn_context)
            return

        # Proposed ECO Cost Rollup call
        if "GET_ECO_COST" in text:

            # Get the ECO number the user is requesting
            ecoNum = text.split(' ')[1]
            print(f'Processing request for ECO Proposed BOM Cost Rollup for {ecoNum}')
            await self._get_eco_cost(turn_context, ecoNum)
            return
        
        # Default reply to the user if no condition is matches
        await self._default_reply(turn_context)
        return

    # Default reply to the user to send another message
    async def _default_reply(self, turn_context: TurnContext):
        reply_activity = MessageFactory.text("Sorry I didn't catch that. Try another request!")
        await turn_context.send_activity(reply_activity)

    # Handles a basic reply to the user
    async def _cool_reply(self, turn_context: TurnContext):
        reply_activity = MessageFactory.text("Sup nerd")
        await turn_context.send_activity(reply_activity)

    # Handles an ECO cost script request
    async def _get_eco_cost(self, turn_context: TurnContext, ecoNum):

        # Run the getECOCost script
        costData = getECOCost(ecoNum)
        
        # Check the validity of the costData
        if type(costData) == list and len(costData) > 0:
            validCost = True
        else:            
            validCost = False
            if costData == -1:
                errorMsg = f'Sorry, {ecoNum} is not a valid ECO number. Please try another number.'
            elif costData == -2:
                errorMsg = f'Sorry, {ecoNum} has no valid affected items.'   

        if validCost:
            # Attach and send the summary card to the user
            costSummaryCard = cost_results_card(ecoNum, costData)
            await turn_context.send_activity(
                MessageFactory.attachment(CardFactory.adaptive_card(costSummaryCard))
            )
        else:
            reply_activity = MessageFactory.text(errorMsg)
            await turn_context.send_activity(reply_activity)
        
