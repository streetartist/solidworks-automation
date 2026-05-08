# IGetRelations Method (ISketchRelationManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetRelations`

Gets all of the sketch relations in the sketch based on the specified filter.
Gets all of the sketch relations in the sketch based on the specified filter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRelations( _
   ByVal Filter As System.Integer, _
   ByVal Count As System.Integer _
) As SketchRelation
```

```

Dim instance As ISketchRelationManager
Dim Filter As System.Integer
Dim Count As System.Integer
Dim value As SketchRelation
 
value = instance.IGetRelations(Filter, Count)
```

```

SketchRelation IGetRelations( 
   System.int Filter,
   System.int Count
)
```

```

SketchRelation^ IGetRelations( 
   System.int Filter,
   System.int Count
) 
```

#### Parameters

*Filter*
:   Sketch relation as defined in [swSketchRelationFilterType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchRelationFilterType_e.html)

*Count*
:   Number of sketch relations

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch relations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate on any dynamically allocated memory.

Call [ISketchRelationManager::GetRelationsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelationsCount.md) before calling this method to get the value for Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.md)  
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.md)  
[ISketchRelationManager::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelations.md)
