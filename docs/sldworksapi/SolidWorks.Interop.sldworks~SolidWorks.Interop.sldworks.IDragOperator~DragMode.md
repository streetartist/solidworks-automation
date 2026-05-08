# DragMode Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragMode`

Gets or sets the drag mode for this drag operation.
Gets or sets the drag mode for this drag operation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DragMode As System.Short
```

```

Dim instance As IDragOperator
Dim value As System.Short
 
instance.DragMode = value
 
value = instance.DragMode
```

```

System.short DragMode {get; set;}
```

```

property System.short DragMode {
   System.short get();
   void set (    System.short value);
}
```

#### Property Value

- 0 = Maximum move (move geometries rigidly, if possible)
- 1 = Minimum move (move the smallest number of geometries)
- 2 = Relaxation (solve geometries using relaxation)
- 3 = No propagation (move geometries with minimal transform propagation)

Example

[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)
