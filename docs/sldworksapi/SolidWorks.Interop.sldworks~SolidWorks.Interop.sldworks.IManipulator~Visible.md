# Visible Property (IManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Visible`

Gets or sets whether the manipulator is visible in this SOLIDWORKS part or assembly document.
Gets or sets whether the manipulator is visible in this SOLIDWORKS part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Visible As System.Boolean
```

```

Dim instance As IManipulator
Dim value As System.Boolean
 
instance.Visible = value
 
value = instance.Visible
```

```

System.bool Visible {get; set;}
```

```

property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the manipulator is visible, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.md)  
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.md)
