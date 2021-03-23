# PLMBot

from typing import List
from botbuilder.core import TurnContext, MessageFactory
from botbuilder.core.teams import TeamsActivityHandler
from get_eco_cost import getECOCost

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
        # text = turn_context.activity.text.strip().lower()
        text = turn_context.activity.text.strip().upper()

        print(f'Formatted text = {text}')

        # Basic reply to a user
        if "hello" in text:
            await self._cool_reply(turn_context)
            return

        # Proposed ECO Cost Rollup call
        if "GET_ECO_COST" in text:

            # Get the ECO number the user is requesting
            ecoNum = text.split(' ')[1]
            print(f'ecoNum = {ecoNum}')
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
        costSummary = getECOCost(ecoNum)

        # Sends the tabulated results back to the user
        reply_activity = MessageFactory.text(costSummary)
        await turn_context.send_activity(reply_activity)
