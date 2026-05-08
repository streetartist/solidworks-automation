# InsertStructuralWeldment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment`

Obsolete. Superseded by IFeatureManager::InsertStructuralWeldment2.
Obsolete. Superseded by [IFeatureManager::InsertStructuralWeldment2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertStructuralWeldment( _
   ByVal Path As System.String, _
   ByVal EndCond As System.Integer, _
   ByVal Angle As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Path As System.String
Dim EndCond As System.Integer
Dim Angle As System.Double
Dim value As Feature
 
value = instance.InsertStructuralWeldment(Path, EndCond, Angle)
```

```

Feature InsertStructuralWeldment( 
   System.string Path,
   System.int EndCond,
   System.double Angle
)
```

```

Feature^ InsertStructuralWeldment( 
   System.String^ Path,
   System.int EndCond,
   System.double Angle
) 
```

#### Parameters

*Path*

*EndCond*

*Angle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
