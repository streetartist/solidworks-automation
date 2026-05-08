# GetEntitiesType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesType`

Gets the types of entities in this sketch relation.
Gets the types of entities in this sketch relation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntitiesType() As System.Object
```

```

Dim instance As ISketchRelation
Dim value As System.Object
 
value = instance.GetEntitiesType()
```

```

System.object GetEntitiesType()
```

```

System.Object^ GetEntitiesType(); 
```

#### Return Value

Array of types of entities in this sketch relation as defined by [swSketchRelationEntityTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchRelationEntityTypes_e.html)

Example

[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)  
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.md)  
[ISketchRelation::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetEntities.md)  
[ISketchRelation::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.md)
