# Approach

Personally, I believe the steps to create a theme are as follows:

1.  **Decide on the Concept**: What is this theme trying to achieve? What is it trying to describe? In this project, it's always a character.
2.  **Decide on Sampling Colors**: What are the most prominent colors of the character?
3.  **Decide on Base and Text**: A theme must have a background and a foreground.
4.  **Decide on Semantic Colors**: Besides the main text, what colors should be used for emphasis?
5.  **Fine-tune according to Gradients**: For UI elements, the backgrounds should have different levels, and the difference in brightness creates the gradient. Since the gradient is fixed, there's not much need for fine-tuning after deciding on it.
6.  **Fine-tune Semantic Colors**: Adjust the brightness of semantic colors until they meet readability standards.
7.  **Write Documentation**: "Tell a story," and then assign meaning to the semantic colors and gradient changes.

## Concept

In this project, each core concept corresponds to a specific anime character.

## Sampling

Once the concept is formed, you can start sampling.
You can sample directly from the original artwork by picking points, or you can use statistical sampling.
Statistical sampling requires using the median / K-means clustering to avoid picking extreme highlights or dark spots.

The sampled content includes Base, Text, and semantic colors. Semantic colors can be picked later.

Another thing to note about sampling is the color space.
The simplest is to use HSL.
However, all the LLMs I've used say OKLCH is better.

- This project uses K-means as actively used by chatGPT o3, but sometimes this sampling is not satisfactory.

## Basic Colors

Also known as base & text, background and foreground, `bg` and `fg`.

Any effective color theme must include a base background color (Base) and a text color (Text).
To ensure readability over long periods of use, they must meet specific contrast standards.

- The standard used in this project is [WCAG 2.1 | Level AA](https://www.w3.org/TR/WCAG21/#contrast-minimum), which requires a contrast ratio of at least `4.5:1` between the background and text colors.

## Gradients

For different UI elements, such as panels, buttons, and hover states, it's impossible for them to be the same color as the background.
So, you need to vary the background color appropriately.
A simple practice is to adjust the brightness.

- The gradient hierarchy in this project is designed with reference to the way the Catppuccin theme handles brightness (ΔL).

## Semantic Colors

Semantic colors are accent colors used for specific purposes, such as syntax highlighting in code, links, warnings, or success states. Mature color themes usually include a complete set of semantic colors.

- **Dracula**:
  - Basic colors: background, current line, foreground, comment
  - Semantic colors: cyan, green, orange, pink, purple, red, yellow
- **Catppuccin**:
  - Basic colors: Text, Subtext1, Subtext0, Overlay2, Overlay1, Overlay0, Surface2, Surface1, Surface0, Base, Mantle, Crust
  - Semantic colors: Rosewater, Flamingo, Pink, Mauve, Red, Maroon, Peach, Yellow, Green, Teal, Sky, Sapphire, Blue, Lavender

You may notice that some colors (the main ones) are close to monochromatic (mono) and very similar.

Of course, the semantic colors here don't mean you have to sample seven or eight colors, because anime characters usually don't use too many colors in order to create a memorable impression.
The process in this project is as follows:

1.  First, determine one or two core accent colors from the sampled colors.
2.  After sampling two or three, you can use tools to help generate other semantic colors. The principles used include, but are not limited to, fine-tuning within the same color family, complementary colors, analogous colors, etc.
3.  Use the Catppuccin framework to assist in generating colors.

For color frameworks, users who prefer minimalism can also use Dracula. For theme mechanism enthusiasts, you can also use the Base16 naming scheme.

Tools to assist in generation include, but are not limited to:

-   LLMs that can **execute programs**.
-   <https://color.adobe.com>: Can only generate by locking a single base color.
-   <https://coolors.co>: Can lock multiple colors, but it requires a paid subscription and is expensive.

## a11y

After creating the semantic colors, you can adjust their brightness to ensure that their combination with the background color meets readability requirements.

- This project requires that the contrast between semantic colors and the base background color is not less than 3:1.

## Confirmation

Now you have the basic and semantic colors. You just need to run a contrast-matrix with some tool.

After running it, you can take screenshots for display and then write the documentation.
When writing the documentation, you need to explain what each color is used for.

Of course, if it's designed based on a framework (like Dracula), then the colors speak for themselves.

- This project uses chatGPT o3 to design based on a framework, so this step is not necessary.
