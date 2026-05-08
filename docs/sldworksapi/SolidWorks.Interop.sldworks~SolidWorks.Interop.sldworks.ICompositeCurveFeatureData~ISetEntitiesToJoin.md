# ISetEntitiesToJoin Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~ISetEntitiesToJoin`

Sets the entities to join to create this composite curve.
Sets the entities to join to create this composite curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetEntitiesToJoin( _
   ByVal Count As System.Integer, _
   ByRef Ents As System.Object _
) 
```

```

Dim instance As ICompositeCurveFeatureData
Dim Count As System.Integer
Dim Ents As System.Object
 
instance.ISetEntitiesToJoin(Count, Ents)
```

```

void ISetEntitiesToJoin( 
   System.int Count,
   ref System.object Ents
)
```

```

void ISetEntitiesToJoin( 
   System.int Count,
   System.Object^% Ents
) 
```

#### Parameters

*Count*
:   Number of entities

*Ents*
:   in-process, unmanaged C++: Pointer to an array of entities (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The entities can be edges, reference curves other than composite curves, projection curves, and sketch entities.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.md)  
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.md)  
[ICompositeCurveFeatureData::SetEntitiesToJoin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~SetEntitiesToJoin.md)
