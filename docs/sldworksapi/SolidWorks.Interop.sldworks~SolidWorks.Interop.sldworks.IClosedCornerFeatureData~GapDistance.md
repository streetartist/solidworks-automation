# GapDistance Property (IClosedCornerFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~GapDistance`

Gets or sets the distance for the gap in a closed corner in a sheet metal part.
Gets or sets the distance for the gap in a closed corner in a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GapDistance As System.Double
```

```

Dim instance As IClosedCornerFeatureData
Dim value As System.Double
 
instance.GapDistance = value
 
value = instance.GapDistance
```

```

System.double GapDistance {get; set;}
```

```

property System.double GapDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Gap distance

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
