# SetCustomBendAllowance Method (IBendsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance`

Sets the custom bend allowance for the Flatten-Bends/Process-Bends feature.
Sets the custom bend allowance for the Flatten-Bends/Process-Bends feature.

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

Dim instance As IBendsFeatureData
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
:   [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.md)  
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.md)  
[IBendsFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~GetCustomBendAllowance.md)  
[IBendsFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~UseDefaultBendAllowance.md)
