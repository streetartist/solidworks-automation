# Insert3DSplineCurve Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Insert3DSplineCurve`

Inserts a 3D-spline curve through the selected reference points.
Inserts a 3D-spline curve through the selected reference points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Insert3DSplineCurve( _
   ByVal CurveClosed As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim CurveClosed As System.Boolean
 
instance.Insert3DSplineCurve(CurveClosed)
```

```

void Insert3DSplineCurve( 
   System.bool CurveClosed
)
```

```

void Insert3DSplineCurve( 
   System.bool CurveClosed
) 
```

#### Parameters

*CurveClosed*
:   True if you want the curve to be closed, false if not

Remarks

Before calling this method, select the reference points by calling [IModelDocExtension::SelectbyID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Marks of 1.

To create 2D splines on a sketch, use [IModelDoc2::SketchSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchSpline.md) or [IModelDoc2::CreateSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSpline.md) or [IModelDoc2::ICreateSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSpline.md).

Example

[Insert a 3D-Spline Curve (VBA)](Insert_3D_Spline_Curve_Example_VB.htm)  
[Create Curve Through Reference Points (VBA)](Create_Curve_Through_Reference_Points_Example_VB.htm)  
[Create Curve Through Reference Points (VB.NET)](Create_Curve_Through_Reference_Points_Example_VBNET.htm)  
[Create Curve Through Reference Points (C#)](Create_Curve_Through_Reference_Points_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
