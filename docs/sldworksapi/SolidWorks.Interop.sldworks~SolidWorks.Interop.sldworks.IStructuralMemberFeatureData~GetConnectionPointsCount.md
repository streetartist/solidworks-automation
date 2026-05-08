# GetConnectionPointsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPointsCount`

Gets the number of sketch points for this structural member.
Gets the number of sketch points for this structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConnectionPointsCount() As System.Integer
```

```

Dim instance As IStructuralMemberFeatureData
Dim value As System.Integer
 
value = instance.GetConnectionPointsCount()
```

```

System.int GetConnectionPointsCount()
```

```

System.int GetConnectionPointsCount(); 
```

#### Return Value

Number of sketch points

Remarks

Call this method before calling [IStructuralMemberFeatureData::IGetConnectionPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~IGetConnectionPoints.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)  
[IStructuralMemberFeatureData::GetConnectionPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~GetConnectionPoints.md)  
[IStructuralMemberFeatureData::ApplyCornerTreatment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ApplyCornerTreatment.md)  
[IStructuralMemberFeatureData::ConnectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConnectionType.md)  
[IStructuralMemberFeatureData::CornerTreatmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~CornerTreatmentType.md)
