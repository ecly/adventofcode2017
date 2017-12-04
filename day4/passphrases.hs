main :: IO()
main = do 
    input <- getContents 
    let phrases = lines input
    putStrLn $ show $ amountOfValid phrases 0

amountOfValid :: [String] -> Int -> Int
amountOfValid [] count = count
amountOfValid (x:xs) count = 
    if isValidPassphrase $ words x
       then amountOfValid xs count+1
       else amountOfValid xs count
    
isValidPassphrase :: [String] -> Bool 
isValidPassphrase [] = True
isValidPassphrase (x:xs) = x `notElem` xs && isValidPassphrase xs
