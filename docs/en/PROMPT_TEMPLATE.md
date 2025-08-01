## Instruction

From a cost-performance perspective, I chose to try using an LLM (the LLM here **must be able to execute programs**) for generation. This requires Prompt Engineering.

I referred to Google's [Prompting guide 101](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf). It points out that a good prompt can be composed of the following elements:

-   Persona
-   Task
-   Context
-   Format

It should be noted that for work involving an LLM, the results are generally not reproducible. In theory, there is a seed, but in practice, it is meaningless.

---

```md
You are a professional UI designer, especially skilled at creating themes for developer tools that have an emotional connection and visual consistency.

I want you to create a Light Mode color palette for a code editor based on the core color scheme of an anime character. This palette must strictly follow the naming structure specified below.

### 1. Character and Style Analysis

-   Character Name: 凯尔希 (Kal'tsit)
-   Source: Arknights
-   Core Personality and Temperament: Kal'tsit, one of the high-level managers of Rhodes Island, and the leader of the Rhodes Island medical project. She has profound knowledge in fields such as metallurgy, sociology, Originium arts, archaeology, historical genealogy, economics, botany, and geology. In some of Rhodes Island's operations, she provides medical theoretical assistance and emergency medical equipment as a medical staff member, and is also an important member of Rhodes Island's strategic command system, active in various projects.

-   Desired Palette Feel: It should be a theme with a greenish-white background, complemented by the semantic colors of her clothing. The character is generally calm.
-   File Structure: kaltsit.png is her character art.

### 2. Core Color Benchmarks

-   Main Base Tone (for background): Observe kaltsit.png. Her hair is clearly a white with a green tint. Extract this white to use as the base.
-   Core Text Color (for text): For the text color, it should be a composite color of the black from her equipment, to be used as text.
-   First Accent Color (most iconic color): Her clothes are green.
-   Second Accent Color (secondary feature): Her ears are yellow.

### 3. Design Task and Color Theory Requirements

Please fill in the following palette structure based on the **core color benchmarks** above.
-   Inference Principle: You need to use professional color theory knowledge (such as adjusting saturation, brightness, finding adjacent colors, complementary colors) to generate the remaining colors based on the core colors. When all colors are combined, they must feel like they originate from the same character.
-   Style Instructions:
    -   UI Series (Base, Mantle, Crust, Surface 0, Surface 1, Surface 2, Overlay 0, Overlay 1, Overlay 2): Fine-tune based on the **main base tone (base)** to ensure comfort for long-term reading. For Surface and Overlay, the larger the number, the darker it is. For specific gradients, refer to #4. Catppuccin Gradient Example.
    -   Text Series (Text, Subtext 0, Subtext 1): Create different brightness versions based on the **core text color (text)** to ensure clear readability. For Subtext, the larger the number, the darker it is. For specific gradients, refer to #4. Catppuccin Gradient Example.
    -   Semantic Series: Must reflect the user-described **core personality and temperament**. They need to be more vivid than the base colors, but not too harsh.
        -   Green series includes: Green. Her clothes are obviously green. You can extract and analyze it from kaltsit.png, and you can change it for long-term readability.
        -   Yellow series includes: Yellow, Peach. You need to look at the character art to find the Yellow on her ears. You can darken this yellow for long-term readability. Peach can be generated using professional color theory knowledge.
        -   Blue series includes: Blue, Sapphire, Sky, Teal, Lavender. These need to be changed and generated through professional color theory knowledge. You can refer to Catppuccin - Latte, but do not copy it.
        -   Red series includes: Red, Maroon, Flamingo, Rosewater. These need to be changed and generated through professional color theory knowledge. You can refer to Catppuccin - Latte, but do not copy it.
        -   The remaining Mauve, Lavender, Pink need to be changed and generated using professional color theory knowledge. You can refer to Catppuccin - Latte, but do not copy it.

### 4. Extract Colors

You must first use an image analysis tool to **extract the core color values** from the provided image. You must not generate colors based on impressions or descriptions alone. You must use Python tools or other methods to extract colors from the specified parts.

You need to use the following image file:
-   `kaltsit.png`

### 5. Catppuccin Gradient Example

The table below shows the precise gradients of *Base ⇢ Surface/Overlay/Mantle/Crust* and *Text ⇢ Subtext* in the Latte flavor.
Please "reuse the same relative increments" when generating the new palette, but start with this character's Base / Text.

| Labels     | Hex       | RGB                | HSL                |
|------------|-----------|--------------------|--------------------|
| Text       | `#4c4f69` | `rgb(76, 79, 105)`   | `hsl(234, 16%, 35%)`|
| Subtext1   | `#5c5f77` | `rgb(92, 95, 119)`   | `hsl(233, 13%, 41%)`|
| Subtext0   | `#6c6f85` | `rgb(108, 111, 133)` | `hsl(233, 10%, 47%)`|
| Overlay2   | `#7c7f93` | `rgb(124, 127, 147)` | `hsl(232, 10%, 53%)`|
| Overlay1   | `#8c8fa1` | `rgb(140, 143, 161)` | `hsl(231, 10%, 59%)`|
| Overlay0   | `#9ca0b0` | `rgb(156, 160, 176)` | `hsl(228, 11%, 65%)`|
| Surface2   | `#acb0be` | `rgb(172, 176, 190)` | `hsl(227, 12%, 71%)`|
| Surface1   | `#bcc0cc` | `rgb(188, 192, 204)` | `hsl(225, 14%, 77%)`|
| Surface0   | `#ccd0da` | `rgb(204, 208, 218)` | `hsl(223, 16%, 83%)`|
| Base       | `#eff1f5` | `rgb(239, 241, 245)` | `hsl(220, 23%, 95%)`|
| Mantle     | `#e6e9ef` | `rgb(230, 233, 239)` | `hsl(220, 22%, 92%)`|
| Crust      | `#dce0e8` | `rgb(220, 224, 232)` | `hsl(220, 21%, 89%)`|

If you don't follow the gradients, some UI text will be difficult to read.

### 6. Output Format

Please return the final palette in JSON format:
-   The top level is an object with keys for color categories, in the order of Semantic, Text, UI.
-   The value of each category is an array of color objects.
-   Each color object contains three fields: Name, Hex, and Rationale.
    -   Name: e.g., Rosewater, Base, etc.
    -   Hex
    -   Rationale: Briefly explain the inspiration or derivation logic for this color (e.g., "Inspired by the color of a gold button, brightness increased to reflect a lively feel").
-   Order: Rosewater, Flamingo, Pink, Mauve, Red, Maroon, Peach, Yellow, Green, Teal, Sky, Sapphire, Blue, Lavender, Text, Subtext0, Subtext1, Base, Mantle, Crust, Surface0, Surface1, Surface2, Overlay0, Overlay1, Overlay2.

Example:

```json
{
  "Semantic": [
    {
      "Name": "Rosewater",
      "Hex": "#F9E2AF",
      "Rationale": "Echoing the halo"
    },
		{
      "Name": "Flamingo",
			// ...
		},
    // ... all other semantic colors here
  ],
  "Text": [
    {
      "Name": "Text",
      "Hex": "#F4F9E3",
      "Rationale": "Sampled highlight white"
    },
		{
      "Name": "Subtext0",
			// ...
		},
		// ... all other text colors here
  ],
  "UI": [
    {
      "Name": "Base",
      "Hex": "#292A3C",
      "Rationale": "Uniform dark blue"
    },
		{
      "Name": "Mantle",
			// ...
		},
  // ... all other UI colors here
  ]
}
```
