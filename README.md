## Practice Journal 

Easy 
* https://leetcode.com/problemset/algorithms/?page=1&difficulty=EASY

Medium 
* https://leetcode.com/problemset/algorithms/?page=1&difficulty=MEDIUM

Dynamic programming 
* https://leetcode.com/tag/dynamic-programming/

## Round 4
### 136. Single Number
https://leetcode.com/problems/single-number/

### 99. Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/

### 215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

### 149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

### 140. Word Break II
https://leetcode.com/problems/word-break-ii/

### 148. Sort List
https://leetcode.com/problems/sort-list/

### 173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/


### 142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/

### 295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

### 330. Patching Array
https://leetcode.com/problems/patching-array/
## Round 3
### 150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/

### 51. N-Queens
https://leetcode.com/problems/n-queens/

### 4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

### 273. Integer to English Words
https://leetcode.com/problems/integer-to-english-words/

### 91. Decode Ways
https://leetcode.com/problems/decode-ways/

### 452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

### 15. 3Sum
https://leetcode.com/problems/3sum/

### 16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/

### 24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/

### 34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

### 790. Domino and Tromino Tiling
https://leetcode.com/problems/domino-and-tromino-tiling/

In how many ways can you fit 1 X 1 X 2 sized dominoes into a domino of dimensions 2 X 2 X N, where N is a variable?

## Round 2
https://leetcode.com/problemset/all/

### 85. Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/

### Available Meeting Time

A group of friends decided to meetup on a chosen date. Everyone in the group provided his/her schedule on that date.
Finally you are given a joined schedule of all members, which lists all the time slots when at least one member is unavailable.

The schedule is a list of lists. Each element in the list is a pair of strings

```
[
[startTime1, endTime1],
[startTime2, endTime2],
[startTime3, endTime3]
]
```
Start time and end time follows the format HHMM, where the first 2 digits denote hour and the last 2 digits denote minute.

Your job is to find all the potential time slots for the meetup. Find all time slots that

between 700 and 1800
when all group members are available

Example 1:
```
Input: schedule = [[1600, 1630], [600, 730], [800, 920], [800, 900], [1730, 1920]]
Output: [[730, 800], [920, 1600], [1630, 1730]]
```
Example 2:
```
Input: schedule = [[1200, 1730], [800, 1000], [1000, 1130]]
Output: [[700, 800], [1130, 1200], [1730, 1800]]
```

### 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

### 218. The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/

### 84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/

### 85. Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/

### 38. Count and Say
https://leetcode.com/problems/count-and-say/

### 36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

### 48. Rotate Image
https://leetcode.com/problems/rotate-image/

### 3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

### 5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

### 64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

### 46. Permutations
https://leetcode.com/problems/permutations/

### 78. Subsets
https://leetcode.com/problems/subsets/

### 23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

### 25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

### 30. Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

### 44. Wildcard Matching
https://leetcode.com/problems/wildcard-matching/

### 233. Number of Digit One 
https://leetcode.com/problems/number-of-digit-one/

## Round 1
### Move Zeros To End

Given a static-sized array of integers arr, move all zeroes in the array to the end of the array. You should preserve the relative order of items in the array.

We should implement a solution that is more efficient than a naive brute force.

Examples:
```
input:  arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
     output:  [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]
```
### Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:
```
input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
```
### Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.

Examples:
```
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.
source = "no", target = "go"
words = ["to"]

output: -1
```

### Toeplitz Matrix
A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix. The matrix can be any dimensions, not necessarily square.

For example,

```
[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
```
is a Toeplitz matrix, so we should return true, while

```
[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]
```
isn’t a Toeplitz matrix, so we should return false.

### BST Successor Search
In a Binary Search Tree (BST), an Inorder Successor of a node is defined as the node with the smallest key greater than the key of the input node (see examples below). Given a node inputNode in a BST, you’re asked to write a function findInOrderSuccessor that returns the Inorder Successor of inputNode. If inputNode has no Inorder Successor, return null.

Explain your solution and analyze its time and space complexities.

```
             20
           9   25
         5  12
           11 14
```           

In this diagram, the inorder successor of 9 is 11 and the inorder successor of 14 is 20.

Example:

In the diagram above, for inputNode whose key = 11

Your function would return:

The Inorder Successor node whose key = 12

```
class Node:

  # Constructor to create a new node
  def __init__(self, key):
    self.key = key 
    self.left = None
    self.right = None
    self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
    self.root = None 

  def find_in_order_successor(self, inputNode):
    pass # your code goes here

  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid 
  # using reference parameters)
  def insert(self, key):
    
    # 1) If tree is empty, create the root
    if (self.root is None):
      self.root = Node(key)
      return
        
    # 2) Otherwise, create a node with the key
    #    and traverse down the tree to find where to
    #    to insert the new node
    currentNode = self.root
    newNode = Node(key)
    while(currentNode is not None):
      
      if(key < currentNode.key):
        if(currentNode.left is None):
          currentNode.left = newNode;
          newNode.parent = currentNode;
          break
        else:
          currentNode = currentNode.left;
      else:
        if(currentNode.right is None):
          currentNode.right = newNode;
          newNode.parent = currentNode;
          break
        else:
          currentNode = currentNode.right;

  # Return a reference to a node in the BST by its key.
  # Use this method when you need a node to test your
  # findInOrderSuccessor function on
  def getNodeByKey(self, key):
    
    currentNode = self.root
    while(currentNode is not None):
      if(key == currentNode.key):
        return currentNode
        
      if(key < currentNode.key):
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
        
    return None
        
######################################### 
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst  = BinarySearchTree()
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

# Get a reference to the node whose key is 9
test = bst.getNodeByKey(9)

# Find the in order successor of test
succ = bst.find_in_order_successor(test)

# Print the key of the successor node
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")

```
### Pairs with Specific Difference
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:
```
input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
```

template
```
def find_pairs_with_given_difference(arr, k):
  pass
```

### Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:
```
input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
```

template
```
def find_array_quadruplet(arr, s):
  pass
```
### K-Messed Array Sort
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:
```
input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```
def sort_k_messed_array(arr, k):
    pass
```

### Busiest Time in The Mall
The Westfield Mall management is trying to figure out what the busiest moment at the mall was last year. You’re given data extracted from the mall’s door detectors. Each data point is represented as an integer array whose size is 3. The values at indices 0, 1 and 2 are the timestamp, the count of visitors, and whether the visitors entered or exited the mall (0 for exit and 1 for entrance), respectively. Here’s an example of a data point: [ 1440084737, 4, 0 ].

Note that time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Given an array, data, of data points, write a function findBusiestPeriod that returns the time at which the mall reached its busiest moment last year. The return value is the timestamp, e.g. 1480640292. Note that if there is more than one period with the same visitor peak, return the earliest one.

Assume that the array data is sorted in an ascending order by the timestamp. Explain your solution and analyze its time and space complexities.

Example:
```
input:  data = [ [1487799425, 14, 1], 
                 [1487799425, 4,  0],
                 [1487799425, 2,  0],
                 [1487800378, 10, 1],
                 [1487801478, 18, 0],
                 [1487801478, 18, 1],
                 [1487901013, 1,  0],
                 [1487901211, 7,  1],
                 [1487901211, 7,  0] ]

output: 1487800378 # since the increase in the number of people
                   # in the mall is the highest at that point
```

```
def find_busiest_period(data):
    pass
```

### Shifted Array Search
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

Explain your solution and analyze its time and space complexities.

Example:

```
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since it’s the index of 2 in arr
```
```
def shifted_arr_search(shiftArr, num):
    pass
```
### Array Index & Element Equality
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:
```
input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.
```
```
def index_equals_value_search(arr):
    pass
```
### Matrix Spiral Copy
Given a 2D array (matrix) inputMatrix of integers, create a function spiralCopy that copies inputMatrix’s values into a 1D array in a spiral order, clockwise. Your function then should return that array. Analyze the time and space complexities of your solution.

Example:
```
input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
```

```
def spiral_copy(inputMatrix):
  pass # your code goes here
```
### Rearrange Array

Given an array {a0, a1, a2, ... an, b0, b1, b2 ... bn}, Rearrange this array into {a0, b0, a1, b1, a2, b2, ... an, bn} inplace, O (1) space

### Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

Examples:
```
input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
```
Important: please convert the occurrence integers in the output list to strings (e.g. "3" instead of 3). We ask this because in compiled languages such as C#, Java, C++, C etc., it’s not straightforward to create mixed-type arrays (as it is, for instance, in scripted languages like JavaScript, Python, Ruby etc.). The expected output will simply be an array of string arrays.

```
def word_count_engine(document):
    pass
```

### Smallest Substring of All Characters
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:
```
input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"
```

```
def get_shortest_unique_substring(arr, s):
```

### Getting a Different Number
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.

Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Example:
```
input:  arr = [0, 1, 2, 3]

output: 4 
```

```
def get_different_number(arr):
```

### Bracket Match
A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.

Examples:
```
input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())(”
output: 2
```
```
def bracket_match(text):
```

### Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities.

Examples:
```
input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose duration is 12
```

```
def meeting_planner(slotsA, slotsB, dur):
```

### Drone Flight Planner
You’re an engineer at a disruptive drone delivery startup and your CTO asks you to come up with an efficient algorithm that calculates the minimum amount of energy required for the company’s drone to complete its flight. You know that the drone burns 1 kWh (kilowatt-hour is an energy unit) for every mile it ascends, and it gains 1 kWh for every mile it descends. Flying sideways neither burns nor adds any energy.

Given an array route of 3D points, implement a function calcDroneMinEnergy that computes and returns the minimal amount of energy the drone would need to complete its route. Assume that the drone starts its flight at the first point in route. That is, no energy was expended to place the drone at the starting point.

For simplicity, every 3D point will be represented as an integer array whose length is 3. Also, the values at indexes 0, 1, and 2 represent the x, y and z coordinates in a 3D point, respectively.

Explain your solution and analyze its time and space complexities.

Example:
```
input:  route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]

output: 5 # less than 5 kWh and the drone would crash before the finish
          # line. More than `5` kWh and it’d end up with excess energy
```

```
def calc_drone_min_energy(route):
```

### Basic Regex Parser
Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.

In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). For more information on regular expression matching, see the Regular Expression Wikipedia page.

Explain your algorithm, and analyze its time and space complexities.

Examples:
```
input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true
```

### Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.

Examples:
```
input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
```
```
def deletion_distance(str1, str2):
```
### Pancake Sort
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
Example:
```
input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] 
```
Analyze the time and space complexities of your solution.

Note: it’s called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only use the spatula to flip some of the top pancakes in the plate. 

```
5 1 4 3 2
2 3 4 1 5
4 3 2 1 5
1 2 3 4 5
3 2 1 4 5
1 2 3 4 5
2 1 3 4 5
1 2 3 4 5
```

```
def pancake_sort(arr):
def flip(arr, k):
```


### Flatten a Dictionary
A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

If you’re using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

If a certain key is empty, it should be excluded from the output (see e in the example below).

Example:
```
input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
```        
Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d the result key would be Key2.c.d.

```
def flatten_dictionary(dictionary):
  pass # your code goes here
```  
### Root of Number
Many times, we need to re-implement basic functions without using any standard library functions already implemented. For example, when designing a chip that requires very little memory space.

In this question we’ll implement a function root that calculates the n’th root of a number. The function takes a nonnegative number x and a positive integer n, and returns the positive n’th root of x within an error of 0.001 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

Don’t be intimidated by the question. While there are many algorithms to calculate roots that require prior knowledge in numerical analysis (some of them are mentioned here), there is also an elementary method which doesn’t require more than guessing-and-checking. Try to think more in terms of the latter.

Make sure your algorithm is efficient, and analyze its time and space complexities.

Examples:
```
input:  x = 7, n = 3
output: 1.913

input:  x = 9, n = 2
output: 3
```

```
import math
def root(x, n):

```
### Largest Smaller BST Key
Given a root of a Binary Search Tree (BST) and a number num, implement an efficient function findLargestSmallerKey that finds the largest key in the tree that is smaller than num. If such a number doesn’t exist, return -1. Assume that all keys in the tree are nonnegative.

Analyze the time and space complexities of your solution.

For example:

For num = 17 and the binary search tree below:
```
      20
    9    25
  5   12 
     11 14
```
Your function would return:

14 since it’s the largest key in the tree that is still smaller than 17.

```
##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################


# A node 
class Node:

# Constructor to create a new node
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
      self.root = None

  def find_largest_smaller_key(self, num):
    pass

  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid
  # using reference parameters)
  def insert(self, key):

      # 1) If tree is empty, create the root
      if (self.root is None):
          self.root = Node(key)
          return

      # 2) Otherwise, create a node with the key
      #    and traverse down the tree to find where to
      #    to insert the new node
      currentNode = self.root
      newNode = Node(key)

      while(currentNode is not None):
        if(key < currentNode.key):
          if(currentNode.left is None):
            currentNode.left = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.left
        else:
          if(currentNode.right is None):
            currentNode.right = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.right

######################################### 
# Driver program to test above function #
#########################################

bst  = BinarySearchTree()
 
# Create the tree given in the above diagram 
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

result = bst.find_largest_smaller_key(17)

print ("Largest smaller number is %d " %(result))

```

### H-Tree Construction
An H-tree is a geometric shape that consists of a repeating pattern resembles the letter “H”.

It can be constructed by starting with a line segment of arbitrary length, drawing two segments of the same length at right angles to the first through its endpoints, and continuing in the same vein, reducing (dividing) the length of the line segments drawn at each stage by 2.

Here are some examples of H-trees at different levels of depth:

https://github.com/quanewang/public/blob/master/H.png

Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates), a starting length, and depth. Assume that the starting line is parallel to the X-axis.

Use the function drawLine provided to implement your algorithm. In a production code, a drawLine function would render a real line between two points. However, this is not a real production environment, so to make things easier, implement drawLine such that it simply prints its arguments (the print format is left to your discretion).

Analyze the time and space complexity of your algorithm. In your analysis, assume that drawLine's time and space complexities are constant, i.e. O(1).

### Koch snowflake
Using draw functions to draw snow flakes.

draw functions
* left(degree), e.g., left(60), turn left for 60 degree
* right(degree) 
* draw(length), e.g., draw(10), draw line of length 10

https://github.com/quanewang/public/blob/master/kochsnowflake.png

```
def koch(length=1, depth=0):
    path
```

## HackerRank

### Alexa
Amazon's Alexa team is working on optimizing the customer experience for scenarios where customers ask generic questions. One example of a generic question is "What are good vegetarian restaurants nearby?"  In this example, Alexa would then search for a list of vegetarian restaurants in the city and select the nearest X vegetarian restaurants relative to the customer's location. Given an array representing the locations of N vegetarian restaurants in the city, implement an algorithm to find the nearest X vegetarian restaurants to the customer's location.
```
Input
The input to the function/method consists of two arguments:
allLocations, a list of elements where each element consists of a pair of integers representing the x and y coordinates of the vegetarian restaurant in the city;
numRestaurants, an integer representing the number of nearby vegetarian restaurants that would be returned to the customer (X).

Output
Return a list of elements where each element of the list represents the x and y integer coordinates of the nearest recommended vegetarian restaurant relative to customer’s location. If there is a tie, return any of the locations as long as you satisfy retuning exactly X nearby vegetarian restaurants. If no location is possible, return a list with an empty location - not just an empty list.

Constraints
numRestaurants ≤ size(allLocations)

Note
The customer begins at the location [0, 0].
The distance from the customer's current location to a recommended vegetarian restaurant location (x, y) is the square root of x2 + y2.
If there are ties then return any of the locations as long as you satisfy returning exactly X nearby vegetarian restaurants.
The returned output can be in any order.

Example
Input:
allLocations = [[1, 2], [3, 4], [1, -1]]
numRestaurants = 2

Output:
[[1, -1], [1, 2]]

Explanation:
The distance of the customer's current location from location [1, 2] is square root(5) = 2.236
The distance of the customer's current location from location [3, 4] is square root(25) = 5
The distance of the customer's current location from location [1, -1] is square root(2) = 1.414
The required number of vegetarian restaurants is 2, hence the output is [1, -1] and [1, 2].
```

### Economy Mart
Economy Mart is a very popular e-commerce platform because they display the cheapest items first. Economy Mart has decided to migrate its database to Amazon's cloud platform. The product listings in the old database are being migrated into the Amazon database. Customers that go onto Amazon.com will be viewing items from the new database.

```
Economy Mart has an unusual way of displaying items,

If a customer views the first item, they will be shown the cheapest item in the database
If a customer is currently viewing the kth cheapest item, viewing the next item will display the (k+1)th cheapest item.
If multiple items have the same price, they are ordered alphabetically ascending.
 
There are 2 types of entries:

The first element in the row is “INSERT” followed by the name of the item (String) and its price (String denoting an Integer). This describes an item being added to the database.
The first element in the row is the word “VIEW”. This is when the customer views an item. The other 2 elements in these rows contain "-" that can be ignored. It is guaranteed that at least one item is added to the database when a customer views an item.
                                                    Table of entries

 	Parameter 1	Parameter 2	Parameter 3
Entry 1	“INSERT”	itemName	price
Entry 2	“VIEW”	"-" (without quotes)	"-" (without quotes)
 
Note: The price of each item is in string format so you may need to convert it to an integer before using it.

While the database is being transferred, an unknowing customer logs onto the website and browses some of Economy Mart's items. Given a server log in chronological order, determine which items were shown to the customer.

Example

entries = [['INSERT', 'milk', '4'], ['INSERT', 'coffee', '3'], ['VIEW', '-', '-'], ['INSERT', 'pizza', '5'], ['INSERT', 'gum', '1'], ['VIEW', '-', '-']]

Let's consider the following entries in the database:

INSERT milk 4
INSERT coffee 3
VIEW - -
INSERT pizza 5
INSERT gum 1
VIEW - -
 
In this case, milk and coffee are added to the database at costs of 4 and 3, respectively. When the customer logs onto the site, the cheapest item in the database is shown: coffee.

While the customer is browsing, pizza and gum are added to the database. Pizza is worth 5 and gum is worth 1. When the customer views the next cheapest item, the items in the database in sorted order are gum (1), coffee (3), milk (4), and pizza (5). Since the customer is viewing for the second time, the second cheapest item, coffee, will be shown again.

Return ['coffee', 'coffee'].

Function Description
Complete the function getItems in the editor below.

getItems has the following parameters:
    string entries[n][3]: each row in the matrix represents an individual log entry
Returns
    string[]: answers to each of the "VIEW" queries
Constraints
1 ≤ n ≤ 105
1 ≤ | itemName | ≤ 10 (The name of each item will be 1 to 10 characters long)
Item names will only consist of lowercase English letters.
All itemName strings are distinct 
1 ≤ price ≤ 109
k ≤ length of the database (That is, there will always be at least k items in the database when the customer is viewing for the kth time)
```
