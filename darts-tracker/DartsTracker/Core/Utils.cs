using System.Collections.Generic;
using Microsoft.Xna.Framework;

namespace DartsTracker.Core;

public static class Utils {
  // https://lodev.org/cgtutor/floodfill.html#4-Way_Method_With_Stack
  public static List<Vector2> FloodFill(
    Color[] data,
    Color delimiter,
    Vector2 startingPoint,
    Vector2 dimensions
  ) {
    List<Vector2> output = [];
    int[] dx = [-1, 1, 0, 0];
    int[] dy = [0, 0, -1, 1];

    Stack<Vector2> stack = new([startingPoint]);
    while (stack.Count > 0) {
      Vector2 point = stack.Pop();
      output.Add(point);

      for (int i = 0; i < 4; i++) {
        Vector2 newPoint = new(point.X + dx[i], point.Y + dy[i]);
        if (Utils.IsValidPoint(output, data, delimiter, newPoint, dimensions))
          stack.Push(newPoint);
      }
    }

    return output;
  }

  private static bool IsValidPoint(
    List<Vector2> output,
    Color[] data,
    Color delimiter,
    Vector2 point,
    Vector2 dimensions
  ) {
    int x = (int)point.X;
    int y = (int)point.Y;
    int w = (int)dimensions.X;
    int h = (int)dimensions.Y;

    // already known
    if (output.Contains(point))
      return false;

    // out of bounds
    if (x < 0 || x >= w || y < 0 || y >= h)
      return false;

    // is border
    if (data[x + y * h].Equals(delimiter))
      return false;

    return true;
  }
}
