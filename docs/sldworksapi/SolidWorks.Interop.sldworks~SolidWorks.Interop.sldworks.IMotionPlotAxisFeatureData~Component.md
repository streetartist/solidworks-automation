# Component Property (IMotionPlotAxisFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData~Component`

Gets or sets the component of the result vector quantity.
Gets or sets the component of the result vector quantity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Component As System.Integer
```

```

Dim instance As IMotionPlotAxisFeatureData
Dim value As System.Integer
 
instance.Component = value
 
value = instance.Component
```

```

System.int Component {get; set;}
```

```

property System.int Component {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Component of the result vector quantity as defined in [swMotionPlotAxisComponent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMotionPlotAxisComponent_e.html)

Remarks

Some motion study results, such as linear displacement/velocity results, are a 3D vector where x, y, and z can be the component of the quantity. For example, if you want the x component of the result vector, then set this property to swMotionPlotAxisComponent\_X.

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
[IMotionPlotAxisFeatureData::ReferencePart Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData~ReferencePart.md)
