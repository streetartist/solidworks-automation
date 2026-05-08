# IGetParents Method (IMacroFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParents`

Gets the parent features of this macro feature.
Gets the parent features of this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetParents( _
   ByVal ParentCount As System.Integer, _
   ByRef PFeatures As Feature _
) 
```

```

Dim instance As IMacroFeatureData
Dim ParentCount As System.Integer
Dim PFeatures As Feature
 
instance.IGetParents(ParentCount, PFeatures)
```

```

void IGetParents( 
   System.int ParentCount,
   out Feature PFeatures
)
```

```

void IGetParents( 
   System.int ParentCount,
   [Out] Feature^ PFeatures
) 
```

#### Parameters

*ParentCount*
:   Number of parent features for this macro feature

*PFeatures*
:   - in-process, unmanaged C++: Pointer to an array of [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) of parents of this macro feature

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

|  |  |
| --- | --- |
| **To get the parent features...** | **Use...** |
| assigned to a macro feature by [IMacroFeatureData::Parents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Parents.md) or [IMacroFeatureData::ISetParents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetParents.md) | - IMacroFeatureData::Parents or IMacroFeatureData::IGetParents    - or- - [IFeature::GetParents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.md) or [IFeature::IGetParents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.md) |
| of a macro feature created by first selecting objects and then calling [IFeatureManager::InsertMacroFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.md) or [IFeatureManager::IInsertMacroFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.md) | - [IMacroFeatureData::GetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.md) or [IMacroFeatureData::IGetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md)    - or - - IFeature::GetParents or IFeature::IGetParents |

Before calling this method, call [IMacroFeatureData::GetParentsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParentsCount.md) to determine the value of ParentCount.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)
