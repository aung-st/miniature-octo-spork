--prelude no likey when I call it elem
elem' :: (Eq a) => a -> [a] -> Bool
elem' _ [] = False
elem' n (x:xs)
    | x == n = True
    | otherwise = elem' n xs

--returns a list without any dupe elements
nub :: (Eq a) => [a] -> [a]
nub [] = []
nub (x:xs) 
    | x `elem'` xs == False = x:nub xs
    | otherwise = nub xs

--check if a list is in ascending order
isAsc :: [Int] -> Bool
isAsc [] = True
isAsc [_] = True
isAsc (x:y:xss)
    | x == y = isAsc xss
    | y > x = isAsc xss
    | otherwise = False

--check if there is a path from x to y
-- [(1,4) (2,3) (4,3)] 4 3 == True
-- [(1,2) (2,3) (4,3)] 3 4 == False
hasPath :: [(Int, Int)] -> Int -> Int -> Bool
hasPath [] x y = x == y
hasPath (b:bs) x y
    | x == y = True 
    | x == fst b && y == snd b = True                                  
    | x == fst b = hasPath bs (snd b) y                                
    | y == snd b = hasPath bs x (fst b)  || hasPath bs x y   
    | otherwise = hasPath bs x y                                          