import chess
from stockfish import Stockfish
import json
import configparser
import time


config = configparser.ConfigParser()
config.read("../config.ini")
stockfish_path = config["STOCKFISH"]["path"]
stockfish_threads = config["STOCKFISH"]["threads"]
stockfish_min_thinking_time = config["STOCKFISH"]["min_thinking_time"]
stockfish = Stockfish(stockfish_path, depth=11, parameters={
    "Threads": stockfish_threads, "Minimum Thinking Time": stockfish_min_thinking_time
})

def analyze_all_chess_move(moves):
    try:
        start = time.time()
   

        data = []
        board = chess.Board()
        for i in range(len(moves)):
            data.append(moves[i]["whiteMove"])
            data.append(moves[i]["blackMove"])

        fens = []
        for i in range(len(data)):
            board.push_san(data[i])
            fens.append(board.fen())

        result = []
        for i in range(len(fens)):
            stockfish.set_fen_position(fens[i])
            best_move = stockfish.get_best_move()
            analysis = stockfish.get_evaluation()
            result.append({"best_move": best_move, "analysis": analysis})
        
        end = time.time()


        return  {"result": result, "time": end - start}

    except Exception as e:
        return {"error": str(e)}


def analyze_chess_move(move):
    # show the next best move
    try:
        start = time.time()      

        stockfish.set_fen_position(move[0]["fen"])
        best_move = stockfish.get_best_move()
        analysis = stockfish.get_evaluation()

        # get the fen from the best move
        board = chess.Board(move[0]["fen"])
        board.push_san(best_move)
        fen = board.fen()

        end = time.time()

        return {"best_move": best_move, "analysis": analysis, "fen": fen, "time": end - start}
    
    except Exception as e:
        print (e)
        return {"error": str(e)}


if __name__ == "__main__":
    try:
        with open("../data/dummy.json", "r") as f:
            data = json.load(f)

        print(analyze_all_chess_move(data))

    except Exception as e:
        print(e)
