import Data.List.Split

main :: IO()
main = do 
    input <- parseInput <$> getContents
    putStrLn $ show $ distance input

parseInput :: String -> [String]
parseInput = splitOn "," . head . lines

calcDist :: Integer -> Integer -> Integer
calcDist x y = max (abs x) (abs y)

distance :: [String] -> (Integer, Integer)
distance = distance' (0,0) 0

-- Returns Integer Tuple of (dist, maxDist)
distance' :: (Integer, Integer) -> Integer -> [String] -> (Integer, Integer)
distance' (x,y) z [] = (calcDist x y, z)
distance' (x,y) z (d:xs) = 
    case d of 
      "n"  -> distance' (x,y+1)   (max (calcDist x y) z) xs
      "s"  -> distance' (x,y-1)   (max (calcDist x y) z) xs
      "ne" -> distance' (x+1,y+1) (max (calcDist x y) z) xs
      "se" -> distance' (x+1,y-1) (max (calcDist x y) z) xs
      "nw" -> distance' (x-1,y+1) (max (calcDist x y) z) xs
      "sw" -> distance' (x-1,y-1) (max (calcDist x y) z) xs
      _    -> distance' (x,y)     (max (calcDist x y) z) xs

