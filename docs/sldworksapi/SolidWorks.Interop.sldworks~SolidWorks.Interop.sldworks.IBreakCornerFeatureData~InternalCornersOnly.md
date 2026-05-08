# InternalCornersOnly Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData~InternalCornersOnly`

Gets or sets whether to add or subtract material from break corner/corner trim features.
Gets or sets whether to add or subtract material from break corner/corner trim features.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InternalCornersOnly As System.Boolean
```

```

Dim instance As IBreakCornerFeatureData
Dim value As System.Boolean
 
instance.InternalCornersOnly = value
 
value = instance.InternalCornersOnly
```

```

System.bool InternalCornersOnly {get; set;}
```

```

property System.bool InternalCornersOnly {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to add or subtract material from break corner/corner trim features, false to not

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
