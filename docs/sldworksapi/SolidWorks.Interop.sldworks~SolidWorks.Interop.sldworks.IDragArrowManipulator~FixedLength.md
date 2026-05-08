# FixedLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~FixedLength`

Gets or sets whether the origin can be changed.
Gets or sets whether the origin can be changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FixedLength As System.Boolean
```

```

Dim instance As IDragArrowManipulator
Dim value As System.Boolean
 
instance.FixedLength = value
 
value = instance.FixedLength
```

```

System.bool FixedLength {get; set;}
```

```

property System.bool FixedLength {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to permit changing the origin, false to not

Remarks

Set this property to true before calling [IDragArrowManipulator::Origin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Origin.md) to change the origin.

Example

See [IDragArrowManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md)  
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.md)  
[IDragArrowManipulator::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Length.md)  
[IDragArrowManipulator::LengthOppositeDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~LengthOppositeDirection.md)
