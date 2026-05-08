# PointArray Property (IFreePointCurveFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData~PointArray`

Gets or sets the list of X, Y, Z coordinates for the points for this free-point curve.
Gets or sets the list of X, Y, Z coordinates for the points for this free-point curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PointArray As System.Object
```

```

Dim instance As IFreePointCurveFeatureData
Dim value As System.Object
 
instance.PointArray = value
 
value = instance.PointArray
```

```

System.object PointArray {get; set;}
```

```

property System.Object^ PointArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of doubles containing 3 \* points (see **Remarks**)

Remarks

The ArrayDataIn argument is an array of doubles containing 3 \* points:

[ x1, y1, z1, x2, y2, z2, ... ]

 See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Insert Free Point Curve Feature (C#)](Insert_Free_Point_Curve_Feature_Example_CSharp.htm)  
[Insert Free Point Curve Feature (VB.NET)](Insert_Free_Point_Curve_Feature_Example_VBNET.htm)  
[Insert Free Point Curve Feature (VBA)](Insert_Free_Point_Curve_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFreePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData.md)  
[IFreePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData_members.md)
