# Parents Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Parents`

Gets or sets the parent features for this macro feature.
Gets or sets the parent features for this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Parents As System.Object
```

```

Dim instance As IMacroFeatureData
Dim value As System.Object
 
instance.Parents = value
 
value = instance.Parents
```

```

System.object Parents {get; set;}
```

```

property System.Object^ Parents {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of parent [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) for this macro feature

Remarks

Parent features set by this property are not persistent when the macro feature is regenerated. Reset the parent features in the [SwComFeature::Regenerate](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwComFeature~Regenerate.md) handler.

|  |  |
| --- | --- |
| **To get the parent features...** | **Use...** |
| assigned to a macro feature by IMacroFeatureData::Parents or IMacroFeatureData::ISetParents | - IMacroFeatureData::Parents or [IMacroFeatureData::IGetParents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetParents.md)    - or- - [IFeature::GetParents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.md) or [IFeature::IGetParents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.md) |
| of a macro feature created by first selecting objects and then calling [IFeatureManager::InsertMacroFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.md) or [IFeatureManager::IInsertMacroFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.md) | - [IMacroFeatureData::GetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.md) or [IMacroFeatureData::IGetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md)    - or - - IFeature::GetParents or IFeature::IGetParents |

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetParentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetParentsCount.md)
