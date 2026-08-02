using System;
using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.Graphics;

namespace DartsTracker.Screen;

public class ScreenManager : IDisposable {
  private SpriteBatch SpriteBatch { get; set; }
  private List<IScreen> Screens { get; }
  private IScreen CurrentScreen { get; set; }

  public ScreenManager() {
    this.Screens = [new ScreenGame()];
    this.CurrentScreen = this.Screens[0];
  }

  public void LoadContent(
    ContentManager content,
    GraphicsDevice graphicsDevice
  ) {
    this.SpriteBatch = new(graphicsDevice);
    this.CurrentScreen.LoadContent(content, graphicsDevice);
  }

  public void UnloadContent() {
    foreach (IScreen screen in this.Screens)
      screen.UnloadContent();
  }

  public void Update(Viewport viewport, GameTime gameTime) {
    this.CurrentScreen.Update(viewport, gameTime);
  }

  public void Draw(GraphicsDevice graphicsDevice, GameTime gameTime) {
    graphicsDevice.Clear(Color.Black);
    this.SpriteBatch.Begin(samplerState: SamplerState.PointClamp);
    this.CurrentScreen.Draw(this.SpriteBatch, gameTime);
    this.SpriteBatch.End();
  }

  void IDisposable.Dispose() {
    this.UnloadContent();
    GC.SuppressFinalize(this);
  }
}
