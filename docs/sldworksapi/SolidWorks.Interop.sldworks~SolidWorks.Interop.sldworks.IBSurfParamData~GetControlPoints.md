# GetControlPoints Method (IBSurfParamData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~GetControlPoints`

Gets the coordinates of a control point at a specific row and column of the control point matrix.
Gets the coordinates of a control point at a specific row and column of the control point matrix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetControlPoints( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.Object
```

```

Dim instance As IBSurfParamData
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As System.Object
 
value = instance.GetControlPoints(Row, Column)
```

```

System.object GetControlPoints( 
   System.int Row,
   System.int Column
)
```

```

System.Object^ GetControlPoints( 
   System.int Row,
   System.int Column
) 
```

#### Parameters

*Row*
:   1 <= index of row <= [ControlPointRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~ControlPointRowCount.md)

*Column*
:   1 <= index of column <= [ControlPointColumnCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~ControlPointColumnCount.md)

#### Return Value

Array of control point coordinates

Remarks

Control points are stored in (ControlPointColumnCount\*ControlPointRowCount) vectors of dimension [ControlPointDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~ControlPointDimension.md). The U direction of surface is in the row direction. The V direction of surface is in the column direction.

- For non-rational surfaces ControlPointDimension = 3, and control point coordinates are stored as [x0,y0,z0,x1,y1,z1,.........].
- For rational surfaces ControlPointDimension = 4, and control point coordinates and weights are stored as [x0,y0,z0,w0,x1,y1,z1,w1,........].
- For example, 6 control points are stored in 6 vectors of dimension 3 in a 2X3 matrix as follows:

|  |  |  |
| --- | --- | --- |
| **Row1, Column1** | **Row1, Column2** | **# Coordinates** |
| x0, y0, z0 | x1, y1, z1 | = 6 |
|  |  |  |
| **Row2, Column1** | **Row2, Column2** |  |
| x2, y2, z2 | x3, y3, z3 | = 6 |
|  |  |  |
| **Row3, Column1** | **Row3, Column2** |  |
| x4, y4, z4 | x5, y5, z5 | = 6 |
|  |  |  |
|  | **Total** | = 18 |

Example

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)  
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)  
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.md)  
[IBSurfParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.md)  
[IBSurfParamData::IGetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~IGetControlPoints.md)
