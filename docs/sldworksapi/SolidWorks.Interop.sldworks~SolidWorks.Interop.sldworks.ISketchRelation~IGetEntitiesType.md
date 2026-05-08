# IGetEntitiesType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetEntitiesType`

Gets the types of entities in this sketch relation.
Gets the types of entities in this sketch relation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntitiesType( _
   ByVal NumEntities As System.Integer _
) As System.Integer
```

```

Dim instance As ISketchRelation
Dim NumEntities As System.Integer
Dim value As System.Integer
 
value = instance.IGetEntitiesType(NumEntities)
```

```

System.int IGetEntitiesType( 
   System.int NumEntities
)
```

```

System.int IGetEntitiesType( 
   System.int NumEntities
) 
```

#### Parameters

*NumEntities*
:   Number of entities

#### Return Value

- in-process, unmanaged C++: Pointer to an array of types of entities in this sketch relation as defined by [swSketchRelationEntityTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchRelationEntityTypes_e.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISketchRelation::GetEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.md) to get the value for NumEntities.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)  
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.md)  
[ISketchRelation::GetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntities.md)
