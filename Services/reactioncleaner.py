class ReactionCleaner:

    @staticmethod
    def cleanReactions(Reactions: dict):
        ReactionList = []
        for Reaction, Value in Reactions.items():
            ReactionList.append({Reaction: Value})

        return ReactionList