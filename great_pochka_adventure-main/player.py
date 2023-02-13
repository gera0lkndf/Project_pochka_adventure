from pygame import *
import pyganim

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#249843"
JUMP_POWER = 10
GRAVITY = 0.25
ANIMATION_DELAY = 0.1

ANIMATION_RIGHT = ['pochka/r1.png',
                   'pochka/r2.png',
                   'pochka/r3.png',
                   'pochka/r2.png',
                   'pochka/r3.png']
ANIMATION_LEFT = ['pochka/l1.png',
                  'pochka/l2.png',
                  'pochka/l3.png',
                  'pochka/l2.png',
                  'pochka/l3.png']
ANIMATION_JUMP_LEFT = [('pochka/jl.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('pochka/jr.png', 0.1)]
ANIMATION_JUMP = [('pochka/j.png', 0.1)]
ANIMATION_STAY = [('pochka/0.png', 0.1)]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.speed = 0
        self.startX = x
        self.startY = y
        self.jspeed = 0
        self.onGround = True
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image.set_colorkey(Color(COLOR))
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

    def update(self, left, right, up, platforms):

        if up:
            if self.onGround:
                self.jspeed = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if left:
            self.speed = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.speed = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not (left or right):
            self.speed = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.jspeed += GRAVITY

        self.onGround = False
        self.rect.y += self.jspeed
        self.collide(0, self.jspeed, platforms)

        self.rect.x += self.speed
        self.collide(self.speed, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.jspeed = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.jspeed = 0