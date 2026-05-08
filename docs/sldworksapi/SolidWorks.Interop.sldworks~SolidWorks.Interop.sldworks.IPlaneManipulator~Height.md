# Height Property (IPlaneManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Height`

Gets or sets the height of a plane that has a manipulator.
Gets or sets the height of a plane that has a manipulator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Height As System.Double
```

```

Dim instance As IPlaneManipulator
Dim value As System.Double
 
instance.Height = value
 
value = instance.Height
```

```

System.double Height {get; set;}
```

```

property System.double Height {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Height of a plane that has a manipulator

Example

[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)  
[Insert and Use Plane with Manipulator (C#)](Insert_and_Use_Plane_with_Manipulator_Example_CSharp.htm)  
[Insert and Use Plane with Manipulator (VB.NET)](Insert_and_Use_Plane_with_Manipulator_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.md)  
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.md)  
[IPlaneManipulator::Width Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Width.md)
