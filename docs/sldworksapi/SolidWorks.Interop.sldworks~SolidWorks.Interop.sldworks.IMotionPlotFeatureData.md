# IMotionPlotFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData`

Allows access to a plot's feature data.
Allows access to a plot's feature data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IMotionPlotFeatureData 
```

```

Dim instance As IMotionPlotFeatureData
```

```

public interface IMotionPlotFeatureData 
```

```

public interface class IMotionPlotFeatureData 
```

Remarks

Typical steps for creating a motion study's plot data and plot:

2. Open an assembly model and create the motion study.
3. Select the model's entities whose motion you want to measure.
4. Perform the calculations and get the results.
5. Create a plot feature data.
6. Create the plot's x-axis and y-axis feature data objects.
7. Set the type of plot.
8. Select the result component.
9. Set the entities for the x-axis and y-axis feature data objects.
10. Get the plot's x-axis and y-axis values and insert and display the plot.

Examine the examples to see the calls for these steps.

Example

[Create Plots and Get Values (C#)](Create_Plots_and_Get_Values_Example_CSharp.htm)  
[Create Plots and Get Values (VB.NET)](Create_Plots_and_Get_Values_Example_VBNET.htm)  
[Create Plots and Get Values (VBA)](Create_Plots_and_Get_Values_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMotionPlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
