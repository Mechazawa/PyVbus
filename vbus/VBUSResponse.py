class VBUSResponse(object):
    def __init__(self, line):
        assert len(line) > 2
        self.positive = line[0] == "+"
        spl = line[1:].split(":", 1)
        self.type = spl[0]
        self.message = None if len(spl) == 1 else spl[1][:1]