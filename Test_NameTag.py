import unittest
from unittest.mock import patch, Mock
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
        uut = NameTag.Scroller(self.create_iterator([1000, 1001]))
        sprites = [thumby.Sprite(16,16,bytearray([]),0,0)]
        uut.scroll(sprites)
        self.assertEqual(thumby.display.width + 1, sprites[0].x)

    def test_that_it_positions_the_sprite_one_px_further_left_after_passed_tick_speed(self):
        uut = NameTag.Scroller(self.create_iterator([1000, 1027]), 27)
        sprites = [thumby.Sprite(16,16,bytearray([]),0,0)]
        uut.scroll(sprites)
        self.assertEqual(thumby.display.width , sprites[0].x)

    def test_that_it_positions_the_second_sprite_one_px_further_left_behind_first_sprite(self):
        uut = NameTag.Scroller(self.create_iterator([1000, 1027]), 27)
        sprites = [
            thumby.Sprite(16,16,bytearray([]),0,0),
            thumby.Sprite(33,16,bytearray([]),0,0),
            thumby.Sprite(16,16,bytearray([]),0,0)
        ]
        uut.scroll(sprites)
        self.assertEqual(sprites[0].x + sprites[0].width, sprites[1].x)
        self.assertEqual(sprites[1].x + sprites[1].width, sprites[2].x)

    def test_that_it_positions_vertically_by_passed_in_fn(self):
        mock = Mock()
        mock.vertical_positioning.return_value = None
        uut = NameTag.Scroller(self.create_iterator([1000, 1027]), 27, lambda t, i, h:  mock.vertical_positioning(t, i, h))
        sprites = [
            NameTag.create16BitSprite([
                255,   1,   1,   1, 255,
                255, 128, 128, 128, 255
            ])
        ]
        uut.scroll(sprites)
        mock.vertical_positioning.assert_called_with(27, 0, 16)


    def test_that_it_returns_false_as_long_as_sprite_has_not_left_screen(self):
        uut = NameTag.Scroller(self.create_iterator([1000, 1027]), 27)
        sprites = [thumby.Sprite(16,16,bytearray([]),0,0)]
        self.assertFalse(uut.scroll(sprites))

    def test_that_it_returns_true_when_sprite_has_left_screen(self):
        time_offset = 1000
        time_offscreen = 2 * 27
        time_when_sprite_hits_left = 72*27
        time_when_sprite_moved_one_char = 16*27
        time_when_sprite_leaves_screen = time_offset + time_offscreen + time_when_sprite_hits_left + time_when_sprite_moved_one_char
        uut = NameTag.Scroller(self.create_iterator([1000, time_when_sprite_leaves_screen]), 27)
        sprites = [thumby.Sprite(16,16,bytearray([]),0,0)]
        self.assertTrue(uut.scroll(sprites))

    def test_that_it_returns_true_when_last_sprite_has_left_screen(self):
        time_offset = 1000
        time_offscreen = 2 * 27
        time_when_sprite_hits_left = 72*27
        time_when_sprite_moved_one_char = 16*27
        time_when_sprite_moved_two_char = 32*27
        time_when_not_all_sprites_left_screen = time_offset + time_offscreen + time_when_sprite_hits_left + time_when_sprite_moved_one_char
        time_when_sprite_leaves_screen =        time_offset + time_offscreen + time_when_sprite_hits_left + time_when_sprite_moved_two_char
        uut = NameTag.Scroller(self.create_iterator([1000, time_when_not_all_sprites_left_screen, time_when_sprite_leaves_screen]), 27)
        sprites = [
            thumby.Sprite(16,16,bytearray([]),0,0),
            thumby.Sprite(16,16,bytearray([]),0,0)
        ]
        self.assertFalse(uut.scroll(sprites))
        self.assertTrue(uut.scroll(sprites))

    @patch('thumby.display.drawSprite')
    def test_that_it_also_draws_each_sprite(self, mock_draw_sprite):
        uut = NameTag.Scroller(self.create_iterator([1000, 1027]), 27)
        sprites = [
            thumby.Sprite(16,16,bytearray([]),0,0),
           thumby.Sprite(16,16,bytearray([]),0,0)
        ]
        uut.scroll(sprites)
        mock_draw_sprite.assert_any_call(sprites[0])
        mock_draw_sprite.assert_any_call(sprites[1])

class TestCreate16BitSprite(unittest.TestCase):
    square = [
        255,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 255,
        255, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 128, 255
    ]

    half_square = [
        255,   1,   1,   1,   1,   1,   1,   1,
        255, 128, 128, 128, 128, 128, 128, 128
    ]

    def test_that_it_creates_bitmap_of_size_8x16 (self):
        result = NameTag.create16BitSprite(self.square)
        self.assertEqual(result.width, 16)
        self.assertEqual(result.height, 16)
        self.assertEqual(result.x, 0)
        self.assertEqual(result.y, 0)

    def test_that_it_creates_bitmap_of_size_8x16 (self):
        result = NameTag.create16BitSprite(self.half_square)
        self.assertEqual(result.width, 8)
        self.assertEqual(result.height, 16)

    def test_that_it_stores_pixels_as_bytearray (self):
        result = NameTag.create16BitSprite(self.square)
        self.assertTrue(isinstance(result.bitmap, bytearray))
        self.assertEqual(list(result.bitmap), self.square)

    def test_that_it_works_with_bytearray_as_well (self):
        bytearray_input = bytearray(self.square)
        result = NameTag.create16BitSprite(bytearray_input)
        self.assertTrue(result.bitmap, bytearray_input)


class TestSliceBitmap(unittest.TestCase):
    half_square = [
        255,   1,   1,   1,   1,   1,   1,   1,
        255, 128, 128, 128, 128, 128, 128, 128
    ]
    def test_that_it_turns_a_sprite_into_width_vertical_slices(self):
        slices = NameTag.sliceBitmap(self.half_square)
        self.assertEqual(len(slices), 8)
        for sprite in slices:
            self.assertEqual(len(sprite.bitmap), 2)

    def test_that_each_slice_contains_16_bits_of_each_column(self):
        verticalBar = NameTag.create16BitSprite([255,255])
        horizontalSegment = NameTag.create16BitSprite([1, 128])
        slices = NameTag.sliceBitmap(self.half_square)
        self.assertEqual(slices[0].bitmap, verticalBar.bitmap)
        for slice in slices[1:]:
            self.assertEqual(slice.bitmap, horizontalSegment.bitmap)


if __name__=="__main__":
    unittest.main()