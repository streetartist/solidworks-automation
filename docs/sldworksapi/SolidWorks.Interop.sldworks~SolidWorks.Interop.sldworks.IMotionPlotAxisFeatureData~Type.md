# Type Property (IMotionPlotAxisFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData~Type`

Gets or sets the type of plot.
Gets or sets the type of plot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Type As System.Integer
```

```

Dim instance As IMotionPlotAxisFeatureData
Dim value As System.Integer
 
instance.Type = value
 
value = instance.Type
```

```

System.int Type {get; set;}
```

```

property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of plot as defined in [swMotionPlotAxisType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMotionPlotAxisType_e.html)

Example

[Create Plots and Get Values (C#)](Create_Plots_and_Get_Values_Example_CSharp.htm)  
[Create Plots and Get Values (VB.NET)](Create_Plots_and_Get_Values_Example_VBNET.htm)  
[Create Plots and Get Values (VBA)](Create_Plots_and_Get_Values_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMotionPlotAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData.md)  
[IMotionPlotAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData_members.md)
