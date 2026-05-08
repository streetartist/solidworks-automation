# IGetFeatureScopeBodies Method (IMirrorPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetFeatureScopeBodies`

Gets the solid bodies that the mirror pattern feature affects in a multibody part.
Gets the solid bodies that the mirror pattern feature affects in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFeatureScopeBodies( _
   ByVal Count As System.Integer _
) As Body2
```

```

Dim instance As IMirrorPatternFeatureData
Dim Count As System.Integer
Dim value As Body2
 
value = instance.IGetFeatureScopeBodies(Count)
```

```

Body2 IGetFeatureScopeBodies( 
   System.int Count
)
```

```

Body2^ IGetFeatureScopeBodies( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of solid bodies to affect

#### Return Value

- in-process, unmanaged C++: Pointer to an array of solid [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md) of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IMirrorPatternFeatureData::GetFeatureScopeBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetFeatureScopeBodiesCount.md) to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.md)  
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.md)  
[IMirrorPatternFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetFeatureScopeBodies.md)  
[IMirrorPatternFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScope.md)  
[IMirrorPatternFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~FeatureScopeBodies.md)
