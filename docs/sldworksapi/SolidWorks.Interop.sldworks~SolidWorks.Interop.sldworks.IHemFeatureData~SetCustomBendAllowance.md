# SetCustomBendAllowance Method (IHemFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~SetCustomBendAllowance`

Sets the custom bend allowance for the hem feature.
Sets the custom bend allowance for the hem feature.

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

Dim instance As IHemFeatureData
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
:   [Custom bend allowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) for the hem feature

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.md)  
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.md)  
[IHemFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~GetCustomBendAllowance.md)  
[IHemFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~UseDefaultBendAllowance.md)
