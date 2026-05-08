# SketchUseEdge Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge`

Obsolete. Superseded by ISketchManager::SketchUseEdge2.
Obsolete. Superseded by [ISketchManager::SketchUseEdge2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchUseEdge2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchUseEdge( _
   ByVal Chain As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim Chain As System.Boolean
Dim value As System.Boolean
 
value = instance.SketchUseEdge(Chain)
```

```

System.bool SketchUseEdge( 
   System.bool Chain
)
```

```

System.bool SketchUseEdge( 
   System.bool Chain
) 
```

#### Parameters

*Chain*
:   True if to convert the entire chain of entities, false to convert only the selected sketch entities (see **Remarks**)

#### Return Value

True if the sketch entities are created, false if not

Remarks

Specifying true for the Chain argument converts the selected entity and any other entities that belong to the same contour or chain (contiguous, geometric entities like edges) on a sketch plane.

To display all sketch relations symbols, set [IModelDoc2::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.md) swViewSketchRelations to true, which can adversely affect performance. To hide all sketch relation symbols, set IModelDoc2::SetUserPreferenceToggle swViewSketchRelations to false, which can improve performance and was the default setting prior to SOLIDWORKS 2005.

See [IModelDoc2::SketchOffsetEntities2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.md) method for similar functionality.

Example

[Insert Sheet Metal Edge Flange (VBA)](Insert_Sheet_Metal_Edge_Flange_Example_VB.htm)  
[Offset Selected Edges in Active Sketch (VBA)](Offset_Selected_Edges_in_Active_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
