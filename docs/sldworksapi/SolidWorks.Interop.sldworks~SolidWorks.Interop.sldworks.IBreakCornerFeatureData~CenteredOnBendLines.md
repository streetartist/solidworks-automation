# CenteredOnBendLines Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~CenteredOnBendLines`

Gets or sets whether to center the corner cuts relative to the bend lines of this break corner feature.
Gets or sets whether to center the corner cuts relative to the bend lines of this break corner feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CenteredOnBendLines As System.Boolean
```

```

Dim instance As IBreakCornerFeatureData
Dim value As System.Boolean
 
instance.CenteredOnBendLines = value
 
value = instance.CenteredOnBendLines
```

```

System.bool CenteredOnBendLines {get; set;}
```

```

property System.bool CenteredOnBendLines {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to center the corner cuts on the bend lines, false to not

Example

[Modify Break Corner Feature (C#)](Modify_Break_Corner_Feature_Example_CSharp.htm)  
[Modify Break Corner Feature (VB.NET)](Modify_Break_Corner_Feature_Example_VBNET.htm)  
[Modify Break Corner Feature (VBA)](Modify_Break_Corner_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData.md)  
[IBreakCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.md)
