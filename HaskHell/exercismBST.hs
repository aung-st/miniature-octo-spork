module BST
    ( BST
    , bstLeft
    , bstRight
    , bstValue
    , empty
    , fromList
    , insert
    , singleton
    , toList
    ) where
    
data BST a =  Empty | Node a (BST a) (BST a) deriving (Eq, Show)
bstLeft :: BST a -> Maybe (BST a)
bstLeft Empty = Nothing
bstLeft (Node _ left _) = Just left

bstRight :: BST a -> Maybe (BST a)
bstRight Empty = Nothing
bstRight (Node _ _ right) = Just right

bstValue :: BST a -> Maybe a
bstValue (Node n _ _) = Just n
bstValue Empty = Nothing

empty :: BST a
empty = Empty

fromList :: Ord a => [a] -> BST a
fromList xs = foldr insert Empty (reverse xs)

insert :: Ord a => a -> BST a -> BST a
insert x Empty = singleton x
insert x (Node n left right)
  | x > n = Node n left (insert x right)
  | otherwise = Node n (insert x left) right

singleton :: a -> BST a
singleton x = (Node x Empty Empty)

toList :: BST a -> [a]
toList Empty = []
toList (Node n left right) = (toList left) ++ [n] ++ (toList right) 
