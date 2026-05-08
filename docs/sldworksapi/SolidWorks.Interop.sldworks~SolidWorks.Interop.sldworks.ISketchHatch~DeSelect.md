# DeSelect Method (ISketchHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~DeSelect`

Deselects the sketch hatch.
Deselects the sketch hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeSelect() As System.Boolean
```

```

Dim instance As ISketchHatch
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

True if the sketch hatch is deselected, false if not

Remarks

This method does not work well when a PropertyManager page is open or a command is running. Use [IModelDoc2::DeSelectByID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeSelectByID.md) instead of using this method. IModelDoc2::DeSelectByID handles selection correctly whether or not a command is running.

To select or deselect a sketch hatch, the owning document of the ISketchHatch object needs to be open and visible.

ISketchHatch selections are accessible through the [ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md) of the owning document of the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md) object, even if the owning document is not active.

Selection or deselection does not work for a sketch hatch in a component within an assembly. Selection or deselection does not work for a sketch hatch in a document within a drawing. Selection or deselection of sketch hatches owned by the top-level assembly or drawing works, but only if the assembly document or the drawing document is active.

If the owning sketch of a sketch hatch is active (inactive) when the sketch hatch is obtained, then it must be active (inactive) to deselect it. For example, if the owning sketch of a sketch hatch was active when the sketch hatch was obtained, then the owning sketch must be active to select or deselect the sketch hatch. Likewise, if the owning sketch of a sketch hatch was inactive when the sketch hatch was obtained, then the owning sketch must be inactive to select or deselect the sketch hatch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)  
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.md)  
[ISketchHatch::Select4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Select4.md)
