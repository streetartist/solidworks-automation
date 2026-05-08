# DeleteRelation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~DeleteRelation`

Deletes the specified logical sketch relation in sketch.
Deletes the specified logical sketch relation in sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteRelation( _
   ByVal ThisRelation As SketchRelation _
) As System.Boolean
```

```

Dim instance As ISketchRelationManager
Dim ThisRelation As SketchRelation
Dim value As System.Boolean
 
value = instance.DeleteRelation(ThisRelation)
```

```

System.bool DeleteRelation( 
   SketchRelation ThisRelation
)
```

```

System.bool DeleteRelation( 
   SketchRelation^ ThisRelation
) 
```

#### Parameters

*ThisRelation*
:   [Sketch relation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)

#### Return Value

True if the sketch relation is deleted, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.md)  
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.md)  
[ISketchRelationManager::DeleteAllRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~DeleteAllRelations.md)
