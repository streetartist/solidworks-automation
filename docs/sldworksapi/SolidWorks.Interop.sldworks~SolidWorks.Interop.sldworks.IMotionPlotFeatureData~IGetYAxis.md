# IGetYAxis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~IGetYAxis`

Gets y-axis features of a plot.
Gets y-axis features of a plot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetYAxis( _
   ByVal Count As System.Integer _
) As Feature
```

```

Dim instance As IMotionPlotFeatureData
Dim Count As System.Integer
Dim value As Feature
 
value = instance.IGetYAxis(Count)
```

```

Feature IGetYAxis( 
   System.int Count
)
```

```

Feature^ IGetYAxis( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of y-axis features

#### Return Value

- in-process, unmanaged C++: Pointer to an [array of y-axis features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMotionPlotFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData.md)  
[IMotionPlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData_members.md)  
[IMotionPlotFeatureData::GetYAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~GetYAxis.md)  
[IMotionPlotFeatureData::GetXAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~GetXAxis.md)
