# InsertCurveFileEnd Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileEnd`

Creates a curve.
Creates a curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCurveFileEnd() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.InsertCurveFileEnd()
```

```

System.bool InsertCurveFileEnd()
```

```

System.bool InsertCurveFileEnd(); 
```

#### Return Value

True if curve is created successfully, false if not

Remarks

This method:

- is the last method called to create a curve.
- and [IModelDoc2::InsertCurveFileBegin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileBegin.md) must enclose all of the calls to [IModelDoc2::InsertCurveFilePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.md).

See the examples.

Example

[Insert Free Point Curve Feature (C#)](Insert_Free_Point_Curve_Feature_Example_CSharp.htm)  
[Insert Free Point Curve Feature (VB.NET)](Insert_Free_Point_Curve_Feature_Example_VBNET.htm)  
[Insert Free Point Curve Feature (VBA)](Insert_Free_Point_Curve_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertCurveFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFile.md)
