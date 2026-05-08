# Length Property (ISketchSlot)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~Length`

Gets the length of the sketch slot.
Gets the length of the sketch slot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Length As System.Double
```

```

Dim instance As ISketchSlot
Dim value As System.Double
 
instance.Length = value
 
value = instance.Length
```

```

System.double Length {get; set;}
```

```

property System.double Length {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Length of the sketch slot

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
[ISketchSlot::LengthType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~LengthType.md)  
[ISketchSlot::Width Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~Width.md)
