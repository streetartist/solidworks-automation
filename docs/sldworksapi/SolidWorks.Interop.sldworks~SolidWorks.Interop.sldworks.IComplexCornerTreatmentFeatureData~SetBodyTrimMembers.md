# SetBodyTrimMembers Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~SetBodyTrimMembers`

Sets the body trim members of this complex corner treatment feature.
Sets the body trim members of this complex corner treatment feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBodyTrimMembers( _
   ByVal BodyMemList As System.Object _
) As System.Boolean
```

```

Dim instance As IComplexCornerTreatmentFeatureData
Dim BodyMemList As System.Object
Dim value As System.Boolean
 
value = instance.SetBodyTrimMembers(BodyMemList)
```

```

System.bool SetBodyTrimMembers( 
   System.object BodyMemList
)
```

```

System.bool SetBodyTrimMembers( 
   System.Object^ BodyMemList
) 
```

#### Parameters

*BodyMemList*
:   Array of body trim [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.md)s

#### Return Value

True if body trim members successfully set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.md)  
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.md)
