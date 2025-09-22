import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push_and_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)

    def test_peek(self):
        self.stack.push("A")
        self.assertEqual(self.stack.peek(), "A")
        self.assertFalse(self.stack.is_empty())

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(5)
        self.stack.push(15)
        self.assertEqual(self.stack.size(), 2)

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

if __name__ == "__main__":
    unittest.main()

