# ChangeSketchPlane Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ChangeSketchPlane`

Obsolete. Superseded by IModelDocExtension::ChangeSketchPlane.
Obsolete. Superseded by [IModelDocExtension::ChangeSketchPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ChangeSketchPlane.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ChangeSketchPlane() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.ChangeSketchPlane()
```

```

System.bool ChangeSketchPlane()
```

```

System.bool ChangeSketchPlane(); 
```

#### Return Value

True if the change was successful, false otherwise

Remarks

Every sketch is associated with a plane (for example, a reference plane or a planar face). You must preselect the sketch and the new plane or face before using this method.

Example

[Change Plane of Sketch (VBA)](Change_Sketch_of_Plane_Example.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
