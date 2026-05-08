# EditSketch Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketch`

Allows the currently selected sketch to be edited.
Allows the currently selected sketch to be edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditSketch() 
```

```

Dim instance As IModelDoc2
 
instance.EditSketch()
```

```

void EditSketch()
```

```

void EditSketch(); 
```

Remarks

This method corresponds to **SOLIDWORKS menu > Edit > Sketch**. If the selection is a feature, its underlying sketch is placed in edit mode.

After a sketch is in edit mode, you can add or delete geometry from the sketch and perform other standard sketch operations.

Example

[Autodimension All Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)  
[Delete All Constraints in Selected Sketch (VBA)](Delete_All_Constraints_in_Selected_Sketch_Example_VB.htm)  
[Get Sketch Constraints (VBA)](Get_Sketch_Constraints_Example_VB.htm)  
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Replace Sketch Text (VBA)](Replace_Sketch_Text_Example_VB.htm)  
[Create and Edit Circular Sketch Pattern (VB.NET)](Create_and_Edit_Circular_Sketch_Pattern_Example_VBNET.htm)  
[Create and Edit Circular Sketch Pattern (C#)](Create_and_Edit_Circular_Sketch_Pattern_Example_CSharp.htm)  
[Create and Edit Circular Sketch Pattern (VBA)](Create_and_Edit_Circular_Sketch_Pattern_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::EditSketchOrSingleSketchFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketchOrSingleSketchFeature.md)
