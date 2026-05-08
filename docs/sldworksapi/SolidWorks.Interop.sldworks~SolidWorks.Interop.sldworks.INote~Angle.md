# Angle Property (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~Angle`

Controls the rotation angle of this note.
Controls the rotation angle of this note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Angle As System.Double
```

```

Dim instance As INote
Dim value As System.Double
 
instance.Angle = value
 
value = instance.Angle
```

```

System.double Angle {get; set;}
```

```

property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Rotation angle, in radians, of this note

Remarks

The rotation angle of a note must be in the -360  to +360  range. If a value is specified that is outside of the range, the angle wraps around to be mapped back into range. For example, attempting to set this property to a value of 365  would result in the angle being set to 5.

Example

[Get Corresponding Objects in Assembly Component (C#)](Get_Corresponding_Objects_in_Assembly_Component_Example_CSharp.htm)  
[Get Corresponding Objects in Assembly Component (VB.NET)](Get_Corresponding_Objects_in_Assembly_Component_Example_VBNET.htm)  
[Get Corresponding Objects in Assembly Component (VBA)](Get_Corresponding_Objects_in_Assembly_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)
