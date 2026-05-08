# SetPrecision2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetPrecision2`

Obsolete. Superseded by IDisplayDimension::SetPrecision3.
Obsolete. Superseded by [IDisplayDimension::SetPrecision3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetPrecision3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPrecision2( _
   ByVal Primary As System.Integer, _
   ByVal Dual As System.Integer, _
   ByVal PrimaryTol As System.Integer, _
   ByVal DualTol As System.Integer _
) As System.Integer
```

```

Dim instance As IDisplayDimension
Dim Primary As System.Integer
Dim Dual As System.Integer
Dim PrimaryTol As System.Integer
Dim DualTol As System.Integer
Dim value As System.Integer
 
value = instance.SetPrecision2(Primary, Dual, PrimaryTol, DualTol)
```

```

System.int SetPrecision2( 
   System.int Primary,
   System.int Dual,
   System.int PrimaryTol,
   System.int DualTol
)
```

```

System.int SetPrecision2( 
   System.int Primary,
   System.int Dual,
   System.int PrimaryTol,
   System.int DualTol
) 
```

#### Parameters

*Primary*
:   Number of digits displayed after the decimal point in the dimension value (see **Remarks**)

*Dual*
:   Number of digits displayed after the decimal point in the dual dimension value

*PrimaryTol*
:   Number of digits displayed after the decimal point in the tolerance value (see **Remarks**)

*DualTol*
:   Number of digits displayed after the decimal point in the dual tolerance value

#### Return Value

Return status (see **Remarks**)

Remarks

The specified precision values must be in the range from 0 to 8, which indicates the number of digits after the decimal place to display that value. Alternatively, the precision values can be defined by [swDimensionPrecisionSettings\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionPrecisionSettings_e.html).

| Parameter | swDimensionPrecisionSettings\_e value | Result |
| --- | --- | --- |
| - Primary - Dual - PrimaryTol - DualTol | swDoNotChangePrecisionSetting | The current setting is not changed. |
| - Primary - Dual - PrimaryTol - DualTol | swPrecisionFollowsDocumentSetting | The number of decimal places to display adheres to the document setting. Use [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md)/ [IModelDocExtension::SetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.md).swDetailingLinearDimPrecision, swDetailingAngularDimPrecision, or swDetailingAltLinearDimPrecision to get or set that value. |
| - PrimaryTol - DualTol | swTolerancePrecisionFollowsNominal | The number of decimal places to display is the same as for the dimension or dual dimension value. |

The return value indicates the success or failure of this method. In general, a value less than 0 indicates that the method failed and SOLIDWORKS did not set any precision values. A value of 0 indicates success. A value greater than 0 indicates that a problem occurred, but the method did not fail.

- -1  Method failed; no precision values were set.
- 0   Method was successful; all precision values were set.
- 1   Primary precision value was invalid.
- 2   Alternate precision value was invalid.
- 3   Primary tolerance precision value was invalid.
- 4   Alternate tolerance precision value was invalid.

After using this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
