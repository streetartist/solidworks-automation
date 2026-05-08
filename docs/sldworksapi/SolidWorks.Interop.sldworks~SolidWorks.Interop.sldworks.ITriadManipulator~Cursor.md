# Cursor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~Cursor`

Sets the cursor to use when the pointer is over the triad manipulator.
Sets the cursor to use when the pointer is over the triad manipulator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

WriteOnly Property Cursor As System.Integer
```

```

Dim instance As ITriadManipulator
 
instance.Cursor = value
```

```

System.int Cursor {set;}
```

```

property System.int Cursor {
   void set (    System.int value);
}
```

#### Property Value

Cursor to use as defined by [swManipulatorCursor\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swManipulatorCursor_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.md)  
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.md)
