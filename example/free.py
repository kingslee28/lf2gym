import lf2gym


env = lf2gym.make(startServer=True, wrap='skip4', driverType=lf2gym.WebDriver.Chrome,
    characters=[lf2gym.Character.Freeze, lf2gym.Character.Firen],
    difficulty=lf2gym.Difficulty.Dumbass, versusPlayer=True, debug=True)

# Set the reset options
options = env.get_reset_options();
print('Original reset options: %s' % options)
options['hp_full'] = 100
options['mp_start'] = 250
print('Custom reset options: %s' % options)

# Reset the env
env.reset(options)

# Game starts
done = False
while not done:
    action = env.action_space.sample()
    _, reward, done, _, _ = env.step(action)

# Game ends
print('Gameover!')