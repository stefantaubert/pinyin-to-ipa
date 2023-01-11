

from pytest import raises

from pinyin_to_ipa.transcription import get_finals


def test_bcdfghklmnprstwz_u__returns_u():
  for c in "bcdfghklmnprstwz":
    result = get_finals(f"{c}u")
    if result != "u":
      assert False


def test_bcdfghklmnprstwz_ü__returns_ü__is_fail():
  for c in "bcdfghklmnprstwz":
    result = get_finals(f"{c}ü")
    if result != "ü":
      assert False


def test_bcdfghklmnprstwz_v__returns_ü__is_fail():
  for c in "bcdfghklmnprstwz":
    result = get_finals(f"{c}v")
    if result != "ü":
      assert False

# region y/j/q/x + u/ue/uan/un (with u/v/ü)


def test_yjqx_u__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}u")
    assert result == "ü"


def test_yjqx_v__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}v")
    assert result == "ü"


def test_yjqx_ü__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}ü")
    assert result == "ü"


def test_yjqx_ue__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}ue")
    assert result == "üe"


def test_yjqx_ve__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}ve")
    assert result == "üe"


def test_yjqx_üe__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}üe")
    assert result == "üe"


def test_yjqx_un__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}un")
    assert result == "ün"


def test_yjqx_vn__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}vn")
    assert result == "ün"


def test_yjqx_ün__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}ün")
    assert result == "ün"


def test_yjqx_uan__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}uan")
    assert result == "üan"


def test_yjqx_van__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}van")
    assert result == "üan"


def test_yjqx_üan__returns_üe():
  for c in "yjqx":
    result = get_finals(f"{c}üan")
    assert result == "üan"

# endregion

# region -o


def test_ao__returns_ao():
  result = get_finals("ao")
  assert result == "ao"


def test_wo__returns_uo():
  result = get_finals("wo")
  assert result == "uo"


def test_yo__returns_o():
  result = get_finals("yo")
  assert result == "o"


def test_lo__returns_o():
  result = get_finals("lo")
  assert result == "o"


def test_bo__returns_o__is_fail():
  result = get_finals("bo")
  # should return uo?
  assert result == "o"


def test_po__returns_o__is_fail():
  result = get_finals("po")
  # should return ou?
  assert result == "o"


# endregion

# region ui/iu/un -> uei/iou/uen

# see pypinyin.standard -> IU_MAP, UI_MAP, UN_MAP
def test_zui__returns_uei():
  """ui -> uei"""
  result = get_finals("zui")
  assert result == "uei"


def test_liu__returns_iou():
  """iu -> iou"""
  result = get_finals("liu")
  assert result == "iou"


def test_lun__returns_uen():
  """un -> uen"""
  result = get_finals("lun")
  assert result == "uen"

# endregion


def test_interjections__ê__returns_none():
  result = get_finals("ê")
  assert result is None


def test_syll_cons__hng__returns_none():
  result = get_finals("hng")
  assert result is None


def test_zi__returns_i():
  result = get_finals("zi")
  assert result == "i"


def test_zhi__returns_i():
  result = get_finals("zhi")
  assert result == "i"


def test_zero_cons__yin__returns_in():
  result = get_finals("yin")
  assert result == "in"


def test_buggy_pinyin__lün__raises_no_value_error():
  result = get_finals("lün")
  assert result == "ün"


def test_invalid_pinyin__raises_value_error():
  with raises(ValueError) as error:
    get_finals("zue")
  assert error.value.args[0] == "Parameter 'normal_pinyin': Final couldn't be detected!"
