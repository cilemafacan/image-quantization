import gradio as gr
import numpy as np
from PIL import Image


def quantize(image, original_bits, target_bits):
    """
    Kuantalama işlemi.
    Formül:  floor((Vi * (V'max - V'min) / (Vmax - Vmin)))
    image: PIL.Image.Image
    bits: int
    """
    np_image = np.array(image)
    Vnew_max = (2 ** target_bits)
    Vnew_min = 0
    Vmax = (2 ** original_bits)
    Vmin = 0
    quantized_image = np.floor((np_image * ((Vnew_max - Vnew_min) / (Vmax - Vmin))))
    return quantized_image

def de_quantize(image, original_bits, target_bits):
    """
    De-kuantalama işlemi.
    Formül:  floor((Vi * (Vmax - Vmin) / (V'max - V'min)))
    image: PIL.Image.Image
    bits: int
    """
    np_image = np.array(image)
    Vnew_max = (2 ** target_bits)
    Vnew_min = 0
    Vmax = (2 ** original_bits)
    Vmin = 0
    de_quantized_image = np.floor((np_image * ((Vmax - Vmin) / (Vnew_max - Vnew_min))))
    print("De quant max: ", de_quantized_image.max(), "De quant min: ", de_quantized_image.min())
    return de_quantized_image

def psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

def mae(original, compressed):
    mae = np.mean(np.abs(original - compressed))
    return mae

def apply_quantization(image, target_bits):
    """
    Kuantalama işlemi uygulayan fonksiyon.
    """
    quantized_image = quantize(image, 8, target_bits)
    de_quantized_image = de_quantize(quantized_image, 8, target_bits)
    psnr_value = psnr(np.array(image), de_quantized_image)
    mae_value = mae(np.array(image), de_quantized_image)

    new_image = Image.fromarray(de_quantized_image.astype(np.uint8))
    return new_image, psnr_value, mae_value

def info_text(bits):
    return f"The image was quantized from 8 bits to {bits} bits and then de-quantized again to 8 bits."

inp_image = Image.open("tesla_8_bit.png")

with gr.Blocks() as demo:
    with gr.Row():
        gr.Label("Image Quantization", show_label=False)
    with gr.Row():
        with gr.Column(scale=2):
            input_image = gr.Image(inp_image, label="Original Image", type="pil", interactive=False)
        with gr.Column(scale=2):
            output_image = gr.Image(label="Quantized Image", type="pil", interactive=False)
        with gr.Column(scale=1):
            slider = gr.Slider(minimum=1, maximum=7, value=7, step=1, label="Target Bits", interactive=True)
            button = gr.Button(value="Apply Quantization", interactive=True)
            info_box = gr.Textbox(label="Info", interactive=False)
            psnr_box = gr.Textbox(label="PSNR", interactive=False)
            mae_box = gr.Textbox(label="MAE", interactive=False)

    button.click(apply_quantization, inputs=[input_image, slider], outputs=[output_image, psnr_box, mae_box])
    button.click(info_text, inputs=[slider], outputs=[info_box])

demo.launch(server_name="0.0.0.0", server_port=7860, debug=True)