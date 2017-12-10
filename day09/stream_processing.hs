main :: IO()
main = do 
    input <- getContents 
    putStrLn $ "First: " ++ show (process input 0 0)
    putStrLn $ "Second: " ++ show (garbageCount input 0)

-- Part 1
process :: String -> Integer -> Integer -> Integer
process [] _ score = score
process ('{':xs) depth score =  process xs (depth+1) score
process ('}':xs) depth score = process xs (depth-1) score+depth
process ('!':_:xs) depth score = process xs depth score
process ('<':xs) depth score = process (garbage xs) depth score
process (_:xs) depth score = process xs depth score

garbage :: String -> String
garbage [] = []
garbage ('!':_:xs) = garbage xs
garbage ('>':xs) = xs
garbage (_:xs) = garbage xs

-- Part 2 
garbageCount :: String -> Integer -> Integer
garbageCount [] count = count
garbageCount ('!':_:xs) count = garbageCount xs count
garbageCount ('<':xs) count = garbageInner xs count
garbageCount (_:xs) count = garbageCount xs count

garbageInner :: String -> Integer -> Integer
garbageInner [] count = count
garbageInner ('!':_:xs) count = garbageInner xs count
garbageInner ('>':xs) count = garbageCount xs count
garbageInner (_:xs) count = 1 + garbageInner xs count
