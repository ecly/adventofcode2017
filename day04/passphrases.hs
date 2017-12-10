import Data.List

main :: IO()
main = do 
    input <- getContents 
    let phrases = lines input
    putStrLn $ show $ amountOfValid hasNoDuplicates phrases 0
    putStrLn $ show $ amountOfValid hasNoAnagrams phrases 0

amountOfValid :: ([String] -> Bool) -> [String] -> Int -> Int
amountOfValid _ [] count = count
amountOfValid isValid (x:xs) count = 
    if isValid $ words x
       then amountOfValid isValid xs count+1
       else amountOfValid isValid xs count
    
hasNoDuplicates :: [String] -> Bool 
hasNoDuplicates [] = True
hasNoDuplicates (x:xs) = x `notElem` xs && hasNoDuplicates xs

hasNoAnagrams :: [String] -> Bool 
hasNoAnagrams [] = True
hasNoAnagrams (x:xs) = (not $ any (isAnagram x) xs) && hasNoAnagrams xs

isAnagram :: String -> String -> Bool
isAnagram a b = sort a == sort b
