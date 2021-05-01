def check_collision(player, pipe):
    return player.rect.colliderect(pipe.rect1) or player.rect.colliderect(pipe.rect2)