# Visibility Property (IMotionPlotFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData~Visibility`

Gets or sets whether a plot's feature data is visible.
Gets or sets whether a plot's feature data is visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Visibility As System.Boolean
```

```

Dim instance As IMotionPlotFeatureData
Dim value As System.Boolean
 
instance.Visibility = value
 
value = instance.Visibility
```

```

System.bool Visibility {get; set;}
```

```

property System.bool Visibility {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the plot's feature data is visible, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMotionPlotFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData.md)  
[IMotionPlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData_members.md)
