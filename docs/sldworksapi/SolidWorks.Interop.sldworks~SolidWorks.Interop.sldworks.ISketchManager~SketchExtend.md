# SketchExtend Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchExtend`

Adds to the length of the selected sketch entity (i.e., line, centerline, or arc) to meet the nearest sketch entity.
Adds to the length of the selected sketch entity (i.e., line, centerline, or arc) to meet the nearest sketch entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchExtend( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.SketchExtend(X, Y, Z)
```

```

System.bool SketchExtend( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.bool SketchExtend( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   Specify 0.0

*Y*
:   Specify 0.0

*Z*
:   Specify 0.0

#### Return Value

True if the sketch entity is extended to meet the nearest sketch entity, false if not

Remarks

Call this method multiple times to extend the selected line to meet successive sketch entities.

Example

[Extend Sketch Entity (VBA)](Extend_Sketch_Entity_Example_VB.htm)  
[Extend Sketch Entity (VB.NET)](Extend_Sketch_Entity_Example_VBNET.htm)  
[Extend Sketch Entity (C#)](Extend_Sketch_Entity_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::SketchTrim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchTrim.md)
