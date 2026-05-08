# GetEntitiesCount Method (ISketchRelation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount`

Gets the number of entities associated with this sketch relation.
Gets the number of entities associated with this sketch relation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntitiesCount() As System.Integer
```

```

Dim instance As ISketchRelation
Dim value As System.Integer
 
value = instance.GetEntitiesCount()
```

```

System.int GetEntitiesCount()
```

```

System.int GetEntitiesCount(); 
```

#### Return Value

Number of entities for this sketch relation

Remarks

Call this method before calling [ISketchRelation::IGetDefinitionEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetDefinitionEntities.md), [ISketchRelation::IGetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetEntities.md), or [ISketchRelation::IGetEntitiesType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetEntitiesType.md) to determine the size of array for the entities or types of entities associated with the sketch relation.

Example

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)  
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.md)
