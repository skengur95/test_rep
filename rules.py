from config import GRACE_SEC, MIN_PEOPLE


def judge(count, handover_elapsed=None, fallen=False):
    """2인 1조 판정

    count            : 구역 안 인원수
    handover_elapsed : 교대 수신호 후 지난 시간(초). 수신호가 없었으면 None
    fallen           : 쓰러진 사람이 있으면 True
    돌려주는 값      : "NORMAL" / "GRACE" / "WARNING" / "EMERGENCY"
    """
    if fallen:
        return "EMERGENCY"
    if count >= MIN_PEOPLE:
        return "NORMAL"
    if handover_elapsed is not None and handover_elapsed < GRACE_SEC:
        return "GRACE"
    return "WARNING"
