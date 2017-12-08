import Data.Map (Map)
import qualified Data.Map as Map

type Key = String
data Unary = Inc | Dec deriving (Show)
data Operator = Eq | Ne | Gt | Lt | Ge | Le deriving (Show)
data Instruction = Instruction { key :: Key 
                               , unary :: Unary
                               , unaryVal :: Integer
                               , predicateKey :: Key
                               , operator :: Operator
                               , predicateVal :: Integer } deriving (Show)

main :: IO()
main = do 
    input <- getContents 
    let instrLines = lines input
    let registers = Map.fromList $ zip (map (head . words) instrLines) (repeat 0)
    let instructions = map parse instrLines
    putStrLn $ show $ maximum $ Map.elems $ apply registers instructions

parseUnary :: String -> Unary
parseUnary "dec" = Dec
parseUnary _ = Inc

parseOperator :: String -> Operator
parseOperator "==" = Eq
parseOperator "!=" = Ne
parseOperator ">" = Gt
parseOperator "<" = Lt
parseOperator ">=" = Ge
parseOperator _ = Le

parse :: String -> Instruction
parse s = let parsed = words s
              k = parsed!!0
              u = parseUnary $ parsed!!1
              v = read $ parsed!!2
              pk = parsed!!4
              o = parseOperator $ parsed!!5
              pv = read $ parsed!!6
          in Instruction k u v pk o pv

predicate :: Map Key Integer -> Instruction -> Bool
predicate m i =
    let actualVal = Map.findWithDefault 0 (predicateKey i) m
    in case operator i of
         Eq -> actualVal == (predicateVal i)
         Ne -> actualVal /= (predicateVal i)
         Gt -> actualVal >  (predicateVal i)
         Lt -> actualVal <  (predicateVal i)
         Ge -> actualVal >= (predicateVal i)
         Le -> actualVal <= (predicateVal i)

updateFunc :: Instruction -> Integer -> Integer
updateFunc i = case unary i of
                 Inc -> (+) $ unaryVal i
                 Dec -> (+) $ -1 * unaryVal i

apply :: Map Key Integer -> [Instruction] -> Map Key Integer
apply m [] = m
apply m (x:xs) 
  | predicate m x = apply (Map.adjust (updateFunc x) (key x) m) xs
  | otherwise     = apply m xs
