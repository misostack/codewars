#!/usr/bin/python
from helpers import assert_equals

"""
A hero is on his way to the castle to complete his mission. 
However, he's been told that the castle is surrounded with a couple of powerful dragons!
Wach dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry..
Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, 
will he survive?

Return true if yes, false otherwise :)

"""

def hero(bullets, dragons):
    bullets_to_defeat_a_dragon = 2
    # he ony survives if has enough bullets
    return bullets >= dragons * bullets_to_defeat_a_dragon

if __name__ == "__main__":
    assert_equals(hero(10, 5), True)
    assert_equals(hero(7, 4), False)
    assert_equals(hero(4, 5), False)
    assert_equals(hero(100, 40), True)
    assert_equals(hero(1500, 751), False)
    assert_equals(hero(0, 1), False)