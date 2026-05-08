# ISketchSegment Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment`

Provides access to functions that are common among sketch entities.
Provides access to functions that are common among sketch entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISketchSegment 
```

```

Dim instance As ISketchSegment
```

```

public interface ISketchSegment 
```

```

public interface class ISketchSegment 
```

Remarks

A SketchSegment can represent a sketch arc, line, ellipse, parabola or spline.

ISketchSegment provides functions that are generic to every type of sketch segment. For example, every sketch segment has an ID and can be programmatically selected. Therefore, the ISketchSegment interface provides functions to obtain the ID and to select the item. (For access to sketched points, see the [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) object)

Example

[Get Sketch Segment Length (C++)](Get_Sketch_Segment_Length_Example_CPlusPlus_COM.htm)  
[Get Sketch Segment Length (VBA)](Get_Sketch_Segment_Length_Example_VB.htm)  
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)  
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)  
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)  
[Select Chain of Entities Attached to a Sketch Segment (C#)](Select_Chain_of_Entities_Example_CSharp.htm)  
[Select Chain of Entities Attached to a Sketch Segment (VB.NET)](Select_Chain_of_Entities_Example_VBNET.htm)  
[Select Chain of Entities Attached to a Sketch Segment (VBA)](Select_Chain_of_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
