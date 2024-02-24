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
            for letter in NameTag.letterBitmapAssignment:
                self.assertLetterInBitmap(
                    NameTag.concatLettersToBitmap(letter),
                    NameTag.letterBitmapAssignment[letter],
                    0
                )

        def test_that_it_concats_two_and_more_letters(self):
            result = NameTag.concatLettersToBitmap("ABC")
            self.assertLetterInBitmap(result, NameTag.bitmapA, 0)
            self.assertLetterInBitmap(result, NameTag.bitmapB, 1)
            self.assertLetterInBitmap(result, NameTag.bitmapC, 2)

        test_that_it_contains_all_pixels_of_a_letter(self)
        test_that_it_concats_two_and_more_letters(self)

if __name__=="__main__":
    unittest.main()