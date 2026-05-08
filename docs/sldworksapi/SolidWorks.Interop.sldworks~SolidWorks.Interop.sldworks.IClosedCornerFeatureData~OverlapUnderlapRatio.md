# OverlapUnderlapRatio Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~OverlapUnderlapRatio`

Gets or sets the overlap/underlap ratio for this closed corner.
Gets or sets the overlap/underlap ratio for this closed corner.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OverlapUnderlapRatio As System.Double
```

```

Dim instance As IClosedCornerFeatureData
Dim value As System.Double
 
instance.OverlapUnderlapRatio = value
 
value = instance.OverlapUnderlapRatio
```

```

System.double OverlapUnderlapRatio {get; set;}
```

```

property System.double OverlapUnderlapRatio {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Ratio

Example

[Create and Modify Closed Corner Feature (C#)](Create_and_Modify_Closed_Corner_Feature_Example_CSharp.htm)  
[Create and Modify Closed Corner Feature (VB.NET)](Create_and_Modify_Closed_Corner_Feature_Example_VBNET.htm)  
[Create and Modify Closed Corner Feature (VBA)](Create_and_Modify_Closed_Corner_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.md)  
[IClosedCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.md)
