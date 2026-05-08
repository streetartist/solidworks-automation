# GetOffsetReferenceType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetOffsetReferenceType`

Gets the offset reference geometry type for this jog feature.
Gets the offset reference geometry type for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOffsetReferenceType() As System.Integer
```

```

Dim instance As IJogFeatureData
Dim value As System.Integer
 
value = instance.GetOffsetReferenceType()
```

```

System.int GetOffsetReferenceType()
```

```

System.int GetOffsetReferenceType(); 
```

#### Return Value

Offset reference geometry type as defined in [swJogOffsetTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swJogOffsetTypes_e.html)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)  
[IJogFeatureData::OffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetDistance.md)  
[IJogFeatureData::OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetReference.md)  
[IJogFeatureData::OffsetType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetType.md)  
[IJogFeatureData::ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ReverseOffset.md)
