# IGetEntities Method (ISketchRelation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetEntities`

Gets the entities associated with this sketch relation.
Gets the entities associated with this sketch relation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntities( _
   ByVal NumEntities As System.Integer _
) As System.Object
```

```

Dim instance As ISketchRelation
Dim NumEntities As System.Integer
Dim value As System.Object
 
value = instance.IGetEntities(NumEntities)
```

```

System.object IGetEntities( 
   System.int NumEntities
)
```

```

System.Object^ IGetEntities( 
   System.int NumEntities
) 
```

#### Parameters

*NumEntities*
:   Number of entities

#### Return Value

- in-process, unmanaged C++: Pointer to an array of entities for this sketch relation

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

When you create a sketch relation, an internal entity may also be created to define that sketch relation. For example, if you add a sketch relation by specifying or selecting a point and an edge, a sketch segment may be created. If this happens, then [ISketchRelation::GetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntities.md) and ISketchRelation::IGetEntities return the point and sketch segment. To get the actual entities used to define the sketch relation, call [ISketchRelation::GetDefinitionEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetDefinitionEntities.md) or [ISketchRelation::IGetDefinitionEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetDefinitionEntities.md).

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate any dynamically allocated memory.

Before calling this method, call [ISketchRelation::GetEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.md) to get the value for NumEntities.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)  
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.md)
