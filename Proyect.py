class NumberLinkSolver:
    def __init__(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                self.rows, self.cols = map(int, lines[0].strip().split(","))

                # Inicializa el tablero con celdas vacías
                self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]

                # Procesa las ubicaciones de las parejas
                for line in lines[1:]:
                    pair_data = list(map(int, line.strip().split(",")))
                    row, col, value = pair_data
                    self.board[row - 1][col - 1] = str(value)

        except Exception as e:
            print(f"Error al leer el archivo de entrada: {e}")
            self.rows = 0
            self.cols = 0
            self.board = None

    def print_board(self):
        horizontal_line = "+---" * self.cols + "+"

        for i in range(self.rows):
            print(horizontal_line)
            for j in range(self.cols):
                print(f"| {self.board[i][j]} ", end="")
            print("|")
        print(horizontal_line)

    def play(self):
        while True:
            self.print_board()
            try:
                row1, col1, row2, col2 = map(
                    int,
                    input(
                        "Ingresa las coordenadas (fila1, columna1, fila2, columna2) o 'q' para salir: "
                    )
                    .strip()
                    .split(),
                )
                if row1 == row2 and col1 == col2:
                    print("Las coordenadas deben ser diferentes.")
                    continue
                if self.is_valid_move(row1, col1, row2, col2):
                    self.connect_cells(row1, col1, row2, col2)
                    if self.is_game_over():
                        print("¡Has ganado! ¡Todas las celdas están conectadas!")
                        break
                else:
                    print(
                        "Movimiento inválido. Asegúrate de que las celdas sean adyacentes y estén vacías."
                    )
            except ValueError:
                if input("¿Deseas salir del juego? (S/N): ").strip().lower() == "s":
                    break
                else:
                    continue

    def is_valid_move(self, row1, col1, row2, col2):
        # Verifica si el movimiento es válido (celdas adyacentes y vacías)
        pass

    def connect_cells(self, row1, col1, row2, col2):
        # Conecta las celdas en el tablero
        pass

    def is_game_over(self):
        # Verifica si se ha completado el juego
        pass


if __name__ == "__main__":
    input_file = "inputfile.txt"
    solver = NumberLinkSolver(input_file)
    if solver.rows > 0 and solver.cols > 0 and solver.board is not None:
        print("Tablero de entrada:")
        solver.play()
    else:
        print("No se pudo cargar el tablero inicial. Verifica el archivo de entrada.")
