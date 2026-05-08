# Type Property (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Type`

Gets or sets the type of sketch point.
Gets or sets the type of sketch point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Type As System.Integer
```

```

Dim instance As ISketchPoint
Dim value As System.Integer
 
instance.Type = value
 
value = instance.Type
```

```

System.int Type {get; set;}
```

```

property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of sketch point as defined in [swSketchPointType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchPointType_e.html)

Remarks

Sketch slot information is independent of the sketch point type.

Example

[Get Persistent Identifiers and Types for Sketch Points (VBA)](Get_Persistent_Identifiers_and_Type_for_Sketch_Points_Example_VB.htm)  
[Get Persistent Identifiers and Types for Sketch Points (VB.NET)](Get_Persistent_Identifiers_and_Types_for_Sketch_Points_Example_VBNET.htm)  
[Get Persistent Identifiers and Types for Sketch Points (C#)](Get_Persistent_Identifiers_and_Types_for_Sketch_Points_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)
