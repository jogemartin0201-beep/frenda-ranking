import { Jimp } from 'jimp';
console.log("Jimp properties:", Object.keys(Jimp));
const img = await Jimp.read({ width: 1, height: 1, color: 0xffffffff });
console.log("New img created with Jimp.read options");
