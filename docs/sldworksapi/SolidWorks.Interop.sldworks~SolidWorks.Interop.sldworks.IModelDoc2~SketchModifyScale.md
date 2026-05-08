# SketchModifyScale Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchModifyScale`

Scales the active or selected sketch.
Scales the active or selected sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchModifyScale( _
   ByVal ScaleFactor As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim ScaleFactor As System.Double
Dim value As System.Boolean
 
value = instance.SketchModifyScale(ScaleFactor)
```

```

System.bool SketchModifyScale( 
   System.double ScaleFactor
)
```

```

System.bool SketchModifyScale( 
   System.double ScaleFactor
) 
```

#### Parameters

*ScaleFactor*
:   Amount by which to scale sketch

#### Return Value

True if successful, false if not

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
[IModelDoc2::ToolsSketchScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ToolsSketchScale.md)
