class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, N=None):
        """Read N first messages of username.

        :param str username: Recipient's username.
        :param N: Number of messages to read.
        :type N: int, optional
        :return: N unread messages.
        :rtype: list of dict
        :raises KeyError: if the recipient username does not exist.
        """
        messages = self.boxes[username]
        if N is None:
            N = len(messages)
        unread = []
        for i in range(len(messages)):
            if N == 0:
                break
            if not messages[i]['read']:
                unread.append(messages[i])
                self.boxes[username][i]['read'] = True
                N -= 1
        return unread

    def search_inbox(self, username, key):
        """Search all messages of username contain key.

        :param str username: Recipient's username.
        :param str key: Keyword to search in Recipient's username messages.
        :return: All messages contain the pass key in username .e-mail
        :rtype: list of dict
        :raises KeyError: if the recipient username does not exist.
        """
        res = []
        messages = self.boxes[username]
        for i in range(len(messages)):
            if key in messages[i]['body'] or key in messages[i]['sender']:
                res.append(messages[i])
                self.boxes[username][i]['read'] = True
        return res


if __name__ == '__main__':
    p = PostOffice(["david", "Cohen"])
    print(p.send_message("Cohen", "david", message_body='After creating a PO box and sending a letter'))
    print(p.send_message("Cohen", "david", message_body='message_id = po_box.send_message(a, b, Hello!)'))
    print(p.read_inbox("david"))
    print(p.search_inbox("david", 'Hello'))
