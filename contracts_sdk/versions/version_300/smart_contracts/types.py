from ..common.types import (
    Balance,
    BalanceDefaultDict,
    BalanceTimeseries,
    defaultAddress,
    defaultAsset,
    Level,
    Features,
    NoteType,
    NumberKind,
    Phase,
    PostingInstructionType,
    RejectedReason,
    Tside,
    UpdatePermission,
    InvalidContractParameter,
    Rejected,
    FlagTimeseries,
    calendarObject,
    datetimeObject,
    decimalObject,
    defaultDict,
    mathObject,
    jsonDumpsObject,
    jsonLoadsObject,
    parseToDatetimeObject,
    roundFloorObject,
    roundHalfDownObject,
    roundHalfUpObject,
    timedeltaObject,
    PostingInstruction,
    PostingInstructionBatch,
    AccountIdShape,
    DateShape,
    DenominationShape,
    NumberShape,
    OptionalShape,
    OptionalValue,
    Parameter,
    ParameterTimeseries,
    StringShape,
    UnionItem,
    UnionItemValue,
    UnionShape,
    ClientTransaction,
    ClientTransactionEffects,
    ClientTransactionEffectsDefaultDict,
)


def types_registry():
    return {
        "AccountIdShape": AccountIdShape,
        "Balance": Balance,
        "BalanceDefaultDict": BalanceDefaultDict,
        "BalanceTimeseries": BalanceTimeseries,
        "calendar": calendarObject,
        "ClientTransaction": ClientTransaction,
        "ClientTransactionEffects": ClientTransactionEffects,
        "ClientTransactionEffectsDefaultDict": ClientTransactionEffectsDefaultDict,
        "DateShape": DateShape,
        "datetime": datetimeObject,
        "Decimal": decimalObject,
        "defaultdict": defaultDict,
        "DEFAULT_ADDRESS": defaultAddress,
        "DEFAULT_ASSET": defaultAsset,
        "DenominationShape": DenominationShape,
        "FlagTimeseries": FlagTimeseries,
        "InvalidContractParameter": InvalidContractParameter,
        "math": mathObject,
        "json_dumps": jsonDumpsObject,
        "json_loads": jsonLoadsObject,
        "Level": Level,
        "Features": Features,
        "NoteType": NoteType,
        "NumberShape": NumberShape,
        "NumberKind": NumberKind,
        "OptionalShape": OptionalShape,
        "OptionalValue": OptionalValue,
        "Parameter": Parameter,
        "ParameterTimeseries": ParameterTimeseries,
        "parse_to_datetime": parseToDatetimeObject,
        "Phase": Phase,
        "PostingInstruction": PostingInstruction,
        "PostingInstructionBatch": PostingInstructionBatch,
        "PostingInstructionType": PostingInstructionType,
        "Rejected": Rejected,
        "RejectedReason": RejectedReason,
        "ROUND_FLOOR": roundFloorObject,
        "ROUND_HALF_DOWN": roundHalfDownObject,
        "ROUND_HALF_UP": roundHalfUpObject,
        "StringShape": StringShape,
        "timedelta": timedeltaObject,
        "Tside": Tside,
        "UnionItem": UnionItem,
        "UnionItemValue": UnionItemValue,
        "UnionShape": UnionShape,
        "UpdatePermission": UpdatePermission,
    }
