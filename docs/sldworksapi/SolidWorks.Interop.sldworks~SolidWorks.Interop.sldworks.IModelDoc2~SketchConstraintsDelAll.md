# SketchConstraintsDelAll Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDelAll`

Deletes all of the constraints on the currently selected sketch segment.
Deletes all of the constraints on the currently selected sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchConstraintsDelAll() 
```

```

Dim instance As IModelDoc2
 
instance.SketchConstraintsDelAll()
```

```

void SketchConstraintsDelAll()
```

```

void SketchConstraintsDelAll(); 
```

Remarks

Only the constraints on the currently selected sketch segment are deleted. If two or more sketch segments are selected, this method has no effect.

Example

[Delete All Constraints in Selected Sketch (VBA)](Delete_All_Constraints_in_Selected_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SketchAddConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchAddConstraints.md)  
[IModelDoc2::SketchConstrainCoincident Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainCoincident.md)  
[IModelDoc2::SketchConstrainConcentric Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainConcentric.md)  
[IModelDoc2::SketchConstrainParallel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainParallel.md)  
[IModelDoc2::SketchConstrainPerp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainPerp.md)  
[IModelDoc2::SketchConstraintsDel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDel.md)  
[IModelDoc2::SketchConstrainTangent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainTangent.md)  
[IModelDoc2::SkToolsAutoConstr Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SkToolsAutoConstr.md)
