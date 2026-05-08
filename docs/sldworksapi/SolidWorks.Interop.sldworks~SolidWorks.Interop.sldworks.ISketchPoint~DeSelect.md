# DeSelect Method (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~DeSelect`

Deselects the sketch point.
Deselects the sketch point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeSelect() As System.Boolean
```

```

Dim instance As ISketchPoint
Dim value As System.Boolean
 
value = instance.DeSelect()
```

```

System.bool DeSelect()
```

```

System.bool DeSelect(); 
```

#### Return Value

True if the sketch point is deselected, false if not

Remarks

This method does not work well when a PropertyManager page is open or a command is running. Use [IModelDoc2::DeSelectByID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeSelectByID.md) instead of using this method. IModelDoc2::DeSelectByID handles selection correctly whether or not a command is running.

To select or deselect a sketch point, the owning document of that ISketchPoint object needs to be open and visible.

Sketch point selections are accessible through the [ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md) of the owning document of the SIketchPoint object, even if the owning document is not active.

Selection or deselection does not work for a sketch point in a document within a drawing. Selection or deselection of sketch points owned by the drawing does work, but only when the drawing document is active.

If the owning sketch of a sketch point was active, or inactive, when the sketch point was obtained, then it must be active, or inactive, to deselect it. For example, if the owning sketch of a sketch point was active when the sketch point was obtained, then the owning sketch must be active to select or deselect the sketch point. Likewise, if the owning sketch of a sketch point was inactive when the sketch point was obtained, then the owning sketch must be inactive to select or deselect the sketch point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)  
[ISketchPoint::Select4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Select4.md)
