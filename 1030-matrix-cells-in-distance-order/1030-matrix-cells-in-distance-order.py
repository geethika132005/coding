class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, r0: int, c0: int) -> List[List[int]]:
        cells = []
        for r in range(rows):
            for c in range(cols):
                cells.append([r, c])

        cells.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return cells

        