# SetEntitiesToJoin Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~SetEntitiesToJoin`

Sets the entities to join to create this composite curve.
Sets the entities to join to create this composite curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEntitiesToJoin( _
   ByVal EntVar As System.Object _
) 
```

```

Dim instance As ICompositeCurveFeatureData
Dim EntVar As System.Object
 
instance.SetEntitiesToJoin(EntVar)
```

```

void SetEntitiesToJoin( 
   System.object EntVar
)
```

```

void SetEntitiesToJoin( 
   System.Object^ EntVar
) 
```

#### Parameters

*EntVar*
:   Array of entities (see **Remarks**)

Remarks

The entities can be edges, reference curves other than composite curves, projection curves, and sketch entities.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.md)  
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.md)  
[ICompositeCurveFeatureData::ISetEntitiesToJoin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~ISetEntitiesToJoin.md)
