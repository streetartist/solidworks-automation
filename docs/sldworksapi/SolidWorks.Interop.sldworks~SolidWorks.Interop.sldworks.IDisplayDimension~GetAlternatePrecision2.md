# GetAlternatePrecision2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAlternatePrecision2`

Gets the displayed precision for the dual portion of this dimension.
Gets the displayed precision for the dual portion of this dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAlternatePrecision2() As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
value = instance.GetAlternatePrecision2()
```

```

System.int GetAlternatePrecision2()
```

```

System.int GetAlternatePrecision2(); 
```

#### Return Value

Precision setting as defined in [swDimensionPrecisionSettings\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionPrecisionSettings_e.html)

Remarks

If the return value equals swPrecisionFollowsDocumentSetting, then the precision used is the document default for dual dimension values. You can retrieve the value using [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md) with swDetailingAltLinearDimPrecision. Otherwise, the return value is the precision in the dimensions dual units.

Use [IDisplayDimension::SetPrecision2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetPrecision2.md) to set precision values on this display dimension.

Example

[Get Precisions for a Dimension (VBA)](Get_Precisions_for_a_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetPrimaryTolPrecision2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetPrimaryTolPrecision2.md)  
[IDisplayDimension:GetPrimaryPrecision2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetPrimaryPrecision2.md)  
[IDisplayDimension:GetPrimaryTolPrecision2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetPrimaryTolPrecision2.md)
