# DeSelect Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~DeSelect`

Deselects the sketch segment.
Deselects the sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeSelect() As System.Boolean
```

```

Dim instance As ISketchSegment
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

True if the sketch segment is deselected successfully, false if not

Remarks

This method does not work well when a PropertyManager page is open or a command is running. Use [IModelDoc2::DeSelectByID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeSelectByID.md) instead of using this method. IModelDoc2::DeSelectByID handles selection correctly whether or not a command is running.

To select or deselect a sketch segment, the owning document of that ISketchSegment object needs to be open and visible.

ISketchSegment selections are accessible through the [ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md) of the owning document of the sketch segment object, even if the owning document is not active.

Selection or deselection does not work for a sketch segment in a document within a drawing. Selection or deselection of sketch segments owned by the drawing does work, but only if the drawing document is active.

If the owning sketch of a sketch segment was active, or inactive, when the sketch segment was obtained, then it must be active, or inactive, to deselect it. For example, if the owning sketch of a sketch segment was active when the sketch segment was obtained, then the owning sketch must be active to select or deselect the sketch segment. Likewise, if the owning sketch of a sketch segment was inactive when the sketch segment was obtained, then the owning sketch must be inactive to select or deselect the sketch segment.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::Select4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select4.md)
