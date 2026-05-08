# InsertEdgeMerge Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEdgeMerge`

Merges multiple edges into a single edge using the selected faces when importing data.
Merges multiple edges into a single edge using the selected faces when importing data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertEdgeMerge( _
   ByVal Angular_tolerance As System.Double, _
   ByVal Edge_length_tolerance As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Angular_tolerance As System.Double
Dim Edge_length_tolerance As System.Double
Dim value As Feature
 
value = instance.InsertEdgeMerge(Angular_tolerance, Edge_length_tolerance)
```

```

Feature InsertEdgeMerge( 
   System.double Angular_tolerance,
   System.double Edge_length_tolerance
)
```

```

Feature^ InsertEdgeMerge( 
   System.double Angular_tolerance,
   System.double Edge_length_tolerance
) 
```

#### Parameters

*Angular\_tolerance*
:   Angular tolerance

*Edge\_length\_tolerance*
:   Edge length tolerance

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
