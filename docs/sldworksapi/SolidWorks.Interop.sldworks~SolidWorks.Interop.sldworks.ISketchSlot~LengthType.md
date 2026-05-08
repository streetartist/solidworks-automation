# LengthType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~LengthType`

Gets or sets the type of length of this sketch slot.
Gets or sets the type of length of this sketch slot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LengthType As System.Integer
```

```

Dim instance As ISketchSlot
Dim value As System.Integer
 
instance.LengthType = value
 
value = instance.LengthType
```

```

System.int LengthType {get; set;}
```

```

property System.int LengthType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of length of this sketch slot as defined in [swSketchSlotLengthType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchSlotLengthType_e.html)

Example

[Insert and Resize Sketch Slot (C#)](Insert_and_Resize_Sketch_Slot_Example_CSharp.htm)  
[Insert and Resize Sketch Slot (VB.NET)](Insert_and_Resize_Sketch_Slot_Example_VBNET.htm)  
[Insert and Resize Sketch Slot (VBA)](Insert_and_Resize_Sketch_Slot_Example_VB.htm)  
[Get Sketch Slot Data (VBA)](Get_Sketch_Slot_Data_Example_vb.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSlot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.md)  
[ISketchSlot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.md)  
[ISketchSlot::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~Length.md)  
[ISketchSlot::Width Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~Width.md)
