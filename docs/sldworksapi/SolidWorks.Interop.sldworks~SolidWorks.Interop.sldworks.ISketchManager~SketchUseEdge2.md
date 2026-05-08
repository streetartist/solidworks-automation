# SketchUseEdge2 Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge2`

Obsolete. Superseded by ISketchManager::SketchUseEdge3.
Obsolete. Superseded by [ISketchManager::SketchUseEdge3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchUseEdge2( _
   ByVal Chain As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim Chain As System.Boolean
Dim value As System.Boolean
 
value = instance.SketchUseEdge2(Chain)
```

```

System.bool SketchUseEdge2( 
   System.bool Chain
)
```

```

System.bool SketchUseEdge2( 
   System.bool Chain
) 
```

#### Parameters

*Chain*
:   True to convert the entire chain of sketch entities, false to convert only the selected sketch entities (see **Remarks**)

#### Return Value

True if the sketch entities are created, false if not

Remarks

Specifying true for the Chain argument creates the selected sketch entity and any other sketch entities that belong to the same contour or chain (contiguous geometric sketch entities like sketch edges) on a sketch plane.

To display all sketch relations symbols, set [IModelDocExtension::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.md) swViewSketchRelations to true, which can adversely affect performance. To hide all sketch relation symbols, set IModelDocExtension::SetUserPreferenceToggle swViewSketchRelations to false, which can improve performance and was the default setting prior to SOLIDWORKS 2005.

Example

[Convert Faces' Edges to Sketch Entities (VB.NET)](Convert_Faces_Edges_to_Sketch_Entities_Example_VBNET.htm)  
[Convert Faces' Edges to Sketch Entities (VBA)](Convert_Faces_Edges_to_Sketch_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[IModelDoc2::SketchOffsetEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.md)
