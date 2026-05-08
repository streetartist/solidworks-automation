# SketchUseEdge3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge3`

Creates sketch entities on a sketch plane by projecting selected edges, loops, faces, curves, and external sketch contours.
Creates sketch entities on a sketch plane by projecting selected edges, loops, faces, curves, and external sketch contours.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchUseEdge3( _
   ByVal Chain As System.Boolean, _
   ByVal InnerLoops As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim Chain As System.Boolean
Dim InnerLoops As System.Boolean
Dim value As System.Boolean
 
value = instance.SketchUseEdge3(Chain, InnerLoops)
```

```

System.bool SketchUseEdge3( 
   System.bool Chain,
   System.bool InnerLoops
)
```

```

System.bool SketchUseEdge3( 
   System.bool Chain,
   System.bool InnerLoops
) 
```

#### Parameters

*Chain*
:   True to convert an entire chain of sketch entities, false to convert only the selected sketch entities (see **Remarks**)

*InnerLoops*
:   True to convert the inner loops of the selected faces to sketch entities, false to not

#### Return Value

True if the sketch entities are created, false if not

Remarks

Specifying true for the Chain argument creates the selected sketch entity and any other sketch entities that belong to the same sketch contour or chain (contiguous geometric entities like sketch edges) on the sketch plane.

To display all sketch relations symbols, set [IModelDocExtension::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.md) swViewSketchRelations to true, which can adversely affect performance. To hide all sketch relation symbols, set IModelDocExtension::SetUserPreferenceToggle swViewSketchRelations to false, which can improve performance and was the default setting prior to SOLIDWORKS 2005.

Example

[Convert Edges and Inner Loops of Face to Sketch Entities (C#)](Convert_Edges_and_Inner_Loops_of_Face_to_Sketch_Entities_Example_CSharp.htm)  
[Convert Edges and Inner Loops of Face to Sketch Entities (VB.NET)](Convert_Edges_and_Inner_Loops_of_Face_to_Sketch_Entities_Example_VBNET.htm)  
[Convert Edges and Inner Loops of Face to Sketch Entities (VBA)](Convert_Edges_and_Inner_Loops_of_Face_to_Sketch_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[IModelDoc2::SketchOffsetEntities2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.md)
