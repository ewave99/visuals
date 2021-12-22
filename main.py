import math
import curses

def preload ( stdscr ):
    curses.start_color ()
    curses.use_default_colors ()
    curses.curs_set ( 0 )

def setup ( stdscr ):
    curses.init_pair ( 1, curses.COLOR_BLUE, -1 )
    curses.init_pair ( 2, curses.COLOR_RED, -1 )
    curses.init_pair ( 3, curses.COLOR_GREEN, -1 )

def draw ( stdscr, t ):
    rows, cols = stdscr.getmaxyx ()

    #parts = 2
    #for i in range ( parts ):
    #    pattern ( stdscr,
    #            sinPatternGenerator,
    #            rows,
    #            cols,
    #            5,
    #            str(cols//6),
    #            1/80,
    #            1/parts,
    #            t%(rows*20)*(i+1),
    #            int ( cols * i / parts ) )

    pattern ( stdscr,
            rectangleGenerator,
            rows,
            cols,
            2,
            'O',
            curses.color_pair ( 1 ),
            ( rows - 5 - int((math.sin(t*2)+1)/2*(rows-10)) ) // 2,
            ( cols - 5 - int((math.sin(t*2)+1)/2*(rows-10)*2) ) // 2,
            5+int ((math.sin(t*2)+1)/2*(rows-10)),
            10+int ((math.sin(t*2)+1)/2*(rows-10)*2)
            )

    pattern ( stdscr,
            rectangleGenerator,
            rows,
            cols,
            2,
            '[]',
            curses.color_pair ( 2 ),
            ( rows - 5 - int((math.sin(t*2+2)+1)/2*(rows-10)) ) // 2,
            ( cols - 5 - int((math.sin(t*2+2)+1)/2*(rows-10)*2) ) // 2,
            5+int ((math.sin(t*2+2)+1)/2*(rows-10)),
            10+int ((math.sin(t*2+2)+1)/2*(rows-10)*2)
            )
    pattern ( stdscr,
            rectangleGenerator,
            rows,
            cols,
            2,
            '\/',
            curses.color_pair ( 3 ),
            ( rows - 5 - int((math.sin(t*2+4)+1)/2*(rows-10)) ) // 2,
            ( cols - 5 - int((math.sin(t*2+4)+1)/2*(rows-10)*2) ) // 2,
            5+int ((math.sin(t*2+4)+1)/2*(rows-10)),
            10+int ((math.sin(t*2+4)+1)/2*(rows-10)*2)
        )


def pattern ( stdscr,
        generator_function,
        rows,
        cols,
        thickness,
        fillchar,
        colour,
        * gf_args,
        ** gf_kwargs ):
    generator = generator_function ( rows, cols, thickness, fillchar, * gf_args, ** gf_kwargs )

    piece = next ( generator )

    while len(piece) >= 3:
        stdscr.addstr ( * piece, colour )

        piece = next ( generator )

def sinPatternGenerator ( rows,
        cols,
        thickness=1,
        fill='+',
        row_stretch=1,
        col_stretch=1,
        row_offset=0,
        col_offset=0 ):
    row = 0

    for row in range ( rows ):
        waves = [
                math.sin ( row / cols / row_stretch - row_offset ),
                math.sin ( row / cols / row_stretch / 3 - row_offset ),
                math.sin ( row / cols / row_stretch / 5 - row_offset )
                ]
        col = int ( col_offset + (cols-thickness) * col_stretch * ( sum ( waves ) / len ( waves ) + 1 ) / 2 )

        yield ( row, col, repeatStr ( fill, thickness ) )

    yield tuple ()

def repeatStr ( fill, thickness ):
    return ( fill * ( thickness // len ( fill ) + 1 ) ) [ :thickness ]

def rectangleGenerator ( rows,
        cols,
        thickness,
        fill,
        row,
        col,
        height,
        width ):
    endrow = row + height - 1
    endcol = col + width - thickness

    yield ( row, col, repeatStr ( fill, width ) )
    row += 1

    while row < endrow:
        yield ( row, col, repeatStr ( fill, thickness ) )
        yield ( row, endcol, repeatStr ( fill, thickness ) )
        row += 1

    yield ( row, col, repeatStr ( fill, width ) )
    row += 1

    yield tuple ()
