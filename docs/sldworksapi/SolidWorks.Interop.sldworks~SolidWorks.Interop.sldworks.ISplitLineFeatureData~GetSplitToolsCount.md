# GetSplitToolsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetSplitToolsCount`

Gets the number of tools used to make the split.
Gets the number of tools used to make the split.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplitToolsCount() As System.Integer
```

```

Dim instance As ISplitLineFeatureData
Dim value As System.Integer
 
value = instance.GetSplitToolsCount()
```

```

System.int GetSplitToolsCount()
```

```

System.int GetSplitToolsCount(); 
```

#### Return Value

Number of tools used to make the split

Remarks

Call this method before calling [ISplitLineFeatureData::IGetSplitTools](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetSplitTools.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.md)  
[ISplitLineFeatureData::ISetSplitTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTools.md)  
[ISplitLineFeatureData::SplitTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTools.md)
