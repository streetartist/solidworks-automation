# SetCustomBendAllowance Method (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~SetCustomBendAllowance`

Sets the custom bend allowance for this swept flange feature.
Sets the custom bend allowance for this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCustomBendAllowance( _
   ByVal PBendData As System.Object _
) 
```

```

Dim instance As ISweptFlangeFeatureData
Dim PBendData As System.Object
 
instance.SetCustomBendAllowance(PBendData)
```

```

void SetCustomBendAllowance( 
   System.object PBendData
)
```

```

void SetCustomBendAllowance( 
   System.Object^ PBendData
) 
```

#### Parameters

*PBendData*
:   [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md)

Remarks

This method is valid only when creating the swept flange and only if [ISweptFlangeFeatureData::UseDefaultBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseDefaultBendAllowance.md) is false.

Use [ISweptFlangeFeatureData::GetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetCustomBendAllowance.md) to specify PBendData.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)
