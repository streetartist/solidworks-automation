# GetRelationsCount Method (ISketchRelationManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelationsCount`

Gets the number of sketch relations in the sketch based on the specified filter.
Gets the number of sketch relations in the sketch based on the specified filter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRelationsCount( _
   ByVal Filter As System.Integer _
) As System.Integer
```

```

Dim instance As ISketchRelationManager
Dim Filter As System.Integer
Dim value As System.Integer
 
value = instance.GetRelationsCount(Filter)
```

```

System.int GetRelationsCount( 
   System.int Filter
)
```

```

System.int GetRelationsCount( 
   System.int Filter
) 
```

#### Parameters

*Filter*
:   Sketch relation as defined in [swSketchRelationFilterType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchRelationFilterType_e.html)

#### Return Value

Number of sketch relations

Remarks

Call this method before calling [ISketchRelationManager::IAddRelation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IAddRelation.md) and [ISketchRelationManager::IGetRelations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetRelations.md) to get the size of the array for that method.

Example

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.md)  
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.md)  
[ISketchRelationManager::AddRelation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~AddRelation.md)  
[ISketchRelationManager::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelations.md)
