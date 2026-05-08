# ISetPointArray Method (IFreePointCurveFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData~ISetPointArray`

Sets the list of X, Y, Z coordinates for the points for this free-point curve.
Sets the list of X, Y, Z coordinates for the points for this free-point curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPointArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Double _
) 
```

```

Dim instance As IFreePointCurveFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Double
 
instance.ISetPointArray(FeatCount, ArrayDataIn)
```

```

void ISetPointArray( 
   System.int FeatCount,
   ref System.double ArrayDataIn
)
```

```

void ISetPointArray( 
   System.int FeatCount,
   System.double% ArrayDataIn
) 
```

#### Parameters

*FeatCount*
:   Number of features

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of doubles containing 3 \* points (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The ArrayDataIn argument is an array of doubles containing 3 \* points:

[ x1, y1, z1, x2, y2, z2, ... ]

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFreePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData.md)  
[IFreePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData_members.md)
