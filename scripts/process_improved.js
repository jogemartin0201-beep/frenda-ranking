import { Jimp } from 'jimp';
import path from 'path';
import fs from 'fs';

const SRC_DIR = "/Users/ryotaasai/Desktop/ポケモンフレンダ/写真";
const DEST_DIR = "/Users/ryotaasai/frenda-ranking/public/images";

async function processImage(srcFile, targetId) {
    const srcPath = path.join(SRC_DIR, srcFile);
    if (!fs.existsSync(srcPath)) return;

    try {
        const image = await Jimp.read(srcPath);

        // 1. Front Card Crop (Mutates image)
        const front = image.clone().crop({ x: 185, y: 230, w: 800, h: 520 });

        // 2. Back Card Crop
        const back = image.clone().crop({ x: 350, y: 1080, w: 470, h: 770 });

        // 3. Create White Canvas
        const canvas = await Jimp.create({ width: 800, height: 1350, color: 0xFFFFFFFF });

        // 4. Composite
        canvas.composite(front, 0, 0);
        canvas.composite(back, (800 - 470) / 2, 550);

        await canvas.write(path.join(DEST_DIR, `${targetId}.png`));
        console.log(`Processed ${srcFile} -> ${targetId}.png`);
    } catch (err) {
        console.error(`Error processing ${srcFile}:`, err);
    }
}

// Test with Zygarde (112)
processImage("IMG_5180.PNG", "112");
