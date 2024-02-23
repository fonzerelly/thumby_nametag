import unittest
import NameTag

def extractLetterSegment(bitmap, letterIndex, row):
    bitmap_list = list(bitmap)
    row_index = int(len(bitmap_list)/2*row)
    from_index = row_index + (letterIndex*16)
    to_index = row_index + ((letterIndex+1)*16)
    return bitmap_list[from_index:to_index]

def extractLetter(bitmap, letterIndex):
    return (
        extractLetterSegment(bitmap, letterIndex, 0) + 
        extractLetterSegment(bitmap, letterIndex, 1)
    )

class TestNameTag(unittest.TestCase):
    def assertLetterInBitmap(self, bitmap, letter, index):
        self.assertEqual(extractLetter(bitmap, index), list(letter))
    def test_concatLettersToBitmap(self):
        def test_that_it_contains_all_pixels_of_a_letter(self):
            
            self.assertLetterInBitmap(
                NameTag.concatLettersToBitmap("A"),
                NameTag.bitmapA,
                0
            )

        test_that_it_contains_all_pixels_of_a_letter(self)

if __name__=="__main__":
    unittest.main()