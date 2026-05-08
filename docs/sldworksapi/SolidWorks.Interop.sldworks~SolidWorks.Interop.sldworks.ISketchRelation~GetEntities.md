# GetEntities Method (ISketchRelation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntities`

Gets the entities associated with this sketch relation.
Gets the entities associated with this sketch relation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntities() As System.Object
```

```

Dim instance As ISketchRelation
Dim value As System.Object
 
value = instance.GetEntities()
```

```

System.object GetEntities()
```

```

System.Object^ GetEntities(); 
```

#### Return Value

Array of entities for this sketch relation

Remarks

When you create a sketch relation, an internal entity may also be created to define that sketch relation. For example, if you add a sketch relation by specifying or selecting a point and an edge, a sketch segment may be created. If this happens, then ISketchRelation::GetEntities and [ISketchRelation::IGetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetEntities.md) return the point and sketch segment. To get the actual entities used to define the sketch relation, call [ISketchRelation::GetDefinitionEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetDefinitionEntities.md) or [ISketchRelation::IGetDefinitionEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetDefinitionEntities.md).

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate any dynamically allocated memory.

Example

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)  
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)  
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)  
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)  
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.md)  
[ISketchRelation::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.md)
