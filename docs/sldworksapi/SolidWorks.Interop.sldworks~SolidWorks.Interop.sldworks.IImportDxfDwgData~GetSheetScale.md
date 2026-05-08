# GetSheetScale Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetSheetScale`

Gets the sheet scale for the drawing.
Gets the sheet scale for the drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetSheetScale( _
   ByVal Sheet As System.String, _
   ByRef Numerator As System.Double, _
   ByRef Denominator As System.Double _
) 
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Numerator As System.Double
Dim Denominator As System.Double
 
instance.GetSheetScale(Sheet, Numerator, Denominator)
```

```

void GetSheetScale( 
   System.string Sheet,
   out System.double Numerator,
   out System.double Denominator
)
```

```

void GetSheetScale( 
   System.String^ Sheet,
   [Out] System.double Numerator,
   [Out] System.double Denominator
) 
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

*Numerator*
:   Numerator of the scale

*Denominator*
:   Denominator of the scale

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::SetSheetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetSheetScale.md)
