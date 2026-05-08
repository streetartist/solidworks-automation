# GetCurveCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~GetCurveCount`

Gets the number of curves for this imported curve feature.
Gets the number of curves for this imported curve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurveCount() As System.Integer
```

```

Dim instance As IImportedCurveFeatureData
Dim value As System.Integer
 
value = instance.GetCurveCount()
```

```

System.int GetCurveCount()
```

```

System.int GetCurveCount(); 
```

#### Return Value

Number of curves

Remarks

Call this method before calling [IImportedCurveFeatureData::IGetCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~IGetCurves.md).

Example

[Get Imported Curve Feature Data (C#)](Get_Imported_Curve_Feature_Data_Example_CSharp.htm)  
[Get Imported Curve Feature Data (VB.NET)](Get_Imported_Curve_Feature_Data_Example_VBNET.htm)  
[Get Imported Curve Feature Data (VBA)](Get_Imported_Curve_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportedCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData.md)  
[IImportedCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData_members.md)  
[IImportedCurveFeatureData::ISetCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~ISetCurves.md)  
[IImportedCurveFeatureData::Curves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~Curves.md)
