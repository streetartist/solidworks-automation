# Selectable Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Selectable`

Gets or sets whether the manipulator can be selected in a PropertyManager page's selection box.
Gets or sets whether the manipulator can be selected in a PropertyManager page's selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Selectable As System.Boolean
```

```

Dim instance As IManipulator
Dim value As System.Boolean
 
instance.Selectable = value
 
value = instance.Selectable
```

```

System.bool Selectable {get; set;}
```

```

property System.bool Selectable {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the manipulator can be selected, false if not

Example

[Create PropertyManager Page and Selectable Triad Manipulator (VBA)](Create_PropertyManager_Page_and_Selectable_Triad_Manipulator_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.md)  
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.md)
