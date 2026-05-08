# SavePointsToFile Method (IFreePointCurveFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData~SavePointsToFile`

Saves the points for this free-point curve to a file.
Saves the points for this free-point curve to a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SavePointsToFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IFreePointCurveFeatureData
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.SavePointsToFile(FileName)
```

```

System.bool SavePointsToFile( 
   System.string FileName
)
```

```

System.bool SavePointsToFile( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and file name of the file to which to save the points; you can specify **.sldcrv** files or **.txt** as the filename extension

#### Return Value

True if the points are saved to the file, false if not

Remarks

Exported units, e.g., meters, of the document that owns the feature, and not necessarily those of the active document, are used when data is saved to a file.

See SOLIDWORKS Help for details about free-point curve files.

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
