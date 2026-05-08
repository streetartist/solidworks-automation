# AddYAxis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~AddYAxis`

Adds y-axis feature to a plot.
Adds y-axis feature to a plot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddYAxis( _
   ByVal YAxis As MotionPlotAxisFeatureData _
) As System.Boolean
```

```

Dim instance As IMotionPlotFeatureData
Dim YAxis As MotionPlotAxisFeatureData
Dim value As System.Boolean
 
value = instance.AddYAxis(YAxis)
```

```

System.bool AddYAxis( 
   MotionPlotAxisFeatureData YAxis
)
```

```

System.bool AddYAxis( 
   MotionPlotAxisFeatureData^ YAxis
) 
```

#### Parameters

*YAxis*
:   [Y-axis feature data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData.md)

#### Return Value

True if y-axis feature is added to the plot, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMotionPlotFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData.md)  
[IMotionPlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData_members.md)  
[IMotionPlotFeatureData::GetYAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~GetYAxis.md)  
[IMotionPlotFeatureData::IGetYAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~IGetYAxis.md)
