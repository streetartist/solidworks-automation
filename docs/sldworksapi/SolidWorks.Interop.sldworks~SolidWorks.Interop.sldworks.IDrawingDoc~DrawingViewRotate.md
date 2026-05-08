# DrawingViewRotate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DrawingViewRotate`

Rotates the selected drawing view.
Rotates the selected drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DrawingViewRotate( _
   ByVal NewAngle As System.Double _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim NewAngle As System.Double
Dim value As System.Boolean
 
value = instance.DrawingViewRotate(NewAngle)
```

```

System.bool DrawingViewRotate( 
   System.double NewAngle
)
```

```

System.bool DrawingViewRotate( 
   System.double NewAngle
) 
```

#### Parameters

*NewAngle*
:   New angle value for the drawing view

#### Return Value

True if successfully rotated, false if not

Example

[Rotate Drawing View 45 Degrees (C#)](Rotate_Drawing_View_45_Degrees_Example_CSharp.htm)  
[Rotate Drawing Veiw 45 Degrees (VB.NET)](Rotate_Drawing_View_45_Degrees_Example_VBNET.htm)  
[Rotate Drawing View 45 Degrees (VBA)](Rotate_Drawing_View_45_Degrees_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::AlignHorz Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AlignHorz.md)  
[IDrawingDoc::AlignVert Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AlignVert.md)  
[IDrawingDoc::RestoreRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~RestoreRotation.md)
