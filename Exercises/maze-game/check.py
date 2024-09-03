import pygame, sys, threading, queue
from maze.manager import GameManager
from maze.statics import BlockType

manager = GameManager()
command_queue = queue.Queue()
result_queue = queue.Queue()

# time limit (frames)
time_limit = 30 * 60

def turn_left():
    command_queue.put("TURN_LEFT")

def turn_right():
    command_queue.put("TURN_RIGHT")

def move_forward():
    command_queue.put("MOVE_FORWARD")

def try_exit():
    command_queue.put("TRY_EXIT")

def check_front():
    command_queue.put("CHECK_FRONT")
    result = result_queue.get()
    return result

def main():
    from logic import operation
    # Initial Draw
    manager.draw()
    pygame.display.flip()
    
    running_time = 0
    
    solve_thread = threading.Thread(target=operation)
    solve_thread.daemon = True
    solve_thread.start()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        while not command_queue.empty():
            command = command_queue.get()
            if command == "CHECK_FRONT":
                result_queue.put(manager.check_front())
            elif command == "TURN_LEFT":
                manager.turn_left()
                manager.update()
                manager.turn_draw()
                pygame.display.flip()
            elif command == "TURN_RIGHT":
                manager.turn_right()
                manager.update()
                manager.turn_draw()
                pygame.display.flip()
            elif command == "MOVE_FORWARD":
                manager.try_move()
                manager.update()
                manager.move_draw()
                pygame.display.flip()
            elif command == "TRY_EXIT":
                if manager.try_exit():
                    print("WIN")
                    pygame.quit()
                    sys.exit()
        manager.clock.tick(30)
        running_time += 1
        if running_time > time_limit:
            print("TIME LIMIT EXCEEDED")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()