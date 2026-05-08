# IDimension Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members`

Allows you to get and set dimension values and tolerances.
The following tables list the members exposed by [IDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [DimensionLineDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~DimensionLineDirection.md) | Gets or sets the direction of this dimension line. |
| Property | [DrivenState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~DrivenState.md) | Gets or sets the driven state of a dimension. |
| Property | [ExtensionLineDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ExtensionLineDirection.md) | Gets or sets the direction of the extension line. |
| Property | [FullName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~FullName.md) | Gets the full name of a dimension including the feature and the model. |
| Property | [Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~Name.md) | Gets or sets the name of a dimension. |
| Property | [ReadOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReadOnly.md) | Gets or sets the read-only state of a dimension. |
| Property | [ReferencePoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReferencePoints.md) | Gets or sets the reference points for this dimension. |
| Property | [SystemValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SystemValue.md) | Obsolete. Superseded by [IDimension::GetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.md), [IDimension::IGetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.md), [IDimension::SetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.md), and [IDimension::ISetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.md). |
| Property | [Tolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~Tolerance.md) | Gets the [IDimensionTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md) object. |
| Property | [Value](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~Value.md) | Obsolete. Superseded by [IDimension::GetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.md), [IDimension::IGetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.md), [IDimension::ISetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.md), and [IDimension::SetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.md). |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetArcEndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetArcEndCondition.md) | Gets the end conditions for linear dimensions that end on an arc. |
| Method | [GetFeatureOwner](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetFeatureOwner.md) | Gets the feature for this dimension. |
| Method | [GetNameForSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetNameForSelection.md) | Gets the name of the selected dimension needed by [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md). |
| Method | [GetReferencePointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetReferencePointsCount.md) | Gets the number of reference points for this dimension. |
| Method | [GetSystemChamferValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemChamferValues.md) | Gets the chamfer dimension values in system units. |
| Method | [GetSystemValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue2.md) | Obsolete. See [IDimension::GetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.md) and [IDimension::IGetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.md). |
| Method | [GetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.md) | Gets the value of the current dimension in system units in the named configuration. |
| Method | [GetToleranceFitValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetToleranceFitValues.md) | Obsolete. Superseded by [IDimensionTolerance::GetHoleFitValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetHoleFitValue.md) and [IDimensionTolerance::GetShaftFitValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetShaftFitValue.md). |
| Method | [GetToleranceFontInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetToleranceFontInfo.md) | Obsolete. Superseded by [IDimensionTolerance::GetFontUseDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.md), [IDimensionTolerance::GetFontUseScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.md), [IDimensionTolerance::GetFontScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontScale.md), and [IDimensionTolerance::GetFontHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontHeight.md). |
| Method | [GetToleranceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetToleranceType.md) | Obsolete. Superseded by [IDimensionTolerance::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.md). |
| Method | [GetToleranceValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetToleranceValues.md) | Obsolete. Superseded by [IDimensionTolerance::GetMaxValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue.md) and [IDimensionTolerance::GetMinValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMinValue.md). |
| Method | [GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetType.md) | Gets the type of dimension. |
| Method | [GetUserValueIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.md) | Gets the value of this dimension in the units of the specified document. |
| Method | [GetValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue2.md) | Obsolete. Superseded by [IDimension::GetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.md) and [IDimension::IGetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.md). |
| Method | [GetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.md) | Gets the values of the dimensions in the specified configurations. |
| Method | [IGetReferencePoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetReferencePoints.md) | Gets the reference points for this dimension. |
| Method | [IGetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.md) | Gets the value of the current dimension in system units in the named configuration. |
| Method | [IGetToleranceFontInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetToleranceFontInfo.md) | Obsolete. Superseded by [IDimensionTolerance::GetFontUseDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.md), [IDimensionTolerance::GetFontUseScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.md), [IDimensionTolerance::GetFontScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontScale.md), and [IDimensionTolerance::GetFontHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontHeight.md). |
| Method | [IGetToleranceValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetToleranceValues.md) | Obsolete. Superseded by [IDimensionTolerance::GetMaxValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue.md) and [IDimensionTolerance::GetMinValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMinValue.md). |
| Method | [IGetUserValueIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn.md) | Obsolete. Superseded by [IDimension::IGetUserValueIn2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.md). |
| Method | [IGetUserValueIn2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.md) | Gets the value of this dimension in the units of the specified document. |
| Method | [IGetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.md) | Gets the values of the dimensions in the specified configurations. |
| Method | [IsAppliedToAllConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IsAppliedToAllConfigurations.md) | Gets whether a dimension is currently applied to all configurations of the model or to just the current configuration. |
| Method | [IsDesignTableDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IsDesignTableDimension.md) | Gets whether this dimension is driven by a design table. |
| Method | [ISetReferencePoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetReferencePoints.md) | Sets the reference points for this dimension. |
| Method | [ISetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.md) | Sets the value of this dimension in system units (meters) in the specified configuration. |
| Method | [ISetUserValueIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn.md) | Obsolete. Superseded by [IDimension::ISetUserValueIn3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.md). |
| Method | [ISetUserValueIn2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn2.md) | Obsolete. Superseded by [IDimension::ISetUserValueIn3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.md). |
| Method | [ISetUserValueIn3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.md) | Sets the value of this dimension in the units of the specified document. |
| Method | [ISetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.md) | Sets the values of the dimensions in the specified configurations. |
| Method | [IsReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IsReference.md) | Gets whether the dimension is a reference dimension. |
| Method | [SetArcEndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetArcEndCondition.md) | Sets the end conditions for linear dimensions that end on an arc. |
| Method | [SetSystemValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue2.md) | Obsolete. Superseded by [IDimension::SetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.md). |
| Method | [SetSystemValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.md) | Sets the value of this dimension in system units (meters) in the specified configuration. |
| Method | [SetToleranceFitValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceFitValues.md) | Obsolete. Superseded by [IDimensionTolerance::SetFitValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitValues.md). |
| Method | [SetToleranceFontInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceFontInfo.md) | Obsolete. Superseded by [IDimensionTolerance::SetFont](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFont.md). |
| Method | [SetToleranceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceType.md) | Obsolete. Superseded by [IDimensionTolerance::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.md). |
| Method | [SetToleranceValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceValues.md) | Obsolete. Superseded by [IDimensionTolerance::SetValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetValues.md). |
| Method | [SetUserValueIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn.md) | Obsolete. Superseded by [IDimension::SetUserValueIn2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.md). |
| Method | [SetUserValueIn2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.md) | Sets the value of this dimension in the units of the specified document. |
| Method | [SetValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue2.md) | Obsolete. Superseded by [IDimension::SetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.md). |
| Method | [SetValue3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.md) | Sets the values of the dimensions in the specified configurations. |

[Top](#top)

 

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)
