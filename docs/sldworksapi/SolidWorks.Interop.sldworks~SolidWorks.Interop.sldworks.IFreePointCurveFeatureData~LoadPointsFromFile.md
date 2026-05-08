# LoadPointsFromFile Method (IFreePointCurveFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData~LoadPointsFromFile`

Loads the points for this free-point curve from a file.
Loads the points for this free-point curve from a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadPointsFromFile( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IFreePointCurveFeatureData
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.LoadPointsFromFile(FileName)
```

```

System.bool LoadPointsFromFile( 
   System.string FileName
)
```

```

System.bool LoadPointsFromFile( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and file name of the free-point curve file that contains the points to load; you can specify **.sldcrv** files or **.txt** files that use the same format as **.sldcrv** files

#### Return Value

True if the points loaded successfully, false if not

Remarks

See SOLIDWORKS Help for details about free-point curve files.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFreePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData.md)  
[IFreePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData_members.md)
