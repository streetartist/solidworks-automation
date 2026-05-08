# BreakType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~BreakType`

Gets or sets the break corner type.
Gets or sets the break corner type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BreakType As System.Integer
```

```

Dim instance As IBreakCornerFeatureData
Dim value As System.Integer
 
instance.BreakType = value
 
value = instance.BreakType
```

```

System.int BreakType {get; set;}
```

```

property System.int BreakType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Break corner type as defined in [swBreakCornerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakCornerTypes_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md)  
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.md)
