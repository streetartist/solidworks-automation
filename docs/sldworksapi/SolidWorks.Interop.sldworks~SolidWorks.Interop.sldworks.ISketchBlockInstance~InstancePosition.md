# InstancePosition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~InstancePosition`

Gets or sets the position for this block instance.
Gets or sets the position for this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InstancePosition As MathPoint
```

```

Dim instance As ISketchBlockInstance
Dim value As MathPoint
 
instance.InstancePosition = value
 
value = instance.InstancePosition
```

```

MathPoint InstancePosition {get; set;}
```

```

property MathPoint^ InstancePosition {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

#### Property Value

[Position](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of this block instance

Example

[Get and Set Blocks Data in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)  
[ISketchBlockDefinition::InsertionPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~InsertionPoint.md)  
[ISketchBlockInstance::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Angle.md)  
[ISketchBlockInstance::LockAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~LockAngle.md)
