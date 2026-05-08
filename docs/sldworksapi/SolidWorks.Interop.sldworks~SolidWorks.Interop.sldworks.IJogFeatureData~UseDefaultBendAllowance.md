# UseDefaultBendAllowance Property (IJogFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~UseDefaultBendAllowance`

Gets or sets whether to use the default bend allowance for this jog feature.
Gets or sets whether to use the default bend allowance for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseDefaultBendAllowance As System.Boolean
```

```

Dim instance As IJogFeatureData
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

Example

See [IJogFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)  
[IJogFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetCustomBendAllowance.md)  
[IJogFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~SetCustomBendAllowance.md)
