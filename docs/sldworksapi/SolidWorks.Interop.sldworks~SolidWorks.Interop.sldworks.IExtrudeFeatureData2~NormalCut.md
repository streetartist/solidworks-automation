# NormalCut Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~NormalCut`

Gets or sets whether the cut is created normal to the thickness of the sheet metal part.
Gets or sets whether the cut is created normal to the thickness of the sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NormalCut As System.Boolean
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean
 
instance.NormalCut = value
 
value = instance.NormalCut
```

```

System.bool NormalCut {get; set;}
```

```

property System.bool NormalCut {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the cut is created normal to the thickness of the sheet metal part, false if not

Remarks

To optimize the geometry of the normal cut in the sheet metal part, set [IExtrudeFeatureData2::OptimizeGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~OptimizeGeometry.md) to true.

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
