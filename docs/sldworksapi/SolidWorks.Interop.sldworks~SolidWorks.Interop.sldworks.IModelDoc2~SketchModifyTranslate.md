# SketchModifyTranslate Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchModifyTranslate`

Translates the coordinate system of the active or selected sketch.
Translates the coordinate system of the active or selected sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchModifyTranslate( _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal EndX As System.Double, _
   ByVal EndY As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim StartX As System.Double
Dim StartY As System.Double
Dim EndX As System.Double
Dim EndY As System.Double
 
instance.SketchModifyTranslate(StartX, StartY, EndX, EndY)
```

```

void SketchModifyTranslate( 
   System.double StartX,
   System.double StartY,
   System.double EndX,
   System.double EndY
)
```

```

void SketchModifyTranslate( 
   System.double StartX,
   System.double StartY,
   System.double EndX,
   System.double EndY
) 
```

#### Parameters

*StartX*
:   X sketch value defining the from-position

*StartY*
:   Y sketch value defining the from-position

*EndX*
:   X sketch value defining the to-position

*EndY*
:   Y sketch value defining the to-position

#### Return Value

The sketch is translated from the XY start point position to the XY end point position.

Example

[Translate Sketch (VBA)](Translate_Sketch_Example_VB.htm)  
[Translate Sketch (VB.NET)](Translate_Sketch_Example_VBNET.htm)  
[Translate Sketch (C#)](Translate_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ToolsSketchTranslate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ToolsSketchTranslate.md)
