# SetTrimToolMember Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~SetTrimToolMember`

Sets the trim tool member for this complex corner treatment feature.
Sets the trim tool member for this complex corner treatment feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTrimToolMember( _
   ByVal Member As System.Object _
) As System.Boolean
```

```

Dim instance As IComplexCornerTreatmentFeatureData
Dim Member As System.Object
Dim value As System.Boolean
 
value = instance.SetTrimToolMember(Member)
```

```

System.bool SetTrimToolMember( 
   System.object Member
)
```

```

System.bool SetTrimToolMember( 
   System.Object^ Member
) 
```

#### Parameters

*Member*
:   [ICornerMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.md) or [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

#### Return Value

True if trim tool member successfully set, false if not

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.md)  
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.md)
