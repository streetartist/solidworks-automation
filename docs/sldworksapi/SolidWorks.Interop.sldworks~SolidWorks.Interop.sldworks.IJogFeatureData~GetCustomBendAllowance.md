# GetCustomBendAllowance Method (IJogFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetCustomBendAllowance`

Gets the custom bend allowance for this jog feature.
Gets the custom bend allowance for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCustomBendAllowance() As CustomBendAllowance
```

```

Dim instance As IJogFeatureData
Dim value As CustomBendAllowance
 
value = instance.GetCustomBendAllowance()
```

```

CustomBendAllowance GetCustomBendAllowance()
```

```

CustomBendAllowance^ GetCustomBendAllowance(); 
```

#### Return Value

Pointer to the [custom gend allowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

See [IJogFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)  
[IJogFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~SetCustomBendAllowance.md)  
[IJogFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~UseDefaultBendAllowance.md)
