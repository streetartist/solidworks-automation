# EditSketchOrSingleSketchFeature Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketchOrSingleSketchFeature`

Edits a selected sketch or feature sketch.
Edits a selected sketch or feature sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditSketchOrSingleSketchFeature() 
```

```

Dim instance As IModelDoc2
 
instance.EditSketchOrSingleSketchFeature()
```

```

void EditSketchOrSingleSketchFeature()
```

```

void EditSketchOrSingleSketchFeature(); 
```

Remarks

This method is valid when one of the following is pre-selected:

- Sketch
- Body feature that is created from one sketch
- Surface feature that is created from one sketch
- Sketch picture
- Pen sketch
- Any item that supports **Context menu RMB > Edit Sketch**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::EditSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketch.md)
