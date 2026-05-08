# ISketchSplineByEqnParams Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISketchSplineByEqnParams`

Creates a spline on the active 2D sketch using the specified b-curve parameters.
Creates a spline on the active 2D sketch using the specified b-curve parameters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISketchSplineByEqnParams( _
   ByRef PropArray As System.Integer, _
   ByRef KnotsArray As System.Double, _
   ByRef CntrlPntCoordArray As System.Double _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim PropArray As System.Integer
Dim KnotsArray As System.Double
Dim CntrlPntCoordArray As System.Double
Dim value As System.Integer
 
value = instance.ISketchSplineByEqnParams(PropArray, KnotsArray, CntrlPntCoordArray)
```

```

System.int ISketchSplineByEqnParams( 
   ref System.int PropArray,
   ref System.double KnotsArray,
   ref System.double CntrlPntCoordArray
)
```

```

System.int ISketchSplineByEqnParams( 
   System.int% PropArray,
   System.double% KnotsArray,
   System.double% CntrlPntCoordArray
) 
```

#### Parameters

*PropArray*
:   Includes dimension, order, number of control points, and periodicity

*KnotsArray*
:   knot1, knot2, and so on

*CntrlPntCoordArray*
:   controlpoint1[dimension], controlpoint2[dimension], and so on

#### Return Value

True if created successfully, false if not

Remarks

The PropArray argument contains 4 integers packed into the first two doubles in the array:

- Dimension
- Order
- Number of Control Points
- Periodicity ( True or false )

The KnotsArray argument is an array of doubles with (Number of Control Points + Order) elements.

The size of the CntrlPntCoordArray array is based upon the curve dimension:

- Dimension = 2 then each control point is an array of 2 doubles ( x, y )
- Dimension = 3 then each control point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each control point is an array of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as 3 arrays, which for COM applications are passed separately.

Pass control point coordinates  to this method in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your b-curve parameters to sketch space with the help of [ISketch::ModelToSketchTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ModelToSketchTransform.md).

NOTE: If the spline being generated is a closed spline, then it must be flagged as periodic. In addition, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created.

Example

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SketchSplineByEqnParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchSplineByEqnParams2.md)  
[IModelDoc2::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplineByEqnParams.md)  
[IModelDoc2::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplinesByEqnParams.md)  
[IModelDoc2::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplineByEqnParams.md)  
[IModelDoc2::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplinesByEqnParams.md)
