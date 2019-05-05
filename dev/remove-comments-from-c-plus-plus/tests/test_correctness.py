import os
import unittest

from remove_comments import remove_comments


class TestCorrectness(unittest.TestCase):

    def test_by_file(self):

        root_dir = os.path.dirname(__file__)
        fixtures_dir = os.path.join(root_dir, 'fixtures')
        answers_dir = os.path.join(root_dir, 'answers')

        for x in os.listdir(fixtures_dir):
            with open(os.path.join(fixtures_dir, x), 'r') as f:
                fixture = f.read()
            with open(os.path.join(answers_dir, x), 'r') as f:
                answer = f.read()
            with self.subTest(file=x):
                r = remove_comments(fixture)
                print(r)
                r = [x.split() for x in r.split('\n') if x.strip()]
                answer = [x.split() for x in answer.split('\n') if x.strip()]
                print(len(r), len(answer))
                self.assertEquals(r, answer)
