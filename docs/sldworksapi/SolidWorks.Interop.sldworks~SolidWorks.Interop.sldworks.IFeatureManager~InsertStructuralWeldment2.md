# InsertStructuralWeldment2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment2`

Obsolete. Superseded by IFeatureManager::InsertStructuralWeldment3.
Obsolete. Superseded by [IFeatureManager::InsertStructuralWeldment3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertStructuralWeldment2( _
   ByVal Path As System.String, _
   ByVal EndCond As System.Integer, _
   ByVal Angle As System.Double, _
   ByVal Merge As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Path As System.String
Dim EndCond As System.Integer
Dim Angle As System.Double
Dim Merge As System.Boolean
Dim value As Feature
 
value = instance.InsertStructuralWeldment2(Path, EndCond, Angle, Merge)
```

```

Feature InsertStructuralWeldment2( 
   System.string Path,
   System.int EndCond,
   System.double Angle,
   System.bool Merge
)
```

```

Feature^ InsertStructuralWeldment2( 
   System.String^ Path,
   System.int EndCond,
   System.double Angle,
   System.bool Merge
) 
```

#### Parameters

*Path*
:   Path, filename, and name of the type of structural member to insert

*EndCond*
:   End condition as defined in [swSolidworksWeldmentEndCondOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSOLIDWORKSWeldmentEndCondOptions_e.html)

*Angle*
:   Angle of rotation of the sketch about the sketch segment

*Merge*
:   True to merge the bodies of the arc segments to the adjacent bodies, false to not

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IFeatureManager::InsertStructuralWeldment3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3.md)
