# IGetEntitiesToJoin Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~IGetEntitiesToJoin`

Gets the entities to join to create this composite curve.
Gets the entities to join to create this composite curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntitiesToJoin( _
   ByVal Count As System.Integer, _
   ByRef Type As System.Integer _
) As System.Object
```

```

Dim instance As ICompositeCurveFeatureData
Dim Count As System.Integer
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.IGetEntitiesToJoin(Count, Type)
```

```

System.object IGetEntitiesToJoin( 
   System.int Count,
   out System.int Type
)
```

```

System.Object^ IGetEntitiesToJoin( 
   System.int Count,
   [Out] System.int Type
) 
```

#### Parameters

*Count*
:   Number of entities

*Type*
:   Type of entity as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

- in-process, unmanaged C++: Pointer to an array of entities (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The entities can be edges, reference curves other than composite curves, projection curves, and sketch entities. Call [ICompositeCurveFeatureData::GetEntitiesToJoinCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoinCount.md) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.md)  
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.md)  
[ICompositeCurveFeatureData::GetEntitiesToJoin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoin.md)
