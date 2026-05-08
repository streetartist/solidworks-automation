# SketchModifyRotate Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchModifyRotate`

Rotates the coordinate system of the active or selected sketch.
Rotates the coordinate system of the active or selected sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchModifyRotate( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal Angle As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim CenterX As System.Double
Dim CenterY As System.Double
Dim Angle As System.Double
 
instance.SketchModifyRotate(CenterX, CenterY, Angle)
```

```

void SketchModifyRotate( 
   System.double CenterX,
   System.double CenterY,
   System.double Angle
)
```

```

void SketchModifyRotate( 
   System.double CenterX,
   System.double CenterY,
   System.double Angle
) 
```

#### Parameters

*CenterX*
:   X point to rotate about

*CenterY*
:   Y point to rotate about

*Angle*
:   Angle of rotation

Example

[Rotate, Scale, and Copy Sketch (C#)](Rotate_Scale_Copy_Sketch_Example_CSharp.htm)  
[Rotate, Scale, and Copy Sketch (VB.NET)](Rotate_Scale_Copy_Sketch_Example_VBNET.htm)  
[Rotate, Scale, and Copy Sketch (VBA)](Rotate_Scale_Copy_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
