import Data.List

main :: IO()
main = do 
    input <- getContents 
    let phrases = lines input
    putStrLn $ show $ amountOfValid hasNoDuplicates phrases
    putStrLn $ show $ amountOfValid hasNoAnagrams phrases

amountOfValid :: ([String] -> Bool) -> [String] -> Int
amountOfValid isValid = length . filter (isValid . words)
    
hasNoDuplicates :: [String] -> Bool 
hasNoDuplicates [] = True
hasNoDuplicates (x:xs) = x `notElem` xs && hasNoDuplicates xs

hasNoAnagrams :: [String] -> Bool 
hasNoAnagrams [] = True
hasNoAnagrams (x:xs) = (not $ any (isAnagram x) xs) && hasNoAnagrams xs

isAnagram :: String -> String -> Bool
isAnagram a b = sort a == sort b
