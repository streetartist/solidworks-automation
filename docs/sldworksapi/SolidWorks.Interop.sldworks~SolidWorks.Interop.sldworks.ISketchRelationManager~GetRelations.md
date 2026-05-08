# GetRelations Method (ISketchRelationManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelations`

Gets all of the sketch relations in the sketch based on the specified filter.
Gets all of the sketch relations in the sketch based on the specified filter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRelations( _
   ByVal Filter As System.Integer _
) As System.Object
```

```

Dim instance As ISketchRelationManager
Dim Filter As System.Integer
Dim value As System.Object
 
value = instance.GetRelations(Filter)
```

```

System.object GetRelations( 
   System.int Filter
)
```

```

System.Object^ GetRelations( 
   System.int Filter
) 
```

#### Parameters

*Filter*
:   Sketch relation as defined in [swSketchRelationFilterType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchRelationFilterType_e.html)

#### Return Value

Array of [sketch relations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)

Remarks

Because some of the objects may be NULL, you should check for this before accessing them. You should deallocate on any dynamically allocated memory.

Example

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)  
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)  
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)  
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.md)  
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.md)  
[ISketchRelationManager::IGetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetRelations.md)  
[ISketchRelationManager::GetRelationsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetRelationsCount.md)
