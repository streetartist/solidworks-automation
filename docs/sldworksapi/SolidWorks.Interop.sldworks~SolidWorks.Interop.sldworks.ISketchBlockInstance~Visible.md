# Visible Property (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Visible`

Gets or sets the visibility of this block instance.
Gets or sets the visibility of this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Visible As System.Integer
```

```

Dim instance As ISketchBlockInstance
Dim value As System.Integer
 
instance.Visible = value
 
value = instance.Visible
```

```

System.int Visible {get; set;}
```

```

property System.int Visible {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Block instance's visibility as defined by [swAnnotationVisibilityState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnnotationVisibilityState_e.html)

Example

[Change Visibility of Sketch Block Instances (C#)](Change_Visibility_of_Sketch_Block_Instances_Example_CSharp.htm)  
[Change Visibility of Sketch Block Instances (VB.NET)](Change_Visibility_of_Sketch_Block_Instances_Example_VBNET.htm)  
[Change Visibility of Sketch Block Instances (VBA)](Change_Visibility_of_Sketch_Block_Instances_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)
