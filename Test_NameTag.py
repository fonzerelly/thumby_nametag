import unittest
import NameTag
import thumby

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

class TestScroller(unittest.TestCase):
    def create_iterator(self, values):
        index = -1  # Initialize index before the start of the list

        def iterator():
            nonlocal index  # Reference the 'index' from the outer scope
            index += 1  # Move to the next index
            if index < len(values):
                return values[index]
            else:
                raise Exception("MockTicker is depleted!")

        return iterator

    def test_that_it_positions_the_sprite_on_the_far_right_of_the_display_based_on_tick(self):
        uut = NameTag.Scroller(self.create_iterator([1000, 1001])) # wie bekome ich es hin, dass mein lambda unterschiedliche werte zurückliefert? mit yeild vieleicht?
        sprite = thumby.Sprite(16,16,bytearray([]),0,0)
        uut.scroll(sprite)
        self.assertEqual(thumby.display.width + 1, sprite.x)

    def xtest_that_it_positions_the_sprite_one_px_further_left_after_passed_tick_speed(self):
        uut = NameTag.Scroller(self.create_iterator([1000, 1027]), 27)
        sprite = thumby.Sprite(16,16,bytearray([]),0,0)
        uut.scroll(sprite)
        self.assertEqual(thumby.display.width , sprite.x)

    def xtest_that_it_returns_false_as_long_as_sprite_has_not_left_screen(self):
        uut = NameTag.Scroller(self.create_iterator([1000, 1027]), 27)
        sprite = thumby.Sprite(16,16,bytearray([]),0,0)
        self.assertFalse(uut.scroll(sprite))

    def test_that_it_returns_true_when_sprite_has_left_screen(self):
        time_offset = 1000
        time_offscreen = 2 * 27 # 1px left, 1px right
        time_when_sprite_hits_left = 72*27
        time_when_sprite_moved_one_char = 16*27
        time_when_sprite_leaves_screen = time_offset + time_offscreen + time_when_sprite_hits_left + time_when_sprite_moved_one_char
        uut = NameTag.Scroller(self.create_iterator([1000, time_when_sprite_leaves_screen]), 27)
        sprite = thumby.Sprite(16,16,bytearray([]),0,0)
        self.assertTrue(uut.scroll(sprite))



if __name__=="__main__":
    unittest.main()