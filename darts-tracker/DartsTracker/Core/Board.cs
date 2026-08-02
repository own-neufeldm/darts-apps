using System;
using System.Collections.Generic;
using System.IO;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Newtonsoft.Json;

namespace DartsTracker.Core;

public class Board {
  public Texture2D Texture { get; }
  private Color[] TextureData { get; }
  private Color TileDelimiter { get; }
  private Dictionary<string, List<Vector2>> Tiles { get; }

  public Board(Texture2D texture, Color tileDelimiter) {
    this.Texture = texture;
    this.TextureData = new Color[this.Texture.Width * this.Texture.Height];
    this.Texture.GetData(this.TextureData);
    this.TileDelimiter = tileDelimiter;
    this.Tiles = [];
    this.LoadTiles(Path.Combine(Environment.CurrentDirectory, "tiles.json"));
  }

  public string TileAt(Vector2 point) {
    foreach (KeyValuePair<string, List<Vector2>> pair in this.Tiles)
      if (pair.Value.Contains(point))
        return pair.Key;
    return "n/a";
  }

  private void LoadTiles(string path) {
    try {
      this.LoadTilesFromFile(path);
    } catch (FileNotFoundException) {
      this.LoadTilesFromTexture();
      this.SaveTilesToFile(path);
    }
  }

  private void LoadTilesFromFile(string path) {
    string contents = File.ReadAllText(path);
    Dictionary<string, List<Vector2>> tiles = JsonConvert.DeserializeObject<Dictionary<string, List<Vector2>>>(contents);
    foreach (KeyValuePair<string, List<Vector2>> tile in tiles)
      this.Tiles.Add(tile.Key, tile.Value);
  }

  private void LoadTilesFromTexture() {
    // miss
    this.Tiles.Add("0", this.LoadTile([new(210, 6)]));

    // bullseye
    this.Tiles.Add("25", this.LoadTile([new(221, 209)]));
    this.Tiles.Add("D25", this.LoadTile([new(222, 217)]));

    // twenty
    this.Tiles.Add("20", this.LoadTile([new(200, 67), new(210, 130)]));
    this.Tiles.Add("D20", this.LoadTile([new(199, 59)]));
    this.Tiles.Add("T20", this.LoadTile([new(209, 122)]));

    // one
    this.Tiles.Add("1", this.LoadTile([new(249, 67), new(239, 130)]));
    this.Tiles.Add("D1", this.LoadTile([new(250, 59)]));
    this.Tiles.Add("T1", this.LoadTile([new(240, 122)]));

    // eighteen
    this.Tiles.Add("18", this.LoadTile([new(296, 83), new(267, 140)]));
    this.Tiles.Add("D18", this.LoadTile([new(299, 76)]));
    this.Tiles.Add("T18", this.LoadTile([new(271, 133)]));

    // four
    this.Tiles.Add("4", this.LoadTile([new(336, 112), new(291, 157)]));
    this.Tiles.Add("D4", this.LoadTile([new(342, 106)]));
    this.Tiles.Add("T4", this.LoadTile([new(296, 152)]));

    // thirteen
    this.Tiles.Add("13", this.LoadTile([new(365, 153), new(308, 182)]));
    this.Tiles.Add("D13", this.LoadTile([new(372, 149)]));
    this.Tiles.Add("T13", this.LoadTile([new(315, 178)]));

    // six
    this.Tiles.Add("6", this.LoadTile([new(380, 200), new(317, 210)]));
    this.Tiles.Add("D6", this.LoadTile([new(388, 199)]));
    this.Tiles.Add("T6", this.LoadTile([new(325, 209)]));

    // ten
    this.Tiles.Add("10", this.LoadTile([new(380, 249), new(317, 239)]));
    this.Tiles.Add("D10", this.LoadTile([new(388, 250)]));
    this.Tiles.Add("T10", this.LoadTile([new(325, 240)]));

    // fifteen
    this.Tiles.Add("15", this.LoadTile([new(364, 296), new(307, 268)]));
    this.Tiles.Add("D15", this.LoadTile([new(371, 299)]));
    this.Tiles.Add("T15", this.LoadTile([new(314, 271)]));

    // two
    this.Tiles.Add("2", this.LoadTile([new(335, 336), new(290, 291)]));
    this.Tiles.Add("D2", this.LoadTile([new(341, 342)]));
    this.Tiles.Add("T2", this.LoadTile([new(295, 297)]));

    // seventeen
    this.Tiles.Add("17", this.LoadTile([new(294, 365), new(265, 308)]));
    this.Tiles.Add("D17", this.LoadTile([new(298, 372)]));
    this.Tiles.Add("T17", this.LoadTile([new(269, 315)]));

    // three
    this.Tiles.Add("3", this.LoadTile([new(247, 380), new(237, 317)]));
    this.Tiles.Add("D3", this.LoadTile([new(248, 388)]));
    this.Tiles.Add("T3", this.LoadTile([new(238, 325)]));

    // nineteen
    this.Tiles.Add("19", this.LoadTile([new(198, 380), new(208, 317)]));
    this.Tiles.Add("D19", this.LoadTile([new(197, 388)]));
    this.Tiles.Add("T19", this.LoadTile([new(207, 325)]));

    // seven
    this.Tiles.Add("7", this.LoadTile([new(151, 364), new(180, 307)]));
    this.Tiles.Add("D7", this.LoadTile([new(148, 371)]));
    this.Tiles.Add("T7", this.LoadTile([new(176, 314)]));

    // sixteen
    this.Tiles.Add("16", this.LoadTile([new(111, 335), new(156, 290)]));
    this.Tiles.Add("D16", this.LoadTile([new(105, 341)]));
    this.Tiles.Add("T16", this.LoadTile([new(151, 295)]));

    // eight
    this.Tiles.Add("8", this.LoadTile([new(82, 294), new(139, 265)]));
    this.Tiles.Add("D8", this.LoadTile([new(75, 298)]));
    this.Tiles.Add("T8", this.LoadTile([new(132, 269)]));

    // eleven
    this.Tiles.Add("11", this.LoadTile([new(67, 247), new(130, 237)]));
    this.Tiles.Add("D11", this.LoadTile([new(59, 248)]));
    this.Tiles.Add("T11", this.LoadTile([new(122, 238)]));

    // fourteen
    this.Tiles.Add("14", this.LoadTile([new(67, 198), new(130, 208)]));
    this.Tiles.Add("D14", this.LoadTile([new(59, 197)]));
    this.Tiles.Add("T14", this.LoadTile([new(122, 207)]));

    // nine
    this.Tiles.Add("9", this.LoadTile([new(83, 151), new(140, 180)]));
    this.Tiles.Add("D9", this.LoadTile([new(76, 148)]));
    this.Tiles.Add("T9", this.LoadTile([new(133, 176)]));

    // twelve
    this.Tiles.Add("12", this.LoadTile([new(112, 111), new(157, 156)]));
    this.Tiles.Add("D12", this.LoadTile([new(106, 105)]));
    this.Tiles.Add("T12", this.LoadTile([new(152, 151)]));

    // five
    this.Tiles.Add("5", this.LoadTile([new(153, 82), new(182, 139)]));
    this.Tiles.Add("D5", this.LoadTile([new(149, 75)]));
    this.Tiles.Add("T5", this.LoadTile([new(178, 132)]));
  }

  private List<Vector2> LoadTile(List<Vector2> startingPoints) {
    List<Vector2> output = [];

    foreach (Vector2 startingPoint in startingPoints) {
      List<Vector2> range = Utils.FloodFill(
        data: this.TextureData,
        delimiter: this.TileDelimiter,
        startingPoint: startingPoint,
        dimensions: new(this.Texture.Width, this.Texture.Width)
      );
      output.AddRange(range);
    }

    return output;
  }

  private void SaveTilesToFile(string path) {
    string contents = JsonConvert.SerializeObject(this.Tiles);
    File.WriteAllText(path, contents);
  }
}
