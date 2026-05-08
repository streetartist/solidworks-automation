# SketchModifyFlip Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchModifyFlip`

Flips the the active or selected sketch about the specified coordinate system axis.
Flips the the active or selected sketch about the specified coordinate system axis.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchModifyFlip( _
   ByVal AxisFlag As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim AxisFlag As System.Integer
 
instance.SketchModifyFlip(AxisFlag)
```

```

void SketchModifyFlip( 
   System.int AxisFlag
)
```

```

void SketchModifyFlip( 
   System.int AxisFlag
) 
```

#### Parameters

*AxisFlag*
:   Axis about which to flip the sketch:

    - X = 1
    - Y = 2

Example

[Flip Sketch (VBA)](Flip_Sketch_Example_VB.htm)  
[Flip Sketch (VB.NET)](Flip_Sketch_Example_VBNET.htm)  
[Flip Sketch (C#)](Flip_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
