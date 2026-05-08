# Entities Property (IMotionPlotAxisFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData~Entities`

Gets or sets the entities whose motion you want to measure.
Gets or sets the entities whose motion you want to measure.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Entities As System.Object
```

```

Dim instance As IMotionPlotAxisFeatureData
Dim value As System.Object
 
instance.Entities = value
 
value = instance.Entities
```

```

System.object Entities {get; set;}
```

```

property System.Object^ Entities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [entities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) to measure

Remarks

See the SOLIDWORKS Motion Studies Help for details about which entities can be measured.

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
