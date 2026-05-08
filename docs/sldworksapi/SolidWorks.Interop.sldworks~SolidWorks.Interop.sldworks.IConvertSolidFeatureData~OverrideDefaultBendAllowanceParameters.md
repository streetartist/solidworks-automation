# OverrideDefaultBendAllowanceParameters Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideDefaultBendAllowanceParameters`

Gets or sets whether to override the default custom bend allowance.
Gets or sets whether to override the default custom bend allowance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverrideDefaultBendAllowanceParameters As System.Boolean
```

```

Dim instance As IConvertSolidFeatureData
Dim value As System.Boolean
 
instance.OverrideDefaultBendAllowanceParameters = value
 
value = instance.OverrideDefaultBendAllowanceParameters
```

```

System.bool OverrideDefaultBendAllowanceParameters {get; set;}
```

```

property System.bool OverrideDefaultBendAllowanceParameters {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override default custom bend allowance, false to not

Remarks

The getter of this property is valid only when creating a new sheet metal feature.

Set this property to true when you want to override the bend allowance that is inherited by default from a parent sheet metal feature. Then [Initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~GetFixedFace.md) IConvertSolidFeatureData with new [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) values for the subsequent sheet metal features.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)
