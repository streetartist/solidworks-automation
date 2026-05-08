# InsertCurveFile Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFile`

Creates a curve.
Creates a curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCurveFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.InsertCurveFile(FileName)
```

```

System.bool InsertCurveFile( 
   System.string FileName
)
```

```

System.bool InsertCurveFile( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and file name containing the point data

#### Return Value

True if the curve is created successfully, false if not

Remarks

The curve goes through the points in the specified file.The points in the specified input file can have the X, Y, Z values separated by commas, spaces, or tabs. There should be one point per line.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertCurveFileBegin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileBegin.md)  
[IModelDoc2::InsertCurveFileEnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileEnd.md)  
[IModelDoc2::InsertCurveFilePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.md)
