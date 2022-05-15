data BinTree = Leaf Int|Branch BinTree Int BinTree deriving Show

--output value of all leaf nodes 
printNodes :: BinTree -> Int
printNodes (Leaf n) = n 
printNodes (Branch left y right) = printNodes left + printNodes right

--how we define an empty leaf 
emptyTree :: BinTree
emptyTree = Leaf 0

--delete a node and all its children
deleteJeremy :: BinTree  -> Int -> BinTree 
deleteJeremy (Branch left y right) n = if n == y then Leaf 0 else  Branch (deleteJeremy left n) y (deleteJeremy right n)
deleteJeremy (Leaf x) n = if n == x then Leaf 0 else Leaf x 

--display a tree as a list
toList :: BinTree -> [Int]
toList (Leaf n) = [n]
toList (Branch left y right) = toList left ++ [y] ++ toList right  

--sum of value of all nodes 
sumTree :: BinTree -> Int 
sumTree ts = sum $ toList ts