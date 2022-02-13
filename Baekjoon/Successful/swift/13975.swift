// 13975
import Foundation

let t = Int(readLine()!)!
for _ in 0..<t {
    let _ = Int(readLine()!)!
    let chs = readLine()!.split(separator:" ").map(){Int(String($0))!}
    let heap = MinHeap(elements: chs)
    print(minCost(heap))
}

func minCost(_ heap: MinHeap) -> Int {
    var heap = heap
    var cost = 0
    while heap.count > 1 {
        let ch1 = heap.pop()
        let ch2 = heap.pop()
        heap.insert(ch1+ch2)
        cost += ch1+ch2
    }
    return cost
}

struct MinHeap {
    private var elements: [Int] = []
    init(elements: [Int]) {
        for e in elements { self.insert(e) }
    }
    var count: Int {
        return self.elements.count
    }
    private var lastIndex: Int {
        return self.count - 1
    }
    private func rightChild(of index: Int) -> Int? {
        guard index*2+2 < self.count else { return nil }
        return index*2+2
    }
    private func leftChild(of index: Int) -> Int? {
        guard index*2+1 < self.count else { return nil }
        return index*2+1
    }
    private func parent(of index: Int) -> Int? {
        guard index > 0 else { return nil }
        return (index-1)/2
    }
    private mutating func swap(_ index1: Int, _ index2: Int) {
        let temp = self.elements[index1]
        self.elements[index1] = self.elements[index2]
        self.elements[index2] = temp
    }
    func node(of index: Int) -> Int {
        return self.elements[index]
    }
    mutating func insert(_ node: Int) {
        self.elements.append(node)
        var child = self.lastIndex
        while let parents = parent(of: child),
            self.elements[parents] > node {
            swap(parents, child)
            child = parents
        }
    }
    mutating func delete() {
        swap(self.lastIndex, 0)
        self.elements.remove(at: self.lastIndex)
        var current = 0
        var lChild = leftChild(of: current)
        var rChild = rightChild(of: current)
        while current < self.count, 
        self.elements[current] > self.elements[lChild ?? current] || self.elements[current] > self.elements[rChild ?? current] {
            if let lChild = lChild,
            let rChild = rChild {
                if self.elements[lChild] < self.elements[rChild] {
                    swap(current, lChild)
                    current = lChild
                } else {
                    swap(current, rChild)
                    current = rChild
                }
            } else if let lChild = lChild {
                swap(current, lChild)
                current = lChild
            } else if let rChild = rChild {
                swap(current, rChild)
                current = rChild
            } else { break }
            lChild = leftChild(of: current)
            rChild = rightChild(of: current)
        }
    }
    mutating func pop() -> Int {
        let removeElement = self.elements[0]
        self.delete()
        return removeElement
    }
}