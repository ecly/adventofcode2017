import Data.List
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
    let instructions = lines input
    let registers = Map.fromList $ zip (map (head . words) instructions) (repeat 0)
    putStrLn $ show $ map parse instructions
        -- putStrLn $ show $ maximum $ (Map.mapKeys . apply) registers

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

apply :: Map k a -> [Instruction] -> Map k a
apply m [] = m
apply m (x:xs) = m
