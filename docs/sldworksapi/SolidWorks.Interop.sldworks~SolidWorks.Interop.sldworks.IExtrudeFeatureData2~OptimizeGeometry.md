# OptimizeGeometry Property (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~OptimizeGeometry`

Gets or sets whether to optimize the geometry of a normal cut in a sheet metal part.
Gets or sets whether to optimize the geometry of a normal cut in a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OptimizeGeometry As System.Boolean
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean
 
instance.OptimizeGeometry = value
 
value = instance.OptimizeGeometry
```

```

System.bool OptimizeGeometry {get; set;}
```

```

property System.bool OptimizeGeometry {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to optimize the geometry of a normal cut in a sheet metal part, false to not (see **Remarks**)

Remarks

Setting this property is only valid when [IExtrudeFeatureData2::NormalCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~NormalCut.md) is true.

Example

[Create Cut Extrude in Sheet Metal Part (C#)](Create_Cut_Extrude_in_Sheet_Metal_Part_Example_CSharp.htm)  
[Create Cut Extrude in Sheet Metal Part (VB.NET)](Create_Cut_Extrude_in_Sheet_Metal_Part_Example_VBNET.htm)  
[Create Cut Extrude in Sheet Metal Part (VBA)](Create_Cut_Extrude_in_Sheet_Metal_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)
