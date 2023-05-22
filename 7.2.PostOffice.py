class PostOffice:
    """A Post Office class. Allows users to message each other."""

    def __init__(self, usernames):
        """
        Initialize a PostOffice instance.

        Args:
            usernames (list): Users for which we should create PO Boxes.
        """
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """
        Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.

        Returns:
            int: The message ID, an auto-incremented number.

        Raises:
            KeyError: If the recipient does not exist.
        """
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        user_box = self.boxes.setdefault(recipient, [])
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, amount=None):
        """
        Read N first messages of a username.

        Args:
            username (str): Recipient's username.
            amount (int, optional): Number of messages to read.

        Returns:
            list of dict: amount unread messages.

        Raises:
            KeyError: If the recipient username does not exist.
        """
        messages = self.boxes.setdefault(username, [])
        amount = amount or len(messages)
        unread = []
        for message in messages:
            if amount == 0:
                break
            if not message['read']:
                message['read'] = True
                unread.append(message)
                amount -= 1
        return unread

    def search_inbox(self, username, key):
        """
        Search all messages of a username that contain a key.

        Args:
            username (str): Recipient's username.
            key (str): Keyword to search in recipient's messages.

        Returns:
            list of dict: All messages containing the key.

        Raises:
            KeyError: If the recipient username does not exist.
        """
        messages = self.boxes.setdefault(username, [])
        return [
            message
            for message in messages
            if key in message['body'] or key in message['sender']
        ]


if __name__ == '__main__':
    p = PostOffice(["david", "Cohen"])
    print(p.send_message("Cohen", "david", message_body='After creating a PO box and sending a letter'))
    print(p.send_message("Cohen", "david", message_body='especially the total of a thing or things in number'))
    print(p.read_inbox("david", 1))
    print(p.read_inbox("david"))
    print(p.search_inbox("david", 'let'))

