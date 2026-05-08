# SketchReplace2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchReplace2`

Replaces a sketch entity in a model with another sketch entity, preserving all references.
Replaces a sketch entity in a model with another sketch entity, preserving all references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchReplace2( _
   ByVal MakeConstruction As System.Boolean, _
   ByVal MakeContour As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim MakeConstruction As System.Boolean
Dim MakeContour As System.Boolean
Dim value As System.Boolean
 
value = instance.SketchReplace2(MakeConstruction, MakeContour)
```

```

System.bool SketchReplace2( 
   System.bool MakeConstruction,
   System.bool MakeContour
)
```

```

System.bool SketchReplace2( 
   System.bool MakeConstruction,
   System.bool MakeContour
) 
```

#### Parameters

*MakeConstruction*
:   True to convert the replaced sketch entity to construction geometry, false to delete it

*MakeContour*
:   True to make the replacement sketch entity a contour, false to not

#### Return Value

True if the the sketch entity is successfully replaced, false if not

Remarks

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Append set to true to select each of the following entities:

1. Sketch entity to be replaced.
2. Replacement sketch entity that does not reference downstream geometry or have references outside of the sketch.

After calling this method, call [ISketchManager::InsertSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch.md) to rebuild the model with the replacement sketch.

Example

[Replace Sketch Entity (VBA)](Replace_Sketch_Example_VB.htm)  
[Replace Sketch Entity (VB.NET)](Replace_Sketch_Example_VBNET.htm)  
[Replace Sketch Entity (C#)](Replace_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
