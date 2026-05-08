# SetCustomBendAllowance Method (IJogFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~SetCustomBendAllowance`

Sets the custom bend allowance for this jog feature.
Sets the custom bend allowance for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCustomBendAllowance( _
   ByVal PBendData As CustomBendAllowance _
) 
```

```

Dim instance As IJogFeatureData
Dim PBendData As CustomBendAllowance
 
instance.SetCustomBendAllowance(PBendData)
```

```

void SetCustomBendAllowance( 
   CustomBendAllowance PBendData
)
```

```

void SetCustomBendAllowance( 
   CustomBendAllowance^ PBendData
) 
```

#### Parameters

*PBendData*
:   Pointer to the [custom bend allowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)  
[IJogFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetCustomBendAllowance.md)  
[IJogFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~UseDefaultBendAllowance.md)
