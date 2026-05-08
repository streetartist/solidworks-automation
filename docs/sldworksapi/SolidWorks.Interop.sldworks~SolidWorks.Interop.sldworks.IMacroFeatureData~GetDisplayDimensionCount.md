# GetDisplayDimensionCount Method (IMacroFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensionCount`

Gets the number of display dimensions for this macro feature.
Gets the number of display dimensions for this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplayDimensionCount() As System.Integer
```

```

Dim instance As IMacroFeatureData
Dim value As System.Integer
 
value = instance.GetDisplayDimensionCount()
```

```

System.int GetDisplayDimensionCount()
```

```

System.int GetDisplayDimensionCount(); 
```

#### Return Value

Number of display dimensions

Remarks

Call this method before calling [IMacroFeatureData::IGetDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetDisplayDimensions.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensions.md)
