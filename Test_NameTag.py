import unittest
import NameTag

def extractLetterSegment(bitmap, letterIndex, row):
    bitmap_list = list(bitmap)
    row_index = int(len(bitmap_list)/2*row)
    gap = letterIndex*1
    from_index = row_index + (letterIndex*16) + gap
    to_index = row_index + ((letterIndex+1)*16) + gap
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

        def test_that_it_keeps_a_gap_of_one_pixel_between_each_letter(self):
            concatenatedBitmap = NameTag.concatLettersToBitmap("OOO")
            resultAtGapPosition =[
                concatenatedBitmap[16], concatenatedBitmap[33], concatenatedBitmap[50],
                concatenatedBitmap[67], concatenatedBitmap[84], concatenatedBitmap[101]
            ]
            self.assertEqual(resultAtGapPosition, [
                0,0,0,
                0,0,0
            ])
            
        test_that_it_contains_all_pixels_of_a_letter(self)
        test_that_it_concats_two_and_more_letters(self)
        test_that_it_keeps_a_gap_of_one_pixel_between_each_letter(self)

if __name__=="__main__":
    unittest.main()