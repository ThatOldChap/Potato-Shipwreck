# PLMBot

from typing import List
from botbuilder.core import CardFactory, TurnContext, MessageFactory
from botbuilder.core.teams import TeamsActivityHandler, TeamsInfo
from botbuilder.schema import CardAction, HeroCard, Mention, ConversationParameters
from botbuilder.schema.teams import TeamInfo, TeamsChannelAccount
from botbuilder.schema._connector_client_enums import ActionTypes

# PLMBot class for handling the Teams messages from the Users
class PLMBot(TeamsActivityHandler):

    # Initializes the bot with its credentials
    def __init__(self, app_id: str, app_password: str):
        self._app_id = app_id
        self._app_password = app_password

    # Handle the messages from the user messaging the bot
    async def on_message_activity(self, turn_context: TurnContext):

        # Strips out any mentions and formats the user's text for parsing
        TurnContext.remove_recipient_mention(turn_context.activity)
        text = turn_context.activity.text.strip().lower()

        # Basic reply to a user
        if "hello" in text:
            await self._cool_reply(turn_context)
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
