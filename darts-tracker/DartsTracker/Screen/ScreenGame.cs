using System;
using DartsTracker.Core;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace DartsTracker.Screen;

public class ScreenGame : IScreen {
  private SpriteFont Font { get; set; }

  private Board Board { get; set; }
  private Texture2D BoardBackground { get; set; }
  private Viewport BoardViewport { get; set; }
  private Rectangle BoardDestinationRectangle { get; set; }

  private Texture2D Turn { get; set; }
  private Texture2D TurnBackground { get; set; }
  private Viewport TurnViewport { get; set; }
  private Rectangle TurnDestinationRectangle { get; set; }

  private string HoveredTile { get; set; }
  private Vector2 HoveredTilePosition { get; set; }

  public void LoadContent(
    ContentManager content,
    GraphicsDevice graphicsDevice
  ) {
    // load font
    this.Font = content.Load<SpriteFont>("Fonts/Consolas");

    // load board
    this.Board = new(
      texture: content.Load<Texture2D>("Textures/Board"),
      tileDelimiter: Color.White
    );
    this.BoardBackground = new(graphicsDevice, width: 1, height: 1);
    this.BoardBackground.SetData([new Color(0, 0, 0)]);

    // load turn
    this.Turn = content.Load<Texture2D>("Textures/Turn");
    this.TurnBackground = new(graphicsDevice, width: 1, height: 1);
    this.TurnBackground.SetData([new Color(24, 24, 24)]);
  }

  public void UnloadContent() {
    this.Board = null;
    this.Font = null;
    this.Turn = null;
  }

  public void Update(Viewport viewport, GameTime gameTime) {
    // update board
    this.BoardViewport = new(
      x: viewport.X,
      y: viewport.Y,
      width: viewport.Width / 5 * 3,
      height: viewport.Height
    );
    int boardMargin = 16;
    float boardScale = Math.Min(
      (this.BoardViewport.Width - boardMargin) / (float)this.Board.Texture.Width,
      (this.BoardViewport.Height - boardMargin) / (float)this.Board.Texture.Height
    );
    this.BoardDestinationRectangle = new(
      x: viewport.X + (int)(this.BoardViewport.Width / 2 - this.Board.Texture.Width * boardScale / 2),
      y: viewport.Y + (int)(this.BoardViewport.Height / 2 - this.Board.Texture.Height * boardScale / 2),
      width: (int)(this.Board.Texture.Width * boardScale),
      height: (int)(this.Board.Texture.Height * boardScale)
    );

    // update turn
    this.TurnViewport = new(
      x: viewport.X + this.BoardViewport.Width,
      y: viewport.Y,
      width: viewport.Width - this.BoardViewport.Width,
      height: viewport.Height
    );
    int turnMargin = 64;
    float turnScale = Math.Min(
      (this.TurnViewport.Width - turnMargin) / (float)this.Turn.Width,
      (this.TurnViewport.Height - turnMargin) / (float)this.Turn.Height
    );
    this.TurnDestinationRectangle = new(
      x: TurnViewport.X + (int)(this.TurnViewport.Width / 2 - this.Turn.Width * turnScale / 2),
      y: TurnViewport.Y + turnMargin / 2,
      width: (int)(this.Turn.Width * turnScale),
      height: (int)(this.Turn.Height * turnScale)
    );

    // update hovered tile
    MouseState mouseState = Mouse.GetState();
    Vector2 mousePosition = new(
      x: (int)((mouseState.X - this.BoardDestinationRectangle.X) / boardScale),
      y: (int)((mouseState.Y - this.BoardDestinationRectangle.Y) / boardScale)
    );
    this.HoveredTile = this.Board.TileAt(mousePosition);
    Vector2 textBoxPosition = new(0 * turnScale, 816 * turnScale);
    Vector2 textBoxDimensions = new(320 * turnScale, 96 * turnScale);
    Vector2 textDimensions = this.Font.MeasureString(this.HoveredTile);
    this.HoveredTilePosition = new(
      this.TurnDestinationRectangle.X + textBoxPosition.X + textBoxDimensions.X / 2 - textDimensions.X / 2,
      this.TurnDestinationRectangle.Y + textBoxPosition.Y + textBoxDimensions.Y / 2 - textDimensions.Y / 2
    );
  }

  public void Draw(SpriteBatch spriteBatch, GameTime gameTime) {
    // draw board
    spriteBatch.Draw(
      texture: this.BoardBackground,
      destinationRectangle: this.BoardViewport.Bounds,
      color: Color.White
    );
    spriteBatch.Draw(
      texture: this.Board.Texture,
      destinationRectangle: this.BoardDestinationRectangle,
      color: Color.White
    );

    // draw turn
    spriteBatch.Draw(
      texture: this.TurnBackground,
      destinationRectangle: this.TurnViewport.Bounds,
      color: Color.White
    );
    spriteBatch.Draw(
      texture: this.Turn,
      destinationRectangle: this.TurnDestinationRectangle,
      color: Color.White
    );

    // draw hovered tile
    spriteBatch.DrawString(
      spriteFont: this.Font,
      text: this.HoveredTile,
      position: this.HoveredTilePosition,
      color: Color.Black
    );
  }
}
