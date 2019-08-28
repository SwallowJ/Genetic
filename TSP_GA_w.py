# -*- encoding: utf-8 -*-

import random
import math
import sys
      
from GA import GA

class TSP_WIN:
      def __init__(self, citys, city_distance):
            self.lifeCount = 100
            self.citys = citys
            self.city_distance = city_distance

      def distance(self, order):
            distance = 0.0
            for i in range(-1, len(self.citys) - 1):
                  index1, index2 = order[i], order[i + 1]
                  city1, city2 = self.citys[index1], self.citys[index2]
                  distance += self.city_distance[city1][city2]
            return distance

      def matchFun(self):
            return lambda life: 1.0 / self.distance(life.gene)
     

      def new(self, evt = None):
            self.isRunning = False
            self.ga = GA(
                  aCrossRate = 0.7, 
                  aMutationRage = 0.02,
                  aLifeCount = self.lifeCount, 
                  aGeneLenght = len(self.citys), 
                  aMatchFun = self.matchFun())

      def start(self, evt = None):
            self.new()
            self.isRunning = True
            self.length_generation = []
            self.end_data = []
            while self.isRunning:
                  self.ga.gnext()
                  distance = self.distance(self.ga.best.gene)
                  self.length_generation.append(distance)
                  if(self.ga.generation > 1000):
                        if self.length_generation[self.ga.generation - 10] == self.length_generation[self.ga.generation - 500]:
                              for i in range(len(self.ga.best.gene)):
                                    self.end_data.append(self.citys[self.ga.best.gene[i]])
                                    # print(self.citys[self.ga.best.gene[i]])

                              # return self.ga.best.gene
                              self.isRunning = False
            return self.end_data

def main(citys,city_distance):
      tsp = TSP_WIN(citys, city_distance)
      return tsp.start()

if __name__ == '__main__':
      citys = ["A", "B", "C", "D"]
      distance = {
            "A":{"A":0,"B":14,"C":13,"D":17},
            "B":{"A":14,"B":0,"C":5,"D":17},
            "C":{"A":13,"B":5,"C":0,"D":15},
            "D":{"A":17,"B":17,"C":15,"D":0}
      }
      print(main(citys, distance))