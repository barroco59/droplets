#!/usr/bin/env python
#coding:utf-8
from graph import Graph
from Queue import PriorityQueue
from sets import Set

def run(graph,start,goal):
    frontier = PriorityQueue()
    frontier.put((0,start))
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()[1]
        if current == goal:
            break
        for next in graph.neighbors(current):
            new_cost = graph.gcost(next,goal)
            if next not in came_from:
                frontier.put((new_cost,next))
                came_from[next] = current

    #for x in came_from:
    #    print x,came_from[x]
    print len(came_from)

    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    print path


if __name__ == "__main__":
    graph = Graph(10,10)
    start = (3,3)
    goal = (6,6)
    run(graph,start,goal)


