# IGetActiveSketch2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetActiveSketch2`

Gets the active sketch.
Gets the active sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetActiveSketch2() As Sketch
```

```

Dim instance As IModelDoc2
Dim value As Sketch
 
value = instance.IGetActiveSketch2()
```

```

Sketch IGetActiveSketch2()
```

```

Sketch^ IGetActiveSketch2(); 
```

#### Return Value

Active [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

Remarks

Before you can use this method, you must select and activate a sketch. You can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select a sketch and [ISketchManager::InsertSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch.md) to make the sketch active.

For an example of getting a sketch through feature traversal, see [Get Sketches (C++)](Get_Sketches_Example_cplusplus_com.htm).

Example

[Create Cylinder (C++)](Create_Cylinder_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetActiveSketch2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetActiveSketch2.md)
