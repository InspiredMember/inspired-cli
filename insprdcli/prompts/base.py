from cement.core.exc import InterfaceError
from cement.utils.shell import Prompt


class Base(Prompt):
    class Meta:
        max_attempts = 1


class CharacterPrompt(Base):
    def process_input(self):
        try:
            str_value = str(self.input)
            assert str_value == self.input
            assert len(str_value) > 0
        except:
            raise InterfaceError(f'Invalid value: "{self.input}"')
        else:
            return str_value


class IntegerPrompt(Base):
    def process_input(self):
        try:
            int_value = int(self.input)
            assert str(int_value) == self.input
            assert int_value > 0
        except:
            raise InterfaceError(f'Invalid value: "{self.input}"')
        else:
            return int_value


class OptionalCharacterPrompt(CharacterPrompt):
    class Meta(Base.Meta):
        max_attempts_exception = False

    def process_input(self):
        if self.input is not None:
            return super(OptionalCharacterPrompt, self).process_input()
        return self.input


class OptionalIntegerPrompt(IntegerPrompt):
    class Meta(Base.Meta):
        max_attempts_exception = False

    def process_input(self):
        if self.input is not None:
            return super(OptionalIntegerPrompt, self).process_input()
        return self.input
