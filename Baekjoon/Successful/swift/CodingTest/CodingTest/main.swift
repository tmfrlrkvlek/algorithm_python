//
//  main.swift
//  CodingTest
//
//  Created by 이지수 on 2021/09/04.
//

import Foundation

let n: Int = Int(readLine() ?? "0") ?? 0

struct Location: Equatable{
    let x: Double
    let y: Double
    let distance: Double
    
    init(x: String, y: String, distance: String){
        self.x = Double(x) ?? 0
        self.y = Double(y) ?? 0
        self.distance = Double(distance) ?? 0
    }
    
    static func == (lhs: Location, rhs: Location) -> Bool{
        lhs.x == rhs.x && lhs.y == rhs.y && lhs.distance == rhs.distance
    }
    
    func distance(with endPoint: Location) -> Double{
        sqrt(pow(self.x - endPoint.x, 2) + pow(self.y - endPoint.y, 2))
    }
    
    func meetCount(with otherSide: Location) -> Int{
        let minDistance = self.distance(with: otherSide)
        let totalDistance = self.distance + otherSide.distance
        let minRadius = min(self.distance, otherSide.distance)
        let maxRadius = max(self.distance, otherSide.distance)
        if self == otherSide { return -1 }
        else if minDistance < maxRadius {
            if maxRadius - minDistance <  minRadius { return 2 }
            else if maxRadius - minDistance == minRadius { return 1 }
            return 0
        }else{
            if totalDistance == minDistance { return 1 }
            else if totalDistance < minDistance { return 0 }
            return 2
        }
    }
}

for _ in 0..<n {
    let data: [String] = (readLine() ?? "").components(separatedBy: " ")
    let person1 = Location(x: data[0], y: data[1], distance: data[2])
    let person2 = Location(x: data[3], y: data[4], distance: data[5])
    print(person1.meetCount(with: person2))
}
