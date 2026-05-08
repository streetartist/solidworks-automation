# GetUnderlyingMemberFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember~GetUnderlyingMemberFeature`

Gets the feature for this corner member.
Gets the feature for this corner member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUnderlyingMemberFeature() As System.Object
```

```

Dim instance As ICornerMember
Dim value As System.Object
 
value = instance.GetUnderlyingMemberFeature()
```

```

System.object GetUnderlyingMemberFeature()
```

```

System.Object^ GetUnderlyingMemberFeature(); 
```

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

After calling this method to get the IFeature, use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get an [ISructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.md).

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.md)  
[ICornerMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember_members.md)
