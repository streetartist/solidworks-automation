# UseDefaultBendAllowance Property (IHemFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~UseDefaultBendAllowance`

Gets or sets whether to use the default bend allowance state for this hem feature.
Gets or sets whether to use the default bend allowance state for this hem feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseDefaultBendAllowance As System.Boolean
```

```

Dim instance As IHemFeatureData
Dim value As System.Boolean
 
instance.UseDefaultBendAllowance = value
 
value = instance.UseDefaultBendAllowance
```

```

System.bool UseDefaultBendAllowance {get; set;}
```

```

property System.bool UseDefaultBendAllowance {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True uses the default bend allowance, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.md)  
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.md)  
[IHemFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~GetCustomBendAllowance.md)  
[IHemFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~SetCustomBendAllowance.md)
