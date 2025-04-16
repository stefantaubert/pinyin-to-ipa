import gradio as gr

from pinyin_to_ipa import pinyin_to_ipa

# ri has 4 conversions


def run_gradio() -> None:
  interface = build_interface()
  interface.queue()
  interface.launch(
    share=False,
    debug=False,
    inbrowser=True,
    quiet=False,
    show_api=False,
  )


def build_interface() -> gr.Blocks:
  web_app: gr.Blocks
  with gr.Blocks(title="pinyin-to-ipa") as web_app:
    gr.Markdown(
      """
      # Pinyin to IPA conversion
      """
    )

    with gr.Tab("Conversion"):
      with gr.Row():
        with gr.Column():
          with gr.Group():
            input_txt_box = gr.Textbox(
              None,
              label="Pinyin syllable",
              placeholder="Enter the pinyin syllable you want to convert to IPA.",
              lines=1,
              max_lines=1,
            )

          convert_btn = gr.Button("Convert", variant="primary")

        with gr.Column(), gr.Group(), gr.Row(), gr.Column():
          output_txt_box = gr.Textbox(
            show_label=True,
            label="IPA",
            interactive=False,
            show_copy_button=True,
            placeholder="The IPA transcription of the input will be displayed here.",
            lines=1,
            max_lines=4,  # ri
          )

      with gr.Row():
        gr.Examples(
          examples=[
            ["pang1"],
            ["pang2"],
            ["pang3"],
            ["pang4"],
            ["pang5"],
            ["pang"],
            ["hàng"],
            ["ang"],  # no initial
            ["hng"],  # SYLLABIC_CONSONANT_MAPPINGS
            ["ê"],  # INTERJECTION_MAPPINGS
            ["io"],  # INTERJECTION_MAPPINGS
            ["er"],  # INTERJECTION_MAPPINGS
            ["zhi"],  # FINAL_MAPPING_AFTER_ZH_CH_SH_R
            ["zi"],  # FINAL_MAPPING_AFTER_Z_C_S
          ],
          fn=synt,
          inputs=[
            input_txt_box,
          ],
          outputs=[
            output_txt_box,
          ],
          label="Examples",
          cache_examples=True,
          examples_per_page=20,
        )

    with gr.Tab("Info"), gr.Column():
      gr.Markdown(
        """
        ### Phoneme Set

        - Vowels: a ɛ e ə ɚ ɤ i o ɔ u ʊ y
        - Diphthongs: ai̯ au̯ aɚ̯ ei̯ ou̯
        - Consonants: f h j k kʰ l m n p pʰ ɹ̩¹ ɻ¹ ɻ̩¹ s t ts tsʰ
          tɕ tɕʰ tʰ w x ŋ ɕ ɥ ʂ ʈʂ ʈʂʰ z̩¹ ʐ¹ ʐ̩¹

        Vowels and diphthongs contain one of these tones:

        - first tone: ˥
        - second tone: ˧˥
        - third tone: ˧˩˧
        - fourth tone: ˥˩
        - fifth tone: (nothing)

        ¹ These consonants contain also tones.

        ### Citation

        Taubert, S. (2024). pinyin-to-ipa (Version 1.0.0) [Computer software]. https://doi.org/10.5281/zenodo.15229718

        ### References

        - [https://en.wikipedia.org/wiki/Help:IPA/Mandarin](https://en.wikipedia.org/wiki/Help:IPA/Mandarin)
        - [https://en.wikipedia.org/wiki/Standard_Chinese_phonology](https://en.wikipedia.org/wiki/Standard_Chinese_phonology)
        - [https://en.wikipedia.org/wiki/Pinyin](https://en.wikipedia.org/wiki/Pinyin)
        - [https://de.wikipedia.org/wiki/Pinyin](https://de.wikipedia.org/wiki/Pinyin)
        - Duanmu, San. 2007. The Phonology of Standard Chinese. 2nd ed. Oxford;
          New York: Oxford University Press.
        - Lin, Yen-Hwei. 2007. The Sounds of Chinese. Cambridge, UK;
          New York: Cambridge University Press.

        ### Acknowledgments

        [pypinyin](https://github.com/mozillazg/python-pinyin) \\
        Funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation)
        – Project-ID 416228727 – [CRC 1410](https://gepris.dfg.de/gepris/projekt/416228727?context=projekt&task=showDetail&id=416228727)

        ### App information

        - Version: 1.0.0
        - License: [MIT](https://github.com/stefantaubert/pinyin-to-ipa?tab=MIT-1-ov-file#readme)
        - GitHub: [stefantaubert/pinyin-to-ipa](https://github.com/stefantaubert/pinyin-to-ipa)
        """
      )

    # pylint: disable=E1101:no-member
    convert_btn.click(
      fn=synt,
      inputs=[
        input_txt_box,
      ],
      outputs=[
        output_txt_box,
      ],
      queue=True,
      show_progress=False,
    )

  return web_app


def synt(pinyin: str) -> str:
  try:
    output = pinyin_to_ipa(pinyin)
  except ValueError:
    result = "No valid pinyin detected! Please make sure to enter only one syllable."
    return result

  result = "\n".join(["".join(x) for x in output])
  return result


if __name__ == "__main__":
  run_gradio()
