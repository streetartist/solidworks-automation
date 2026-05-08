# PreserveZAxis Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~PreserveZAxis`

Gets or sets whether to preserve the orientation of the Z-axis in the opposite-hand versions.
Gets or sets whether to preserve the orientation of the Z-axis in the opposite-hand versions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PreserveZAxis As System.Boolean
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean
 
instance.PreserveZAxis = value
 
value = instance.PreserveZAxis
```

```

System.bool PreserveZAxis {get; set;}
```

```

property System.bool PreserveZAxis {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to preserve the orientation of the Z-axis, false to not

Remarks

This property is valid only if [IMirrorComponentFeatureData::CreateDerivedConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~CreateDerivedConfigurations.md) is false.

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
