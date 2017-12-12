import Data.List.Split

main :: IO()
main = do 
    input <- parseInput <$> readFile "input.in" 
    putStrLn $ show $ distance input

parseInput :: String -> [String]
parseInput = splitOn "," . head . lines

distance :: [String] -> Integer
distance = distance' (0,0)

distance' :: (Integer, Integer) -> [String] -> Integer
distance' (x,y) [] = max (abs x) (abs y)
distance' (x,y) (d:xs) = 
    case d of 
      "n"  -> distance' (x,y+1)   xs
      "s"  -> distance' (x,y-1)   xs
      "ne" -> distance' (x+1,y+1) xs
      "se" -> distance' (x+1,y-1) xs
      "nw" -> distance' (x-1,y+1) xs
      "sw" -> distance' (x-1,y-1) xs
      _    -> distance' (x,y)     xs

