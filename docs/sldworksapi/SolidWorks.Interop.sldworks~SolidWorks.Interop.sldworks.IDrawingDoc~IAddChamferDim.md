# IAddChamferDim Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddChamferDim`

Adds a chamfer dimension.
Adds a chamfer dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddChamferDim( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As DisplayDimension
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As DisplayDimension
 
value = instance.IAddChamferDim(X, Y, Z)
```

```

DisplayDimension IAddChamferDim( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

DisplayDimension^ IAddChamferDim( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X dimension

*Y*
:   Y dimension

*Z*
:   Z dimension

#### Return Value

Pointer to the newly created chamfer [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::AddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddChamferDim.md)  
[IDimension::GetSystemChamferValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemChamferValues.md)
