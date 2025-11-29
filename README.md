# ABC Template Datapack

A Minecraft datapack template compatible with versions 1.16-1.21.

## Installation

1. Download or clone this repository
2. Copy the entire folder to your world's `datapacks` folder:
   - Location: `.minecraft/saves/[Your World Name]/datapacks/`
3. In-game, run `/reload` or restart the world
4. You should see a confirmation message when the datapack loads

## Usage

This template includes basic examples to get you started:

### Example Commands

- `/function abc:example` - Gives the player a diamond (example function)

### Structure

```
abc-template/
├── pack.mcmeta                           # Datapack metadata
├── data/
│   ├── abc/                              # Main namespace
│   │   └── functions/
│   │       ├── load.mcfunction           # Runs on datapack load/reload
│   │       ├── tick.mcfunction           # Runs every game tick
│   │       └── example.mcfunction        # Example custom function
│   └── minecraft/
│       └── tags/
│           └── functions/
│               ├── load.json             # Load function tag
│               └── tick.json             # Tick function tag
```

## Version Compatibility

- **Pack Format**: 10
- **Minecraft Versions**: 1.16 - 1.21
- Tested and working across all versions in this range

## Customization

1. Add your custom functions in `data/abc/functions/`
2. Modify `load.mcfunction` to run setup commands when the datapack loads
3. Modify `tick.mcfunction` to add repeating logic (runs 20 times per second)
4. Create additional namespaces by adding folders under `data/`

## Contributing

Feel free to use this template as a starting point for your own Minecraft datapacks!

## License

See LICENSE file for details.