# GetDefinitionEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetDefinitionEntities`

Obsolete. Superseded by ISketchRelation::GetDefinitionEntities2.
Obsolete. Superseded by [ISketchRelation::GetDefinitionEntities2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetDefinitionEntities2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDefinitionEntities() As System.Object
```

```

Dim instance As ISketchRelation
Dim value As System.Object
 
value = instance.GetDefinitionEntities()
```

```

System.object GetDefinitionEntities()
```

```

System.Object^ GetDefinitionEntities(); 
```

#### Return Value

Array of the actual entities for this sketch relation

Remarks

When you created a sketch relation, an internal entity may have also been created to define that sketch relation. For example, if you added a sketch relation by specifying or selecting a point and an edge, a sketch segment may have been created. If this happened, then [ISketchRelation::GetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntities.md) and [ISketchRelation::IGetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetEntities.md) would return the point and sketch segment. To get the actual entities used to define the sketch relation, call ISketchRelation::GetDefinitionEntities or [ISketchRelation::IGetDefinitionEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetDefinitionEntities.md).

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate any dynamically allocated memory.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)  
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.md)  
[ISketchRelation::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.md)
