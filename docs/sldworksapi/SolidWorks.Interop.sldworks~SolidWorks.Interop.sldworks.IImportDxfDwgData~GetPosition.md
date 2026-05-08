# GetPosition Method (IImportDxfDwgData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPosition`

Gets the position of the entities created in the drawing.
Gets the position of the entities created in the drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetPosition( _
   ByVal Sheet As System.String, _
   ByRef Positioning As System.Integer, _
   ByRef X As System.Double, _
   ByRef Y As System.Double _
) 
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Positioning As System.Integer
Dim X As System.Double
Dim Y As System.Double
 
instance.GetPosition(Sheet, Positioning, X, Y)
```

```

void GetPosition( 
   System.string Sheet,
   out System.int Positioning,
   out System.double X,
   out System.double Y
)
```

```

void GetPosition( 
   System.String^ Sheet,
   [Out] System.int Positioning,
   [Out] System.double X,
   [Out] System.double Y
) 
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

*Positioning*
:   Position as defined in [swDwgImportEntitiesPositioning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgImportEntitiesPositioning_e.html)

*X*
:   X coordinate of the origin of the imported drawing

*Y*
:   Y coordinate of the origin of the imported drawing

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPosition.md)
