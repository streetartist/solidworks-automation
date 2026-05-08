# IGetDefinitionEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetDefinitionEntities`

Obsolete. Superseded by ISketchRelation::IGetDefinitionEntities2.
Obsolete. Superseded by [ISketchRelation::IGetDefinitionEntities2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetDefinitionEntities2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDefinitionEntities( _
   ByVal NumEntities As System.Integer _
) As System.Object
```

```

Dim instance As ISketchRelation
Dim NumEntities As System.Integer
Dim value As System.Object
 
value = instance.IGetDefinitionEntities(NumEntities)
```

```

System.object IGetDefinitionEntities( 
   System.int NumEntities
)
```

```

System.Object^ IGetDefinitionEntities( 
   System.int NumEntities
) 
```

#### Parameters

*NumEntities*
:   Number of actual entities

#### Return Value

- in-process, unmanaged C++: Pointer to an array of the actual entities for this sketch relation

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

When you created a sketch relation, an internal entity may have also been created to define that sketch relation. For example, if you added a sketch relation by specifying or selecting a point and an edge, a sketch segment may have been created. If this happened, then [ISketchRelation::GetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntities.md) and [ISketchRelation::IGetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~IGetEntities.md) would return the point and sketch segment. To get the actual entities used to define the sketch relation, call [ISketchRelation::GetDefinitionEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetDefinitionEntities.md) or ISketchRelation::IGetDefinitionEntities.

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate any dynamically allocated memory.

Before calling this method, call [ISketchRelation::GetEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetEntitiesCount.md) to get the value for NumEntities.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)  
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.md)
