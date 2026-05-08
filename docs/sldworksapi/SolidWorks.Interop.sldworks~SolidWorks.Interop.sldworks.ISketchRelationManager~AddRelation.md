# AddRelation Method (ISketchRelationManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~AddRelation`

Adds a relation to the specified entities in the active sketch.
Adds a relation to the specified entities in the active sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddRelation( _
   ByVal Entities As System.Object, _
   ByVal RelationType As System.Integer _
) As SketchRelation
```

```

Dim instance As ISketchRelationManager
Dim Entities As System.Object
Dim RelationType As System.Integer
Dim value As SketchRelation
 
value = instance.AddRelation(Entities, RelationType)
```

```

SketchRelation AddRelation( 
   System.object Entities,
   System.int RelationType
)
```

```

SketchRelation^ AddRelation( 
   System.Object^ Entities,
   System.int RelationType
) 
```

#### Parameters

*Entities*
:   Array of entities to which add the relation

*RelationType*
:   Type of relation as defined by [swConstraintType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html)

#### Return Value

[Sketch relation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)

Remarks

A sketch must be active for this method to have any effect. Use [IModelDoc2::GetActiveSketch2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetActiveSketch2.md) or [IModelDoc2::IGetActiveSketch2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetActiveSketch2.md) to determine if a sketch is active.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.md)  
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.md)  
[ISketchRelationManager::IAddRelation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IAddRelation.md)  
[ISketchRelationManager::GetRelationsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelationsCount.md)
