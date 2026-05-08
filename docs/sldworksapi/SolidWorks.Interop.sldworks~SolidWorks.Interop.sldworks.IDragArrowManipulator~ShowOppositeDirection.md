# ShowOppositeDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~ShowOppositeDirection`

Gets or sets whether to display the bidirectional handle.
Gets or sets whether to display the bidirectional handle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowOppositeDirection As System.Boolean
```

```

Dim instance As IDragArrowManipulator
Dim value As System.Boolean
 
instance.ShowOppositeDirection = value
 
value = instance.ShowOppositeDirection
```

```

System.bool ShowOppositeDirection {get; set;}
```

```

property System.bool ShowOppositeDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display the bidirectional handle, false to display the unidirectional handle

Example

See [IDragArrowManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md)  
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.md)  
[IDragArrowManipulator::AllowFlip Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~AllowFlip.md)
