# Distance Property (IBreakCornerFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~Distance`

Gets or sets the chamfer length or fillet radius, depending on the break corner type.
Gets or sets the chamfer length or fillet radius, depending on the break corner type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Distance As System.Double
```

```

Dim instance As IBreakCornerFeatureData
Dim value As System.Double
 
instance.Distance = value
 
value = instance.Distance
```

```

System.double Distance {get; set;}
```

```

property System.double Distance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Chamfer length or fillet radius

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md)  
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.md)
