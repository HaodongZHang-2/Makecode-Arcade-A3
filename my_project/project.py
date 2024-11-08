# single line comments
# if player overlaps enemy,
# then stop all sounds and
# finish the game with failure
# register overlap event for player and enemy
# if player overlaps any enemy, then callback
# function named on_on_onoverlap

def on_on_overlap(sprite3, otherSprite):
    music.stop_all_sounds()
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

# event listener to ControllerButton 'B' pressed
# register event  listener to key B pressed

def on_b_pressed():
    global bullet
    bullet = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 4 4 . . . . . . . 
                    . . . . . . 4 5 5 4 . . . . . . 
                    . . . . . . 2 5 5 2 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        beibie,
        76,
        0)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.UNTIL_DONE)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

# event listener to listen whether
# player achieve the goal
# register event listener to call on_overlap_tile
# when player touches swamp_tile1 which indicates
# the player win the game

def on_overlap_tile(sprite, location):
    music.stop_all_sounds()
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.swamp.swamp_tile1,
    on_overlap_tile)

# event listener to ControllerButton 'A' pressed
# register event listener

def on_a_pressed():
    music.play(music.melody_playable(music.beam_up),
        music.PlaybackMode.IN_BACKGROUND)
    beibie.vy = -320
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# event listener to 'left' key pressed
# register event listener

def on_left_pressed():
    animation.run_image_animation(beibie,
        [img("""
                . . . . . . . . . . . . . . 
                        . f f f . f f f f f . . . . 
                        f f f f f c c c c f f . . . 
                        f f f f b c c c c c c f . . 
                        f f f c 3 c c c c c c f . . 
                        . f 3 3 c c c c c c c c f . 
                        . f f f c c c c c 4 c c f . 
                        . f f f f c c c 4 4 c f f . 
                        . f f 4 4 f b f 4 4 f f f . 
                        . f f 4 d 4 1 f d d c f . . 
                        . . f f f 4 d d d d f . . . 
                        . . 4 d d e 4 4 4 e f . . . 
                        . . e d d e 3 3 3 3 f . . . 
                        . . f e e f 6 6 6 6 f f . . 
                        . . f f f f f f f f f f . . 
                        . . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . . . . . . . . . 
                        . . . . f f f f f . f f f . 
                        . . . f f c c c c f f f f f 
                        . . f c c c c c c b f f f f 
                        . . f c c c c c c 3 c f f f 
                        . f c c c c c c c c 3 3 f . 
                        . f c c 4 c c c c c f f f . 
                        . f f c 4 4 c c c f f f f . 
                        . f f f 4 4 f b f 4 4 f f . 
                        . . f f d d f 1 4 d 4 f . . 
                        . . . f d d d e e f f f . . 
                        . . . f e 4 e d d 4 f . . . 
                        . . . f 3 3 e d d e f . . . 
                        . . f f 6 6 f e e f f f . . 
                        . . f f f f f f f f f f . . 
                        . . . f f f . . . f f . . .
            """),
            img("""
                . . . . . . . . . . . . . . 
                        . . . . f f f f f . f f f . 
                        . . . f f c c c c f f f f f 
                        . . f c c c c c c b f f f f 
                        . . f c c c c c c 3 c f f f 
                        . f c c c c c c c c 3 3 f . 
                        . f c c 4 c c c c c f f f . 
                        . f f c 4 4 c c c f f f f . 
                        . f f f 4 4 f b f 4 4 f f . 
                        . . f c d d f 1 4 d 4 f f . 
                        . . . f d d d d 4 f f f . . 
                        . . . f e 4 4 4 e d d 4 . . 
                        . . . f 3 3 3 3 e d d e . . 
                        . . f f 6 6 6 6 f e e f . . 
                        . . f f f f f f f f f f . . 
                        . . . f f f . . . f f . . .
            """),
            img("""
                . . . . f f f f f . f f f . 
                        . . . f f c c c c f f f f f 
                        . . f c c c c c c b f f f f 
                        . . f c c c c c c 3 c f f f 
                        . f c c c c c c c c 3 3 f . 
                        . f c c 4 c c c c c f f f . 
                        . f f e 4 4 c c c f f f f . 
                        . f f e 4 4 f b f 4 4 f f . 
                        . . f f d d f 1 4 d 4 f . . 
                        . . . f d d d d 4 f f f . . 
                        . . . f e 4 4 4 e e f . . . 
                        . . . f 3 3 3 e d d 4 . . . 
                        . . . f 3 3 3 e d d e . . . 
                        . . . f 6 6 6 f e e f . . . 
                        . . . . f f f f f f . . . . 
                        . . . . . . f f f . . . . .
            """)],
        100,
        False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

# event listener to down into the water
# define on_overlap_tile2 function as a evenlistener
# which will be called on corresponding event occured
# register falling down into the water event,
# call function of on_overlap_tile2 to respond
# the event

def on_overlap_tile2(sprite2, location2):
    music.stop_all_sounds()
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_water,
    on_overlap_tile2)

# customised function as event listener to respond
# enemy hit wall ,then bounce the enemy back
# register hitwall event for enemy

def on_hit_wall(sprite4, location3):
    if sprite4.is_hitting_tile(CollisionDirection.RIGHT):
        sprite4.set_velocity(-20, 0)
    # TODO
    if sprite4.is_hitting_tile(CollisionDirection.LEFT):
        sprite4.set_velocity(20, 0)
scene.on_hit_wall(SpriteKind.enemy, on_hit_wall)

# event listener to 'right' key pressed
# register eventlistener or binding the event with eventlistener

def on_right_pressed():
    animation.run_image_animation(beibie,
        [img("""
                . . . . . . . . . . . . . . 
                        . f f f . f f f f f . . . . 
                        f f f f f c c c c f f . . . 
                        f f f f b c c c c c c f . . 
                        f f f c 3 c c c c c c f . . 
                        . f 3 3 c c c c c c c c f . 
                        . f f f c c c c c 4 c c f . 
                        . f f f f c c c 4 4 c f f . 
                        . f f 4 4 f b f 4 4 f f f . 
                        . f f 4 d 4 1 f d d c f . . 
                        . . f f f 4 d d d d f . . . 
                        . . 4 d d e 4 4 4 e f . . . 
                        . . e d d e 3 3 3 3 f . . . 
                        . . f e e f 6 6 6 6 f f . . 
                        . . f f f f f f f f f f . . 
                        . . . f f . . . f f f . . .
            """),
            img("""
                . f f f . f f f f f . . . . 
                        f f f f f c c c c f f . . . 
                        f f f f b c c c c c c f . . 
                        f f f c 3 c c c c c c f . . 
                        . f 3 3 c c c c c c c c f . 
                        . f f f c c c c c 4 c c f . 
                        . f f f f c c c 4 4 e f f . 
                        . f f 4 4 f b f 4 4 e f f . 
                        . . f 4 d 4 1 f d d f f . . 
                        . . f f f 4 d d d d f . . . 
                        . . . f e e 4 4 4 e f . . . 
                        . . . 4 d d e 3 3 3 f . . . 
                        . . . e d d e 3 3 3 f . . . 
                        . . . f e e f 6 6 6 f . . . 
                        . . . . f f f f f f . . . . 
                        . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . 
                        . f f f . f f f f f . . . . 
                        f f f f f c c c c f f . . . 
                        f f f f b c c c c c c f . . 
                        f f f c 3 c c c c c c f . . 
                        . f 3 3 c c c c c c c c f . 
                        . f f f c c c c c 4 c c f . 
                        . f f f f c c c 4 4 c f f . 
                        . f f 4 4 f b f 4 4 f f f . 
                        . . f 4 d 4 1 f d d f f . . 
                        . . f f f e e d d d f . . . 
                        . . . f 4 d d e 4 e f . . . 
                        . . . f e d d e 3 3 f . . . 
                        . . f f f e e f 6 6 f f . . 
                        . . f f f f f f f f f f . . 
                        . . . f f . . . f f f . . .
            """),
            img("""
                . f f f . f f f f f . . . . 
                        f f f f f c c c c f f . . . 
                        f f f f b c c c c c c f . . 
                        f f f c 3 c c c c c c f . . 
                        . f 3 3 c c c c c c c c f . 
                        . f f f c c c c c 4 c c f . 
                        . f f f f c c c 4 4 e f f . 
                        . f f 4 4 f b f 4 4 e f f . 
                        . . f 4 d 4 1 f d d f f . . 
                        . . f f f 4 d d d d f . . . 
                        . . . f e e 4 4 4 e f . . . 
                        . . . 4 d d e 3 3 3 f . . . 
                        . . . e d d e 3 3 3 f . . . 
                        . . . f e e f 6 6 6 f . . . 
                        . . . . f f f f f f . . . . 
                        . . . . . f f f . . . . . .
            """)],
        100,
        False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

# event listener to respond enemy falling down into water
# register enemy falling down into water event

def on_overlap_tile3(sprite22, location22):
    sprites.destroy(sprite22, effects.spray, 500)
scene.on_overlap_tile(SpriteKind.enemy,
    sprites.dungeon.hazard_water,
    on_overlap_tile3)

# event listener to detect whether or
# not bullet overlapping enemy
# register shooting event listener

def on_on_overlap2(sprite42, otherSprite2):
    sprites.destroy(sprite42)
    sprites.destroy(otherSprite2, effects.spray, 200)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

# generate monsters with some attributes
def Create_monsters():
    global monsters, game_scene
    for index in range(5):
        monsters = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.enemy)
        tiles.place_on_tile(monsters,
            tiles.get_tile_location(randint(3, 80), randint(6, 10)))
        monsters.ay = 1000
        monsters.set_velocity(20, 0)
        animation.run_image_animation(monsters,
            [img("""
                    . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                f 5 5 2 2 5 5 5 5 5 5 5 5 5 f . 
                                f 5 5 5 2 2 2 5 5 5 5 5 5 f f . 
                                f 5 5 5 5 5 2 2 5 5 5 f f . . . 
                                f 5 5 5 5 5 5 5 5 f f . . . . . 
                                f 5 5 5 5 5 5 5 f . . . . . . . 
                                f 5 5 5 5 5 5 5 5 f f . . . . . 
                                f 5 5 5 5 5 5 5 5 5 5 f f . . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . f f f f f f f . . . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                f 5 5 2 2 5 5 5 5 5 5 5 5 5 f . 
                                f 5 5 5 2 2 2 5 5 5 5 5 5 5 f . 
                                f 5 5 5 5 5 2 2 5 5 5 5 5 5 f . 
                                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                                f 5 5 5 5 5 5 5 f f f f f f f . 
                                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                                f 5 5 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . f 5 5 5 5 5 5 5 5 5 5 5 f . . 
                                . . f 5 5 5 5 5 5 5 5 5 f . . . 
                                . . . f 5 5 5 5 5 5 5 f . . . . 
                                . . . . f f f f f f f . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            100,
            True)
        if game_scene >= 2:
            game_scene += 1
            game_scene += 1
game_scene = 0
monsters: Sprite = None
bullet: Sprite = None
beibie: Sprite = None
scene.set_background_image(img("""
    8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888855555
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888885555555
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888885555555
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888855555555
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888855555555
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888885555555
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888885555555
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888555555
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888588888888888888888888888888888888888888888888888888888888888888888855555
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888588888888888888888888888888888888888888888855555
        8888888888888888888888888885888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888885555
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888858888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888858888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888858888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888898888888888888888888888888888888888888888888888888888888888888888888888888888888889888888888888888888888888888888888888888888888888888888888888
        8888888888888888889888888888888888888888888888888888888888888888888888888888888888888888888888888888988888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888988888888888888888888888888888888888888888888888888888888888888888888888888888888898888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888988888888888888888888888888888888888888888888888888888888888888888888888888888888898888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888858888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888188888888888dd8888888888588888888888885888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888ddd888888888ddd888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888881ddd888888888ddd888888888888888888888888888888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888888888888888888ddddddd888888ddddd88888888888888888888888888888888888888888888888888888888888888888
        88888888888888888888888888888888888888888ddddddddd888888888888888858888888888ddddddd888888ddddd888888888888888888888888888888888888888888dddddddddd8888888888888
        88888888888888888888888888888888888888888ddddddddd888888888888888888888888888ddddddd888888ddddd888888888888888888888888888888888888888888dddddddddd8888888888888
        8888888888888888888ddd8888888888888888888d11dddddd888888888888888888888888888d11dddd88888ddddddd88888888888888888888dd8888888888888888888dd1d1ddddd8888888888888
        888888888888888888ddddd888888888888888888ddddddd1d888888888888888888888888888ddddddd88888ddddddd8888888888888888888dddd888888888888888888dddddd11dd8888888888888
        88888888888888888dddddd888888888888888888ddddddddd8888888888d88888888ddddd888d1ddddd88888ddddddd88888888888888888dddddd888888888888888888dddddddddd8888888888888
        88888888888888888ddd1d888888d888888888888ddddddddd888888888dd88888888ddddd888ddddddd88888ddddddd88888888888888888ddd1d888888dd88888888888dddd1ddddd88888888dd888
        88888888888888888dddddd88888d888888888888ddddddd1d888888888dd88888888ddddd888ddddddd88888ddddddd88888888888888888dddddd88888dd88888888888ddddddd1dd88888888dd888
        88888888ddd888888dd11d88888ddd88888888888ddddddddd88dddddd8dd88888888ddddd888ddddddd88888ddddddd888888888dd888888ddd1d88888ddd88888888888dddddddddd8ddddddddd888
        d8dd8888ddddddddddd1ddd888ddddd8888888888ddddddd1d88d11ddd8dd888888888dd1dd88ddddddd888dddddddddd8dd8888ddddddddddddd1d8888dddd8888888888dddddd11dd8d11dddddd888
        dddd88888d1dd1ddddddddd888ddddd8888888888ddddddddd88dddd1d8dd88888888dddddd88dd1dddd888ddddddddddddd8888dd1ddd1dddddddd8888dddd8888888888dddddddddd8dddd1dddd888
        dd1d88888ddd1111ddddddd888ddddd8888888888ddddddddd88dddd1dddd88888888dddddd88ddddddd888ddddddddddd1d8888dddd1d11ddddddd8888dddd8888888888dddddddddd8dddd1dddd888
        dddd8888dddddddddddddddd88dddddd88dd8dd8ddddddddddd8d11dddddd88888888dddddd88ddddddd888ddddddddddddd8888dddddddddddddddd88dddddd888d88ddddddddddddd8d11dddddd888
        dd1d8888dddddddddddddddd88dddddd88ddddddddddddddddd8ddddddddd88d88d88dddddd88ddddddd888ddddddddddd1d8888dddddddddddddddd88dddddd888dddddddddddddddd8ddddddddd888
        ddddd8dd1d1ddddddddddddd88ddddddd8dddd11ddddddddddddd11bbddddddd8ddd88dd1dd88ddddddd888ddddddddddddddd8ddd1ddddddddddddd88ddddddd888d11ddddddbddddddd11bbbddd8dd
        ddddd8dddddddddddddddddddd1dddddd8dddddddddbbbdddddddddbbbdddddd8ddd8dddddd88ddddddd888ddddddddddddddd8dddddddddddddddddddddddddd8ddddddddddbbdddddddddbbbddd8dd
        ddddd8ddddddddddddddddddddddddddd8dddddddddbbbdddddddddbbbdddddddddddddddddddddddddd888ddddddddddddddd8dddddddddddddddddddddddddd8ddddddddddbbdddddddddbbbdddddd
        ddddd8ddddddddddddddddddddddddddd8dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd8ddddddddddddddd8dddddddddddddddddddddddddd8d1ddddddbbbbbbbdddddbbbbbddddd
        dddddbbbbbbbbbddddddddddddddddddd8dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd8ddddddddddddddbbbbbbbbbbdddddddddddddddddd8ddddddddbbbbbbbdddddbbbbbddddd
        dddddbbbbbbbbbddddddddddddddddddd8dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd8ddddddddddddddbbbbbbbbbbdddddddddddddddddd8ddddddddbbbbbbbdddddbbbbbddddd
        dddddbddbbbbbbddddddddddddddddddd8dddddddbddbbbbdddddbbbbbbbdd111dddddddddddddddbbdddd8ddddddddddddddbbdbdbbbbbdddddddddddddddddd8ddddddddbbbbbbbddddbbbbbbbb11d
        dddddbbbbbbbdbddddddddddddddddddd8dddddddbbbbbbbdddddbbbbbbbddd11ddddddddddddddbbbbddd8ddddddddddddddbbbbbbddbbdddddddddddddddddd8ddddddddbbbbbbbddddbbbbbbbbddd
        dddddbbbbbbbbbddddddddddbddddddddbbbbbdddbdbbbbbdddddbbbbbbbddddddddddd1dddddbbbbbbddd8ddddddddddddddbbbbbbbbbbdddddddddddddddddddbbbbddddbbbdbbbddddbbbbbbbbddd
        dddddbbbbbbbbbdddddddddbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdd1ddddddddddddddbbbdbddddddbbdddddddddddbbbbdbbbbbddddddddbbdddddddddbbbbddddbbbdbbbddddbbbbbbbbd1d
        dddddbbbbbbbdbdddddddddbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdd111ddddddddddddbbbbbbdddddbbdddddddddddbbbbbbbdbbddddddddbbddddddddbbbbbbdddbbbbbbbddddbbbbbbbb11d
        dddddbbbbbbbbbddbbbbbbdbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdddddddddbb1dddddbbbdbdddddbbbdddddddddddbbbbbbbbbbdbbbbbbbbbddddddddbbbbbbdddbbbdbbbddddbbbbbbbbddd
        dddddbbbbbbbdbddbddbbbdbbdddddddddbbdbbddbbbbbbbdddbbbbbbbbbbdbbddddbbbbbbbbbbbbbdbddddbbbbddddddddddbbbbbbddbbdbddbbbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        dddddbbbbbbbbbddbbbbdbdbbddddddddbbbbbbddbbdbbbbdddbbbbbbbbbbbbbddddbbdbbbdbbbbbbbbddddbbbbddddddddddbbbbbbbbbbdbbbbdbbbbddddddddbbbbbbbddbbbbdbbddbbbbbbbbbbbbb
        dddddbbbbbbbbbddbbbbdbbbbddddddddbbbbbbddbbbbbbbdddbbbbbbbbbbbdbddddbbbbdbddbbbbbbbddddbbbbddddddddddbbbbbbbbbbdbbbbdbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        dbbdbbbbbbbbbbbdbddbbbbbbddddddddbbbbbbddbbbbbbbdddbbbbbbbbbbbbbddddbbbbbbbbbbbbbbbbddbbbbbbdddbddbbbbbbbbbbbbbdbddbbbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbdbbbbbbbbbddbddbddbbbbbbddbbbbbbbdddbbbbbbbbbbbdbddddbbbbbbbbbbbbbbbbddbbbbbbdddbbbbbbbbbbbbbbbbdbbbbbbbbbdddddbddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        bbddbbbbbbbbbbbbbddddbbbbbbbdbbbddbbdbbddbbbbbbbdddbbbbbbbbbbbbbbbdbbbdbbbbbbbbbbbbbddbbbbbbbdddbddbbbbbbbbbbbbbbddbdbbbbdbbdbbbdbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbdbbbbbbddbbbbbbbdddbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbdbbbbbbbbbbbddbbbbdbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbddbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbbbbbbbebbbbbbbbbbbbbbbbebbbbb
        bbbbbbebbbeebbbbbeebbbbebbbebbbbebeebbbebbbbbbebbbeebbbbbeebbbbebbbebbbbebeebbbebbbbbbebbbeebbbbbeebbbbebbbebbbbebeebbbebbbbbbebbbeebbbbbeebbbbebbbebbbbebeebbbe
        bbebbbeebeebbebbbeebbbeebbbeebbbebbeebeebbebbbeebeebbebbbeebbbeebbbeebbbebbeebeebbebbbeebeebbebbbeebbbeebbbeebbbebbeebeebbebbbeebeebbebbbeebbbeebbbeebbbebbeebee
        bbeebbeebeebbeebbbeebeebbbbeebebeebeeeebbbeebbeebeebbeebbbeebeebbbbeebebeebeeeebbbeebbeebeebbeebbbeebeebbbbeebebeebeeeebbbeebbeebeebbeebbbeebeebbbbeebebeebeeeeb
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
"""))
game.set_dialog_frame(img("""
    ...cc......................cc....
        ..c55c..bbbb...bbbbb......c55c...
        .cb55bcbdddbbbbbdddbbbbbbcb55bc..
        b555555bbdddb111bdddb11db555555b.
        bb5555bbdbdb11111bdb1111bb5555bb.
        cb5555bcddd11111ddd11111cb5555bc.
        .c5bb5c1111d111d111d111ddc5bb5c..
        .cbbbbc111111111111111111cbbbbc..
        ..b11111111111111111111111d111bb.
        ..b111111111111111111111111d1bdb.
        ..bb11111111111111111111111dbddb.
        .bbdb1d11111111111111111111ddddb.
        .bdddd11111111111111111111d1bdbb.
        .bddbd11111111111111111111111bb..
        .bdb1d111111111111111111111111b..
        .bb111d11111111111111111111111b..
        ..b11111111111111111111111d111bb.
        ..b111111111111111111111111d1bdb.
        ..bb11111111111111111111111dbddb.
        .bbdb1d11111111111111111111ddddb.
        .bdddd11111111111111111111d1bdbb.
        .bddbd11111111111111111111111bb..
        .bdbb1111111111111111111111111b..
        .bbbd1111111111111111111111111b..
        ..bcc111111111111111111111dccdb..
        ..c55c111d111d111d111d1111c55cb..
        .cb55bcdd11111ddd11111dddcb55bc..
        b555555b11111bdb11111bdbb555555b.
        bb5555bbb111bdddb111bdddbb5555bb.
        cb5555bcdbbbbbdddbbbbbddcb5555bc.
        .c5bb5c.bb...bbbbb...bbbbc5bb5c..
        .cbbbbc..................cbbbbc..
        .................................
"""))
game.set_dialog_cursor(img("""
    . f f f . f f f f . f f f . 
        f f f f f c c c c f f f f f 
        f f f f b c c c c b f f f f 
        f f f c 3 c c c c 3 c f f f 
        . f 3 3 c c c c c c 3 3 f . 
        . f c c c c 4 4 c c c c f . 
        . f f c c 4 4 4 4 c c f f . 
        . f f f b f 4 4 f b f f f . 
        . f f 4 1 f d d f 1 4 f f . 
        . . f f d d d d d d f f . . 
        . . e f e 4 4 4 4 e f e . . 
        . e 4 f b 3 3 3 3 b f 4 e . 
        . 4 d f 3 3 3 3 3 3 c d 4 . 
        . 4 4 f 6 6 6 6 6 6 f 4 4 . 
        . . . . f f f f f f . . . . 
        . . . . f f . . f f . . . .
"""))
game.show_long_text("\"Left and right buttons to move\"", DialogLayout.BOTTOM)
game.show_long_text("\"Press a to jump.\"", DialogLayout.BOTTOM)
beibie = sprites.create(img("""
        . f f f . f f f f . f f f . 
            f f f f f c c c c f f f f f 
            f f f f b c c c c b f f f f 
            f f f c 3 c c c c 3 c f f f 
            . f 3 3 c c c c c c 3 3 f . 
            . f c c c c 4 4 c c c c f . 
            . f f c c 4 4 4 4 c c f f . 
            . f f f b f 4 4 f b f f f . 
            . f f 4 1 f d d f 1 4 f f . 
            . . f f d d d d d d f f . . 
            . . e f e 4 4 4 4 e f e . . 
            . e 4 f b 3 3 3 3 b f 4 e . 
            . 4 d f 3 3 3 3 3 3 c d 4 . 
            . 4 4 f 6 6 6 6 6 6 f 4 4 . 
            . . . . f f f f f f . . . . 
            . . . . f f . . f f . . . .
    """),
    SpriteKind.player)
scene.camera_follow_sprite(beibie)
tiles.set_current_tilemap(tilemap("""
    map
"""))
Create_monsters()
tiles.place_on_tile(beibie, tiles.get_tile_location(0, 5))
controller.move_sprite(beibie, 100, 0)
beibie.ay = 1000
pause(2000)
# generate monsters constantly with given interval
# register and set updating logic

def on_update_interval():
    Create_monsters()
game.on_update_interval(3000, on_update_interval)
