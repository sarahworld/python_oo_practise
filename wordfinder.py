"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    """Class to find random words from directory.

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

     >>> wf.random() in ["cat", "dog", "porcupine"]
    True

     >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, path):
        """ Read file and reports number of words read"""
        file = open(path);
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")
    
    def parse(self, file):
        """Returns list of words with spaces removed"""
        return [ w.strip() for w in file]

    def random(self):
        """Returns random word from the words list"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    Specialized Word Finder that excludes blank lines/ comments.

    >>> swf = SpecialWordFinder("complex.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """
    def init(self, path):
        """ Runs the init method for parent class"""
        super.__init__(path)

    def parse(self, file):
        """Parse file and considers words by skipping blank lines and comments"""
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]