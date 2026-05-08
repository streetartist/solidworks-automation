# ISetParents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParents`

Sets the parent features for this macro feature.
Sets the parent features for this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetParents( _
   ByVal ParentCount As System.Integer, _
   ByRef PFeatures As Feature _
) 
```

```

Dim instance As IMacroFeatureData
Dim ParentCount As System.Integer
Dim PFeatures As Feature
 
instance.ISetParents(ParentCount, PFeatures)
```

```

void ISetParents( 
   System.int ParentCount,
   ref Feature PFeatures
)
```

```

void ISetParents( 
   System.int ParentCount,
   Feature^% PFeatures
) 
```

#### Parameters

*ParentCount*
:   Number of parent features for this macro feature

*PFeatures*
:   - in-process, unmanaged C++: Pointer to an array of parent [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Parent features set by this method are not persistent when the macro feature is regenerated. Reset the parent features in the [SwComFeature::Regenerate](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwComFeature~Regenerate.md) handler.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetParentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParentsCount.md)  
[IMacroFeatureData::IGetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParents.md)  
[IMacroFeatureData::Parents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Parents.md)
