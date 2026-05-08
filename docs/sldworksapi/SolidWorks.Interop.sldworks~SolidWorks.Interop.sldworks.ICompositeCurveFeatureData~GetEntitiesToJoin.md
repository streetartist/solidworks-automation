# GetEntitiesToJoin Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoin`

Gets the entities to join to create this composite curve feature.
Gets the entities to join to create this composite curve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntitiesToJoin( _
   ByRef Type As System.Object _
) As System.Object
```

```

Dim instance As ICompositeCurveFeatureData
Dim Type As System.Object
Dim value As System.Object
 
value = instance.GetEntitiesToJoin(Type)
```

```

System.object GetEntitiesToJoin( 
   out System.object Type
)
```

```

System.Object^ GetEntitiesToJoin( 
   [Out] System.Object^ Type
) 
```

#### Parameters

*Type*
:   Type of entity as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

Array of entities (see **Remarks**)

Remarks

The entities can be edges, reference curves other than composite curves, projection curves, and sketch entities.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.md)  
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.md)  
[ICompositeCurveFeatureData::IGetEntitiesToJoin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~IGetEntitiesToJoin.md)  
[ICompositeCurveFeatureData::GetEntitiesToJoinCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoinCount.md)
