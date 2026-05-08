# SetSupportingFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~SetSupportingFaces`

Sets the two, adjacent, supporting faces for this gusset feature.
Sets the two, adjacent, supporting faces for this gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSupportingFaces( _
   ByVal PFace1 As Face2, _
   ByVal PFace2 As Face2 _
) As System.Boolean
```

```

Dim instance As IGussetFeatureData
Dim PFace1 As Face2
Dim PFace2 As Face2
Dim value As System.Boolean
 
value = instance.SetSupportingFaces(PFace1, PFace2)
```

```

System.bool SetSupportingFaces( 
   Face2 PFace1,
   Face2 PFace2
)
```

```

System.bool SetSupportingFaces( 
   Face2^ PFace1,
   Face2^ PFace2
) 
```

#### Parameters

*PFace1*
:   Pointer to the first [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) object

*PFace2*
:   Pointer to the second [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) object

#### Return Value

|  |
| --- |
|  |

True if the supporting faces are set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md)  
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.md)  
[IGussetFeatureData::GetSupportingFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~GetSupportingFaces.md)
