import unittest
from untbookstore import UntbookstoreSpider

class UntbookstoreSpiderTestCase(unittest.TestCase):
    def provideSource():
        source = '<!DOCTYPE html><html><head><title>Big Nasty Tech - Home</title></head><body><h1>test</h1><p>more test stuff</p>' +
            '</body></html>'
        return source
    def test_convertToScrapyObject(self):
        self.source = self.provideSource()
        