# ReferencePart Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData~ReferencePart`

Gets or sets the result component.
Gets or sets the result component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferencePart As Component2
```

```

Dim instance As IMotionPlotAxisFeatureData
Dim value As Component2
 
instance.ReferencePart = value
 
value = instance.ReferencePart
```

```

Component2 ReferencePart {get; set;}
```

```

property Component2^ ReferencePart {
   Component2^ get();
   void set (    Component2^ value);
}
```

#### Property Value

Result [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

A component is one of the vector elements. To define a vector, you need to specify a coordinate frame. You can select a part or a subassembly to define the vector with regards to the origin coordinate system of the selected part or subassembly. If nothing is selected, then the top assembly's coordinate system is used to define the vector.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMotionPlotAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData.md)  
[IMotionPlotAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData_members.md)
