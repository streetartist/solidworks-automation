# ClearGroup2Selections Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ClearGroup2Selections`

Clears Chain Group 2 selections in this connected linkage chain pattern feature.
Clears **Chain Group 2** selections in this connected linkage chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ClearGroup2Selections() As System.Boolean
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Boolean
 
value = instance.ClearGroup2Selections()
```

```

System.bool ClearGroup2Selections()
```

```

System.bool ClearGroup2Selections(); 
```

#### Return Value

True if **Chain Group 2** selections are cleared, false if no selections for **Chain Group 2** existed (see **Remarks**)

Remarks

This method allows you to change a **Chain Group 1** and **Chain Group 2** connected linkage chain pattern feature to a **Chain Group 1** connected linkage chain pattern feature.

This property is only available to connected linkage chain patterns.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md)  
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)  
[IChainPatternFeatureData::Group2FlipPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2FlipPlane.md)  
[IChainPatternFeatureData::Group2PathLink1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink1.md)  
[IChainPatternFeatureData::Group2PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink2.md)  
[IChainPatternFeatureData::Group2PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathPlane.md)  
[IChainPatternFeatureData::Group2PatternComponent Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PatternComponent.md)
