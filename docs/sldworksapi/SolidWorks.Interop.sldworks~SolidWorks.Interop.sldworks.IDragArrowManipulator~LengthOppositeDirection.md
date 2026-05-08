# LengthOppositeDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~LengthOppositeDirection`

Gets or sets the length of the opposite handle.
Gets or sets the length of the opposite handle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LengthOppositeDirection As System.Double
```

```

Dim instance As IDragArrowManipulator
Dim value As System.Double
 
instance.LengthOppositeDirection = value
 
value = instance.LengthOppositeDirection
```

```

System.double LengthOppositeDirection {get; set;}
```

```

property System.double LengthOppositeDirection {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Length of opposite handle

Remarks

If you change the length of the handle using this property, then use [IDragArrowMainpulator::Update](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Update.md) to display the modified handle in the graphics area.

Example

See [IDragArrowManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md)  
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.md)  
[IDragArrowManipulator::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~Length.md)
