# IGetRelations Method (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~IGetRelations`

Gets the sketch relations for this sketch point.
Gets the sketch relations for this sketch point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRelations( _
   ByVal Count As System.Integer _
) As SketchRelation
```

```

Dim instance As ISketchPoint
Dim Count As System.Integer
Dim value As SketchRelation
 
value = instance.IGetRelations(Count)
```

```

SketchRelation IGetRelations( 
   System.int Count
)
```

```

SketchRelation^ IGetRelations( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of sketch relations

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch relations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISketchPoint::GetRelationsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetRelationsCount.md) to get the value for Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)  
[ISketchPoint::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetRelations.md)
