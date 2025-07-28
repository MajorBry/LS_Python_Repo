class Banner:
    def __init__(self, message):
        self._message = message
        self._inner_width = 2 + len(message)

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return '|' + ' ' * self._inner_width + '|'

    def _horizontal_rule(self):
        return '+' + '-' * self._inner_width+ '+'

    def _message_line(self):
        return f"| {self._message} |"

# Comments show expected output
banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

print()
banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+