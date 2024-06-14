# FrozenDawn Rod Game and Solver
 This is a minigame from COD WW2 zombies that appears in one of the levels. It's a rod that when you shoot it changes directions. Here I've recreated the game and included a GUI to solve it

RodGame.py recreates the game. The rules of the game are that you choose to 'shoot' one of each of the blocks on a rod. I've labeled them rod A-D from top to bottom, so A is top, D is the bottom. When you 'shoot' one of the blocks the block that was shot will spin 2 times and will force the blocks both above and below to spin 1 time. So if block B was shot then block A would spin from front(0) position to right(1) position. Block B would spin from front(0) position to back(2) position. Block C would spin from front(0) to right(1) position. The object of the game is to get all of the blocks to face front(0) position.

window_test.py is the GUI solver. You move each of the blocks to match the ingame block positions. When you click submit it will find the shortest possible solution. The results will be a list of length 4. An example result would be [1,0,1,2] which would mean shoot A block 1 time, B block 0 times, C block 1 time, and D block 2 times.
