# ISetFeatureScopeBodies Method (ILoftFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetFeatureScopeBodies`

Sets the solid bodies that the loft feature affects in a multibody part.
Sets the solid bodies that the loft feature affects in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetFeatureScopeBodies( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2 _
) 
```

```

Dim instance As ILoftFeatureData
Dim Count As System.Integer
Dim BodyArr As Body2
 
instance.ISetFeatureScopeBodies(Count, BodyArr)
```

```

void ISetFeatureScopeBodies( 
   System.int Count,
   ref Body2 BodyArr
)
```

```

void ISetFeatureScopeBodies( 
   System.int Count,
   Body2^% BodyArr
) 
```

#### Parameters

*Count*
:   Number of solid bodies to affect

*BodyArr*
:   - in-process, unmanaged C++: Pointer to an array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.md)  
[ILoftFeatureData::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetFeatureScopeBodies.md)  
[ILoftFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~FeatureScope.md)  
[ILoftFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~FeatureScopeBodies.md)  
[ILoftFeatureData::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetFeatureScopeBodiesCount.md)  
[ILoftFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~AutoSelect.md)
