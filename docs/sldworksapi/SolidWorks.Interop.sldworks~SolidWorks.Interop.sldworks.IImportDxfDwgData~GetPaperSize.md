# GetPaperSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetPaperSize`

Gets the size of the paper for the drawing.
Gets the size of the paper for the drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetPaperSize( _
   ByVal Sheet As System.String, _
   ByRef Size As System.Integer, _
   ByRef Height As System.Double, _
   ByRef Width As System.Double _
) 
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Size As System.Integer
Dim Height As System.Double
Dim Width As System.Double
 
instance.GetPaperSize(Sheet, Size, Height, Width)
```

```

void GetPaperSize( 
   System.string Sheet,
   out System.int Size,
   out System.double Height,
   out System.double Width
)
```

```

void GetPaperSize( 
   System.String^ Sheet,
   [Out] System.int Size,
   [Out] System.double Height,
   [Out] System.double Width
) 
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

*Size*
:   Size as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)

*Height*
:   If Size is swDwgPapersUserDefined, then the height of the paper in meters

*Width*
:   If Size is swDwgPapersUserDefined, then the width of the paper in meters

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::SetPaperSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetPaperSize.md)
